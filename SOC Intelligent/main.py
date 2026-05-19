"""
=============================================================================
SOC INTELLIGENT BASÉ SUR IA - BACKEND PRINCIPAL
=============================================================================
Fichier : main.py
Description : Détection d'intrusions réseau sur le dataset NSL-KDD
              avec deux modèles ML : Random Forest & SVM.
=============================================================================
"""

# ─── Imports ────────────────────────────────────────────────────────────────
import os
import sys
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import joblib
import urllib.request

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

# ─── Chemins de sauvegarde ──────────────────────────────────────────────────
MODELS_DIR        = "models"
os.makedirs(MODELS_DIR, exist_ok=True)

RF_MODEL_PATH     = os.path.join(MODELS_DIR, "random_forest_model.joblib")
SVM_MODEL_PATH    = os.path.join(MODELS_DIR, "svm_model.joblib")
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, "preprocessor.joblib")
TEST_DATA_PATH    = os.path.join(MODELS_DIR, "test_data.joblib")
METRICS_PATH      = os.path.join(MODELS_DIR, "metrics.joblib")

# ─── Colonnes NSL-KDD ───────────────────────────────────────────────────────
NSL_KDD_COLUMNS = [
    "duration", "protocol_type", "service", "flag", "src_bytes",
    "dst_bytes", "land", "wrong_fragment", "urgent", "hot",
    "num_failed_logins", "logged_in", "num_compromised", "root_shell",
    "su_attempted", "num_root", "num_file_creations", "num_shells",
    "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate",
    "label", "difficulty_level"
]

CATEGORICAL_COLS = ["protocol_type", "service", "flag"]
NUMERIC_COLS = [
    col for col in NSL_KDD_COLUMNS
    if col not in CATEGORICAL_COLS + ["label", "difficulty_level"]
]

# ─── URLs dataset ────────────────────────────────────────────────────────────
TRAIN_URL  = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt"
TEST_URL   = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest+.txt"
TRAIN_FILE = "KDDTrain+.txt"
TEST_FILE  = "KDDTest+.txt"


# =============================================================================
# SECTION 1 : COMPRENDRE LES DONNÉES
# =============================================================================

def download_dataset():
    """Télécharge le dataset NSL-KDD si absent localement."""
    for url, filename in [(TRAIN_URL, TRAIN_FILE), (TEST_URL, TEST_FILE)]:
        if not os.path.exists(filename):
            print(f"  → Téléchargement de {filename}...")
            try:
                urllib.request.urlretrieve(url, filename)
                print(f"  ✓ {filename} téléchargé.")
            except Exception as e:
                print(f"  ✗ Erreur : {e}")
                sys.exit(1)
        else:
            print(f"  ✓ {filename} trouvé localement.")


def load_dataset():
    """Charge et fusionne KDDTrain+ et KDDTest+."""
    download_dataset()
    df_train = pd.read_csv(TRAIN_FILE, header=None, names=NSL_KDD_COLUMNS)
    df_test  = pd.read_csv(TEST_FILE,  header=None, names=NSL_KDD_COLUMNS)
    df = pd.concat([df_train, df_test], ignore_index=True)
    df.drop(columns=["difficulty_level"], inplace=True, errors="ignore")
    return df


def comprendre_les_donnees(df):
    """Section 1 : Analyse exploratoire du dataset."""
    print("\n" + "="*70)
    print("  SECTION 1 : COMPRENDRE LES DONNÉES")
    print("="*70)

    print(f"\n📊 Dimensions : {df.shape[0]:,} lignes × {df.shape[1]} colonnes")

    print("\n📋 Types de colonnes :")
    for dtype, count in df.dtypes.value_counts().items():
        print(f"   {str(dtype):<12} → {count} colonnes")

    print(f"\n🎯 Variable cible : 'label'")
    print(f"   Features numériques    : {len(NUMERIC_COLS)}")
    print(f"   Features catégorielles : {len(CATEGORICAL_COLS)}  {CATEGORICAL_COLS}")

    # Distribution des labels bruts
    print("\n📈 Distribution des labels bruts (top 10) :")
    label_counts = df["label"].value_counts().head(10)
    for label, count in label_counts.items():
        pct = count / len(df) * 100
        bar = "█" * max(1, int(pct / 2))
        print(f"   {label:<20} {count:>7,}  ({pct:5.1f}%) {bar}")

    # Binaire
    df["binary_label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)
    n_normal = (df["binary_label"] == 0).sum()
    n_attack = (df["binary_label"] == 1).sum()
    total    = len(df)
    print(f"\n📈 Classification binaire (Normal=0 / Attaque=1) :")
    print(f"   Normal  : {n_normal:>7,}  ({100*n_normal/total:.1f}%)")
    print(f"   Attaque : {n_attack:>7,}  ({100*n_attack/total:.1f}%)")

    missing = df.isnull().sum().sum()
    print(f"\n🔍 Valeurs manquantes : {'Aucune ✓' if missing == 0 else missing}")

    return df


# =============================================================================
# SECTION 2 : PRÉPARATION DES DONNÉES
# =============================================================================

def preparer_les_donnees(df):
    """Section 2 : Nettoyage, encodage OneHot, normalisation StandardScaler."""
    print("\n" + "="*70)
    print("  SECTION 2 : PRÉPARATION DES DONNÉES")
    print("="*70)

    # 2.1 — Nettoyage
    n_init = len(df)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    print(f"\n🧹 Nettoyage :")
    print(f"   Avant : {n_init:,} lignes  →  Après : {len(df):,} lignes")
    print(f"   Supprimées : {n_init - len(df):,} doublons/NaN")

    # 2.2 — Séparation X / y
    X = df.drop(columns=["label", "binary_label"], errors="ignore")
    y = df["binary_label"].values

    numeric_features     = [c for c in NUMERIC_COLS     if c in X.columns]
    categorical_features = [c for c in CATEGORICAL_COLS if c in X.columns]

    print(f"\n✂️  Séparation X / y :")
    print(f"   X shape : {X.shape}")
    print(f"   y shape : {y.shape}  — {(y==0).sum():,} normaux, {(y==1).sum():,} attaques")

    # 2.3 — ColumnTransformer : StandardScaler + OneHotEncoder
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
             categorical_features),
        ],
        remainder="drop"
    )

    print(f"\n⚙️  ColumnTransformer configuré :")
    print(f"   StandardScaler   → {len(numeric_features)} features numériques")
    print(f"   OneHotEncoder    → {len(categorical_features)} features catégorielles")
    print(f"   Note : Le fit() se fera UNIQUEMENT sur X_train (pas de data leakage).")

    return X, y, preprocessor, numeric_features, categorical_features


# =============================================================================
# SECTION 3 : MODÈLES DE DÉTECTION
# =============================================================================

def evaluer_modele(y_true, y_pred, model_name):
    """Calcule et affiche toutes les métriques d'évaluation."""
    acc  = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec  = recall_score(y_true, y_pred, zero_division=0)
    f1   = f1_score(y_true, y_pred, zero_division=0)
    cm   = confusion_matrix(y_true, y_pred)

    print(f"\n📊 Métriques — {model_name} :")
    print(f"   Accuracy  : {acc:.4f}  ({acc*100:.2f}%)")
    print(f"   Precision : {prec:.4f}")
    print(f"   Recall    : {rec:.4f}")
    print(f"   F1-Score  : {f1:.4f}")

    print(f"\n   Matrice de confusion :")
    print(f"                   Prédit Normal  Prédit Attaque")
    print(f"   Réel Normal     {cm[0][0]:>13,}  {cm[0][1]:>14,}")
    print(f"   Réel Attaque    {cm[1][0]:>13,}  {cm[1][1]:>14,}")

    print(f"\n   Rapport de classification complet :")
    report = classification_report(
        y_true, y_pred, target_names=["Normal", "Attaque"], zero_division=0
    )
    for line in report.split("\n"):
        print(f"   {line}")

    return {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1, "cm": cm}


def entrainer_et_evaluer(X, y, preprocessor):
    """Section 3 : Entraînement et évaluation de Random Forest + SVM."""
    print("\n" + "="*70)
    print("  SECTION 3 : MODÈLES DE DÉTECTION ML")
    print("="*70)

    # Split 80% train / 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n🔀 Split 80/20 (stratifié) :")
    print(f"   Entraînement : {X_train.shape[0]:,} samples")
    print(f"   Test         : {X_test.shape[0]:,} samples")

    # Prétraitement — fit sur X_train uniquement
    print("\n⚙️  Fit du préprocesseur sur X_train uniquement...")
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc  = preprocessor.transform(X_test)
    print(f"   Shape après prétraitement : {X_train_proc.shape}")

    # Sauvegarde du préprocesseur fitté
    joblib.dump(preprocessor, PREPROCESSOR_PATH)
    print(f"   ✓ Préprocesseur sauvegardé → {PREPROCESSOR_PATH}")

    # Sauvegarde du jeu de test (pour simulation en Section 4)
    joblib.dump({"X_test": X_test, "y_test": y_test,
                 "X_test_proc": X_test_proc}, TEST_DATA_PATH)

    all_metrics = {}

    # ─────────────────────────────────────────────────────────────────────────
    # MODÈLE 1 : Random Forest
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "─"*50)
    print("🌲 MODÈLE 1 : Random Forest Classifier")
    print("─"*50)
    print("   Hyperparamètres : n_estimators=100, max_depth=20,")
    print("                     min_samples_split=5, n_jobs=-1")

    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1          # utilise tous les cœurs CPU disponibles
    )
    print("  → Entraînement en cours...")
    rf_model.fit(X_train_proc, y_train)
    print("  ✓ Entraînement terminé.")

    y_pred_rf = rf_model.predict(X_test_proc)
    rf_metrics = evaluer_modele(y_test, y_pred_rf, "Random Forest")
    all_metrics["Random Forest"] = rf_metrics

    joblib.dump(rf_model, RF_MODEL_PATH)
    print(f"\n  ✓ Modèle Random Forest sauvegardé → {RF_MODEL_PATH}")

    # Importance des features (top 10)
    feature_names_num = preprocessor.named_transformers_["num"].get_feature_names_out() \
        if hasattr(preprocessor.named_transformers_["num"], "get_feature_names_out") \
        else np.array([f"num_{i}" for i in range(X_train_proc.shape[1])])
    try:
        feature_names_cat = preprocessor.named_transformers_["cat"].get_feature_names_out()
        all_feature_names = np.concatenate([feature_names_num, feature_names_cat])
    except:
        all_feature_names = np.array([f"feature_{i}" for i in range(X_train_proc.shape[1])])

    importances = rf_model.feature_importances_
    top10_idx = np.argsort(importances)[::-1][:10]
    print("\n  🔑 Top 10 features les plus importantes (Random Forest) :")
    for rank, idx in enumerate(top10_idx):
        fname = all_feature_names[idx] if idx < len(all_feature_names) else f"feature_{idx}"
        print(f"     {rank+1:>2}. {fname:<40} {importances[idx]:.4f}")

    # ─────────────────────────────────────────────────────────────────────────
    # MODÈLE 2 : SVM
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "─"*50)
    print("⚡ MODÈLE 2 : Support Vector Machine (SVM)")
    print("─"*50)
    print("   Hyperparamètres : kernel=rbf, C=1.0, gamma=scale, probability=True")
    print("   ⚠️  Le SVM est O(n²) en mémoire — sous-échantillonnage si nécessaire.")

    # Sous-échantillonnage pour le SVM (scalabilité sur grand dataset)
    MAX_SVM_SAMPLES = 50_000
    if X_train_proc.shape[0] > MAX_SVM_SAMPLES:
        print(f"   → Sous-échantillonnage stratifié à {MAX_SVM_SAMPLES:,} samples...")
        idx_svm = np.random.choice(X_train_proc.shape[0], MAX_SVM_SAMPLES, replace=False)
        X_svm, y_svm = X_train_proc[idx_svm], y_train[idx_svm]
    else:
        X_svm, y_svm = X_train_proc, y_train

    svm_model = SVC(
        kernel="rbf",       # Radial Basis Function — bon pour données non-linéaires
        C=1.0,              # paramètre de régularisation
        gamma="scale",      # 1 / (n_features * X.var()) — adaptatif
        probability=True,   # active predict_proba() via Platt scaling
        random_state=42
    )
    print("  → Entraînement en cours...")
    svm_model.fit(X_svm, y_svm)
    print("  ✓ Entraînement terminé.")

    y_pred_svm = svm_model.predict(X_test_proc)
    svm_metrics = evaluer_modele(y_test, y_pred_svm, "SVM (kernel RBF)")
    all_metrics["SVM"] = svm_metrics

    joblib.dump(svm_model, SVM_MODEL_PATH)
    print(f"\n  ✓ Modèle SVM sauvegardé → {SVM_MODEL_PATH}")

    # ─────────────────────────────────────────────────────────────────────────
    # Tableau comparatif
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "="*70)
    print("  COMPARAISON DES DEUX MODÈLES ML")
    print("="*70)
    print(f"\n  {'Métrique':<18} {'Random Forest':>15} {'SVM (RBF)':>15}")
    print("  " + "─"*50)
    for metric in ["accuracy", "precision", "recall", "f1"]:
        rf_val  = rf_metrics[metric]
        svm_val = svm_metrics[metric]
        mark_rf  = " ◄ meilleur" if rf_val >= svm_val else ""
        mark_svm = " ◄ meilleur" if svm_val > rf_val  else ""
        print(f"  {metric.capitalize():<18} {rf_val:>14.4f}{mark_rf}")
        print(f"  {'':<18} {'':>14}  {svm_val:>14.4f}{mark_svm}")
        print()

    best = "Random Forest" if rf_metrics["f1"] >= svm_metrics["f1"] else "SVM"
    print(f"  🏆 Meilleur modèle selon le F1-score : {best}")

    # Sauvegarde des métriques pour le dashboard Streamlit
    joblib.dump(all_metrics, METRICS_PATH)
    print(f"  ✓ Métriques sauvegardées → {METRICS_PATH}")

    return rf_model, svm_model, preprocessor, X_test, y_test, X_test_proc


# =============================================================================
# SECTION 4 : SIMULATION EN TEMPS RÉEL
# =============================================================================

def predire_evenement(raw_data_point, rf_model, svm_model, preprocessor, use_model="rf"):
    """
    Prend un point de données brut et retourne la prédiction.

    Le prétraitement appliqué ici est IDENTIQUE à celui de l'entraînement
    (même objet preprocessor fitté sur X_train).

    Paramètres :
        raw_data_point : pd.Series ou dict contenant les features brutes
        use_model      : "rf" pour Random Forest, "svm" pour SVM
    Retourne :
        (label_str, confidence) : ("NORMAL" | "ATTACK DETECTED", float)
    """
    # Conversion en DataFrame une ligne
    if isinstance(raw_data_point, pd.Series):
        df_point = raw_data_point.to_frame().T
    else:
        df_point = pd.DataFrame([raw_data_point])

    # Retirer les colonnes non-features si présentes
    for col in ["label", "binary_label", "difficulty_level"]:
        df_point.drop(columns=[col], inplace=True, errors="ignore")

    # Prétraitement IDENTIQUE à l'entraînement
    X_proc = preprocessor.transform(df_point)

    if use_model == "rf":
        pred  = rf_model.predict(X_proc)[0]
        proba = rf_model.predict_proba(X_proc)[0]
        conf  = float(proba[pred])
    else:
        pred  = svm_model.predict(X_proc)[0]
        proba = svm_model.predict_proba(X_proc)[0]
        conf  = float(proba[pred])

    label_str = "NORMAL" if pred == 0 else "ATTACK DETECTED"
    return label_str, conf


def simuler_temps_reel(X_test, y_test, rf_model, svm_model, preprocessor):
    """Section 4 : Simulation sur 10 échantillons aléatoires."""
    print("\n" + "="*70)
    print("  SECTION 4 : SIMULATION EN TEMPS RÉEL")
    print("="*70)

    # Rechargement depuis fichiers pour valider la persistance
    print("\n📂 Rechargement des modèles depuis disque (validation de la persistance)...")
    rf_loaded   = joblib.load(RF_MODEL_PATH)
    svm_loaded  = joblib.load(SVM_MODEL_PATH)
    pp_loaded   = joblib.load(PREPROCESSOR_PATH)
    print("  ✓ Modèles rechargés avec succès.")

    print(f"\n🔍 Simulation sur 10 échantillons aléatoires du jeu de test :")
    print("─"*70)

    indices     = np.random.choice(len(X_test), size=10, replace=False)
    correct_rf  = 0
    correct_svm = 0

    for i, idx in enumerate(indices):
        raw_sample = X_test.iloc[idx]
        true_label = "NORMAL" if y_test[idx] == 0 else "ATTACK"

        pred_rf,  conf_rf  = predire_evenement(raw_sample, rf_loaded, svm_loaded, pp_loaded, "rf")
        pred_svm, conf_svm = predire_evenement(raw_sample, rf_loaded, svm_loaded, pp_loaded, "svm")

        ok_rf  = (pred_rf  == "NORMAL") == (y_test[idx] == 0)
        ok_svm = (pred_svm == "NORMAL") == (y_test[idx] == 0)
        if ok_rf:  correct_rf  += 1
        if ok_svm: correct_svm += 1

        icon_rf  = "🟢" if pred_rf  == "NORMAL" else "🔴"
        icon_svm = "🟢" if pred_svm == "NORMAL" else "🔴"
        mark_rf  = "✓" if ok_rf  else "✗"
        mark_svm = "✓" if ok_svm else "✗"

        print(f"\n  Échantillon {i+1:>2} | Vrai label : {true_label:<7}")
        print(f"    🌲 RF  : {icon_rf} {pred_rf:<20} (confiance : {conf_rf:.2%}) {mark_rf}")
        print(f"    ⚡ SVM : {icon_svm} {pred_svm:<20} (confiance : {conf_svm:.2%}) {mark_svm}")

    print("\n" + "─"*70)
    print(f"  📈 Score sur 10 échantillons :")
    print(f"     Random Forest : {correct_rf}/10 correctes")
    print(f"     SVM           : {correct_svm}/10 correctes")


# =============================================================================
# POINT D'ENTRÉE PRINCIPAL
# =============================================================================

def main():
    print("\n" + "█"*70)
    print("█" + " "*14 + "SOC INTELLIGENT — DÉTECTION D'INTRUSIONS IDS" + " "*10 + "█")
    print("█" + " "*18 + "Random Forest  +  SVM  •  NSL-KDD" + " "*16 + "█")
    print("█"*70)

    print("\n⏳ Chargement du dataset NSL-KDD...")
    df = load_dataset()

    df = comprendre_les_donnees(df)
    X, y, preprocessor, _, _ = preparer_les_donnees(df)
    rf_model, svm_model, preprocessor, X_test, y_test, _ = entrainer_et_evaluer(
        X, y, preprocessor
    )
    simuler_temps_reel(X_test, y_test, rf_model, svm_model, preprocessor)

    print("\n" + "="*70)
    print("  ✅ Pipeline complet terminé avec succès !")
    print(f"  📁 Fichiers sauvegardés dans : ./{MODELS_DIR}/")
    print("     - random_forest_model.joblib")
    print("     - svm_model.joblib")
    print("     - preprocessor.joblib")
    print("     - test_data.joblib")
    print("     - metrics.joblib")
    print("  🚀 Lancez maintenant : streamlit run app.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
