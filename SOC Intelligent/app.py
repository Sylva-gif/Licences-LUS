"""
=============================================================================
SOC INTELLIGENT BASÉ SUR IA - FRONTEND STREAMLIT
=============================================================================
Fichier : app.py
Description : Dashboard interactif de détection d'intrusions réseau.
              Modèles : Random Forest & SVM sur NSL-KDD.
Usage      : streamlit run app.py
=============================================================================
"""

# ─── Imports ────────────────────────────────────────────────────────────────
import os
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import joblib
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ─── Configuration de la page ────────────────────────────────────────────────
st.set_page_config(
    page_title="SOC Intelligent — IDS Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS personnalisé ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
  font-family: 'IBM Plex Sans', sans-serif;
  background-color: #070d1a;
  color: #c9d4e8;
}
.stApp { background: #070d1a; }

h1 { font-family:'IBM Plex Mono',monospace !important; color:#38bdf8 !important; letter-spacing:-1px; }
h2 { font-family:'IBM Plex Mono',monospace !important; color:#818cf8 !important; }
h3 { color:#94a3b8 !important; }

/* Cartes de métriques */
.kpi-card {
  background: linear-gradient(145deg, #0f1d35, #0d1829);
  border: 1px solid #1e3a5f;
  border-radius: 14px;
  padding: 22px 18px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.kpi-card::before {
  content:'';
  position:absolute; top:0; left:0; right:0; height:3px;
  border-radius:14px 14px 0 0;
}
.kpi-card.blue::before  { background: linear-gradient(90deg, #38bdf8, #818cf8); }
.kpi-card.green::before { background: linear-gradient(90deg, #34d399, #6ee7b7); }
.kpi-card.red::before   { background: linear-gradient(90deg, #f87171, #fca5a5); }
.kpi-card.amber::before { background: linear-gradient(90deg, #fbbf24, #f59e0b); }

.kpi-num {
  font-family:'IBM Plex Mono',monospace;
  font-size:2.4rem; font-weight:700; margin:10px 0 4px;
}
.kpi-label { font-size:0.75rem; color:#475569; text-transform:uppercase; letter-spacing:.1em; }
.kpi-sub   { font-size:0.8rem; color:#64748b; margin-top:4px; }
.kpi-blue  { color:#38bdf8; }
.kpi-green { color:#34d399; }
.kpi-red   { color:#f87171; }
.kpi-amber { color:#fbbf24; }

/* Section header */
.sec-hdr {
  border-left: 4px solid #38bdf8;
  background: linear-gradient(90deg, #0f1d35, transparent);
  padding: 10px 18px; margin: 28px 0 18px;
  font-family:'IBM Plex Mono',monospace;
  font-size:.8rem; color:#38bdf8;
  text-transform:uppercase; letter-spacing:.12em;
  border-radius:0 6px 6px 0;
}

/* Alertes */
.alert-normal {
  background: linear-gradient(135deg, #052e16, #064e3b);
  border: 2px solid #059669; border-radius: 16px;
  padding: 32px; text-align: center;
  box-shadow: 0 0 50px rgba(5,150,105,.2);
  animation: glow-green 2s ease-in-out infinite;
}
.alert-attack {
  background: linear-gradient(135deg, #3b0606, #5c0f0f);
  border: 2px solid #dc2626; border-radius: 16px;
  padding: 32px; text-align: center;
  box-shadow: 0 0 50px rgba(220,38,38,.25);
  animation: glow-red 1.2s ease-in-out infinite;
}
@keyframes glow-green {
  0%,100% { box-shadow: 0 0 30px rgba(5,150,105,.15); }
  50%      { box-shadow: 0 0 60px rgba(5,150,105,.4); }
}
@keyframes glow-red {
  0%,100% { box-shadow: 0 0 30px rgba(220,38,38,.2); }
  50%      { box-shadow: 0 0 60px rgba(220,38,38,.5); }
}
.status-txt-normal { font-family:'IBM Plex Mono',monospace; font-size:2rem; font-weight:700; color:#34d399; }
.status-txt-attack { font-family:'IBM Plex Mono',monospace; font-size:2rem; font-weight:700; color:#fca5a5; }

/* Badge statut */
.badge-on  { background:#052e16; color:#34d399; border:1px solid #059669;
             padding:3px 10px; border-radius:20px; font-size:.72rem;
             font-family:'IBM Plex Mono',monospace; font-weight:600; }
.badge-off { background:#3b0606; color:#fca5a5; border:1px solid #dc2626;
             padding:3px 10px; border-radius:20px; font-size:.72rem;
             font-family:'IBM Plex Mono',monospace; font-weight:600; }

/* Metric bar */
.metric-bar-wrap { background:#0f1d35; border-radius:6px; height:8px; margin:4px 0; overflow:hidden; }
.metric-bar-rf   { background:linear-gradient(90deg,#38bdf8,#818cf8); height:100%; border-radius:6px; }
.metric-bar-svm  { background:linear-gradient(90deg,#34d399,#6ee7b7); height:100%; border-radius:6px; }

/* Info box */
.info-box {
  background:#0f1d35; border:1px solid #1e3a5f;
  border-radius:10px; padding:16px; margin:8px 0;
}

/* Buttons */
.stButton > button {
  background: linear-gradient(135deg, #1d4ed8, #38bdf8) !important;
  color: #fff !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-weight: 600 !important; font-size:.95rem !important;
  border: none !important; border-radius: 8px !important;
  padding: 14px 24px !important; width: 100% !important;
  box-shadow: 0 4px 20px rgba(56,189,248,.25) !important;
  transition: all .25s ease !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 30px rgba(56,189,248,.45) !important;
}

[data-testid="stSidebar"] {
  background: #080f1e !important;
  border-right: 1px solid #1e3a5f;
}

hr { border-color: #1e3a5f !important; }
</style>
""", unsafe_allow_html=True)

# ─── Chemins des fichiers ─────────────────────────────────────────────────────
MODELS_DIR        = "models"
RF_MODEL_PATH     = os.path.join(MODELS_DIR, "random_forest_model.joblib")
SVM_MODEL_PATH    = os.path.join(MODELS_DIR, "svm_model.joblib")
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, "preprocessor.joblib")
TEST_DATA_PATH    = os.path.join(MODELS_DIR, "test_data.joblib")
METRICS_PATH      = os.path.join(MODELS_DIR, "metrics.joblib")

TRAIN_FILE = "KDDTrain+.txt"
TEST_FILE  = "KDDTest+.txt"

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


# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================

@st.cache_resource(show_spinner=False)
def charger_modeles():
    """Charge les modèles ML et le préprocesseur (mis en cache Streamlit)."""
    try:
        rf_model     = joblib.load(RF_MODEL_PATH)
        svm_model    = joblib.load(SVM_MODEL_PATH)
        preprocessor = joblib.load(PREPROCESSOR_PATH)
        metrics      = joblib.load(METRICS_PATH) if os.path.exists(METRICS_PATH) else {}
        return rf_model, svm_model, preprocessor, metrics, True
    except Exception as e:
        return None, None, None, {}, False


@st.cache_data(show_spinner=False)
def charger_dataset():
    """Charge le dataset NSL-KDD pour les statistiques globales."""
    try:
        dfs = []
        for fname in [TRAIN_FILE, TEST_FILE]:
            if os.path.exists(fname):
                dfs.append(pd.read_csv(fname, header=None, names=NSL_KDD_COLUMNS))
        if not dfs:
            return None
        df = pd.concat(dfs, ignore_index=True)
        df.drop(columns=["difficulty_level"], inplace=True, errors="ignore")
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        df["binary_label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)
        return df
    except:
        return None


def predire(raw_input: dict, rf_model, svm_model, preprocessor, use_model="rf"):
    """
    Applique le prétraitement IDENTIQUE à l'entraînement
    puis retourne (pred_label, confidence).
    """
    df_point = pd.DataFrame([raw_input])
    for col in ["label", "binary_label", "difficulty_level"]:
        df_point.drop(columns=[col], inplace=True, errors="ignore")

    X_proc = preprocessor.transform(df_point)

    if use_model == "rf":
        pred  = rf_model.predict(X_proc)[0]
        proba = rf_model.predict_proba(X_proc)[0]
        conf  = float(proba[pred])
    else:
        pred  = svm_model.predict(X_proc)[0]
        proba = svm_model.predict_proba(X_proc)[0]
        conf  = float(proba[pred])

    return int(pred), conf


# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:20px 0 24px;">
      <div style="font-size:3rem;">🛡️</div>
      <div style="font-family:'IBM Plex Mono',monospace;color:#38bdf8;
                  font-size:.95rem;font-weight:700;margin-top:8px;">SOC INTELLIGENT</div>
      <div style="font-size:.72rem;color:#475569;margin-top:4px;">
        Random Forest + SVM • NSL-KDD
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**🔌 Statut des composants**")

    checks = [
        ("Random Forest",  os.path.exists(RF_MODEL_PATH)),
        ("SVM",            os.path.exists(SVM_MODEL_PATH)),
        ("Préprocesseur",  os.path.exists(PREPROCESSOR_PATH)),
        ("Dataset",        os.path.exists(TRAIN_FILE) or os.path.exists(TEST_FILE)),
    ]
    for name, ok in checks:
        badge = f'<span class="badge-on">● EN LIGNE</span>' if ok \
                else f'<span class="badge-off">● ABSENT</span>'
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;"
            f"align-items:center;margin:7px 0;font-size:.85rem;'>"
            f"{name}{badge}</div>", unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("**⚙️ Modèle de prédiction**")
    model_choice = st.radio(
        "Sélectionnez un modèle",
        ["🌲 Random Forest", "⚡ SVM (RBF)"],
        help="Le modèle utilisé pour la prédiction en temps réel."
    )
    model_key = "rf" if "Random" in model_choice else "svm"

    st.markdown("---")
    st.markdown("""
    <div style="font-size:.75rem;color:#475569;line-height:1.8;">
      <b style="color:#94a3b8;">💡 Pour démarrer :</b><br>
      1. <code>pip install -r requirements.txt</code><br>
      2. <code>python main.py</code><br>
      3. Rechargez cette page
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# EN-TÊTE
# =============================================================================

st.markdown("""
<div style="padding:20px 0 12px;">
  <h1 style="margin:0;font-size:1.9rem;">🛡️ SOC Intelligent — Tableau de Bord IDS</h1>
  <p style="color:#475569;margin:6px 0 0;font-size:.88rem;">
    Système de Détection d'Intrusions • Random Forest + SVM • Dataset NSL-KDD
  </p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ─── Chargement ──────────────────────────────────────────────────────────────
rf_model, svm_model, preprocessor, saved_metrics, models_loaded = charger_modeles()
df = charger_dataset()


# =============================================================================
# SECTION 1 : VUE D'ENSEMBLE
# =============================================================================

st.markdown('<div class="sec-hdr">◈ 01 — Vue d\'ensemble du Système</div>',
            unsafe_allow_html=True)

if df is not None:
    total   = len(df)
    n_norm  = int((df["binary_label"] == 0).sum())
    n_att   = int((df["binary_label"] == 1).sum())
    n_types = int(df[df["binary_label"] == 1]["label"].nunique())
    att_pct = n_att / total * 100

    # KPI cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="kpi-card blue">
          <div class="kpi-label">Total Événements</div>
          <div class="kpi-num kpi-blue">{total:,}</div>
          <div class="kpi-sub">Dataset complet NSL-KDD</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="kpi-card green">
          <div class="kpi-label">Trafic Normal</div>
          <div class="kpi-num kpi-green">{n_norm:,}</div>
          <div class="kpi-sub">{100-att_pct:.1f}% du total</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="kpi-card red">
          <div class="kpi-label">Attaques</div>
          <div class="kpi-num kpi-red">{n_att:,}</div>
          <div class="kpi-sub">{att_pct:.1f}% du total</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="kpi-card amber">
          <div class="kpi-label">Types d'Attaques</div>
          <div class="kpi-num kpi-amber">{n_types}</div>
          <div class="kpi-sub">catégories distinctes</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Graphiques ligne 1
    g1, g2 = st.columns([1, 2])

    PLOT_LAYOUT = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8", size=12),
        margin=dict(t=48, b=20, l=10, r=10),
    )

    with g1:
        fig = go.Figure(go.Pie(
            labels=["Normal", "Attaque"],
            values=[n_norm, n_att],
            hole=0.62,
            marker=dict(colors=["#34d399", "#f87171"],
                        line=dict(color="#070d1a", width=3)),
            textinfo="label+percent",
            textfont=dict(color="#c9d4e8", size=12),
            hovertemplate="<b>%{label}</b><br>%{value:,}<br>%{percent}<extra></extra>"
        ))
        fig.update_layout(
            **PLOT_LAYOUT,
            title=dict(text="Répartition Normal / Attaque",
                       font=dict(color="#818cf8", size=13), x=.5),
            showlegend=False, height=300,
            annotations=[dict(text=f"<b>{att_pct:.1f}%</b><br>attaques",
                              x=.5, y=.5, showarrow=False,
                              font=dict(size=14, color="#f87171"))]
        )
        st.plotly_chart(fig, use_container_width=True)

    with g2:
        top10 = df[df["binary_label"] == 1]["label"].value_counts().head(10).reset_index()
        top10.columns = ["Type", "Count"]
        fig = go.Figure(go.Bar(
            x=top10["Count"], y=top10["Type"], orientation="h",
            marker=dict(
                color=top10["Count"],
                colorscale=[[0,"#3b0606"],[.5,"#b91c1c"],[1,"#f87171"]],
            ),
            text=top10["Count"].apply(lambda x: f"{x:,}"),
            textposition="outside", textfont=dict(color="#fca5a5", size=11),
            hovertemplate="<b>%{y}</b><br>%{x:,}<extra></extra>"
        ))
        fig.update_layout(
            **PLOT_LAYOUT,
            title=dict(text="Top 10 Types d'Attaques",
                       font=dict(color="#818cf8", size=13), x=.5),
            xaxis=dict(showgrid=True, gridcolor="#1e3a5f", color="#475569"),
            yaxis=dict(showgrid=False, color="#94a3b8"),
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Graphiques ligne 2
    g3, g4 = st.columns(2)

    with g3:
        proto = df.groupby(["protocol_type","binary_label"]).size().reset_index(name="n")
        proto["Statut"] = proto["binary_label"].map({0:"Normal",1:"Attaque"})
        fig = px.bar(proto, x="protocol_type", y="n", color="Statut",
                     color_discrete_map={"Normal":"#34d399","Attaque":"#f87171"},
                     barmode="group",
                     title="Distribution par Protocole",
                     labels={"protocol_type":"Protocole","n":"Événements"})
        fig.update_layout(**PLOT_LAYOUT,
                          title_font=dict(color="#818cf8",size=13),
                          xaxis=dict(gridcolor="#1e3a5f"),
                          yaxis=dict(gridcolor="#1e3a5f"),
                          legend=dict(bgcolor="rgba(0,0,0,0)"),
                          height=280)
        st.plotly_chart(fig, use_container_width=True)

    with g4:
        top_flags = df["flag"].value_counts().head(6).index
        flag_df = df[df["flag"].isin(top_flags)].groupby(["flag","binary_label"]).size().reset_index(name="n")
        flag_df["Statut"] = flag_df["binary_label"].map({0:"Normal",1:"Attaque"})
        fig = px.bar(flag_df, x="flag", y="n", color="Statut",
                     color_discrete_map={"Normal":"#38bdf8","Attaque":"#fbbf24"},
                     barmode="stack", title="Distribution par Flag TCP",
                     labels={"flag":"Flag","n":"Événements"})
        fig.update_layout(**PLOT_LAYOUT,
                          title_font=dict(color="#818cf8",size=13),
                          xaxis=dict(gridcolor="#1e3a5f"),
                          yaxis=dict(gridcolor="#1e3a5f"),
                          legend=dict(bgcolor="rgba(0,0,0,0)"),
                          height=280)
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("⚠️ Dataset NSL-KDD introuvable. Lancez `python main.py` pour le télécharger.")


# =============================================================================
# SECTION 2 : PERFORMANCES DES MODÈLES ML
# =============================================================================

st.markdown("---")
st.markdown('<div class="sec-hdr">◈ 02 — Performances des Modèles ML</div>',
            unsafe_allow_html=True)

if saved_metrics and models_loaded:
    rf_m  = saved_metrics.get("Random Forest", {})
    svm_m = saved_metrics.get("SVM", {})

    p1, p2 = st.columns(2)
    for col, name, m, bar_cls, color in [
        (p1, "🌲 Random Forest", rf_m,  "metric-bar-rf",  "#38bdf8"),
        (p2, "⚡ SVM (RBF)",     svm_m, "metric-bar-svm", "#34d399"),
    ]:
        with col:
            st.markdown(f"**{name}**")
            for metric_key, label in [
                ("accuracy","Accuracy"), ("precision","Precision"),
                ("recall","Recall"), ("f1","F1-Score")
            ]:
                val = m.get(metric_key, 0)
                pct = val * 100
                st.markdown(f"""
                <div style="margin:10px 0;">
                  <div style="display:flex;justify-content:space-between;
                              font-size:.82rem;margin-bottom:3px;">
                    <span style="color:#94a3b8;">{label}</span>
                    <span style="color:{color};font-family:'IBM Plex Mono',monospace;
                                 font-weight:600;">{pct:.2f}%</span>
                  </div>
                  <div class="metric-bar-wrap">
                    <div class="{bar_cls}" style="width:{pct}%;"></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

    # Radar comparatif
    st.markdown("<br>", unsafe_allow_html=True)
    categories = ["Accuracy", "Precision", "Recall", "F1-Score"]
    rf_vals  = [rf_m.get(k,0) for k in ["accuracy","precision","recall","f1"]]
    svm_vals = [svm_m.get(k,0) for k in ["accuracy","precision","recall","f1"]]

    fig_radar = go.Figure()
    for vals, name, color in [
        (rf_vals,  "Random Forest", "#38bdf8"),
        (svm_vals, "SVM (RBF)",     "#34d399"),
    ]:
        if color.startswith("#") and len(color) == 7:
            rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
            fillcolor = f"rgba({rgb[0]},{rgb[1]},{rgb[2]},0.12)"
        elif color.startswith("rgb("):
            fillcolor = color.replace("rgb(", "rgba(").replace(")", ",0.12)")
        else:
            fillcolor = color

        fig_radar.add_trace(go.Scatterpolar(
            r=vals + [vals[0]], theta=categories + [categories[0]],
            fill="toself", name=name,
            line=dict(color=color, width=2),
            fillcolor=fillcolor,
            marker=dict(color=color, size=6)
        ))
    fig_radar.update_layout(
        **PLOT_LAYOUT,
        polar=dict(
            bgcolor="#0f1d35",
            radialaxis=dict(visible=True, range=[0,1], color="#475569",
                            gridcolor="#1e3a5f", tickformat=".0%"),
            angularaxis=dict(color="#94a3b8", gridcolor="#1e3a5f")
        ),
        title=dict(text="Comparaison Radar des Modèles ML",
                   font=dict(color="#818cf8", size=14), x=.5),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#94a3b8")),
        height=380
    )
    st.plotly_chart(fig_radar, use_container_width=True)

else:
    st.info("ℹ️ Entraînez les modèles avec `python main.py` pour voir leurs performances.")


# =============================================================================
# SECTION 3 : SIMULATION DE DÉTECTION EN TEMPS RÉEL
# =============================================================================

st.markdown("---")
st.markdown('<div class="sec-hdr">◈ 03 — Simulation de Détection en Temps Réel</div>',
            unsafe_allow_html=True)

if not models_loaded:
    st.error("🔴 Modèles non chargés. Lancez d'abord : `python main.py`")
else:
    active_model_label = "🌲 Random Forest" if model_key == "rf" else "⚡ SVM (RBF)"
    st.markdown(f"""<div class="info-box">
      <span style="color:#38bdf8;font-family:'IBM Plex Mono',monospace;font-size:.82rem;">
        MODÈLE ACTIF : {active_model_label} — Renseignez les features et cliquez sur Analyser.
      </span>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Formulaire (7 features représentatives) ──────────────────────────────
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**📡 Connexion réseau**")
        duration = st.number_input("Durée de connexion (s)",
                                   min_value=0, max_value=60000, value=0)
        protocol_type = st.selectbox("Type de protocole", ["tcp","udp","icmp"])
        service = st.selectbox("Service", [
            "http","ftp","ssh","smtp","dns","telnet",
            "ftp_data","finger","pop_3","imap4",
            "private","ecr_i","urp_i","other"
        ])

    with col2:
        st.markdown("**📊 Volume de données**")
        src_bytes = st.number_input("Octets src → dst",
                                    min_value=0, max_value=10_000_000, value=181)
        dst_bytes = st.number_input("Octets dst → src",
                                    min_value=0, max_value=10_000_000, value=5450)
        flag = st.selectbox("Flag TCP", [
            "SF","S0","REJ","RSTO","SH","S1","S2","RSTOS0","S3","OTH","RSTR"
        ])

    with col3:
        st.markdown("**🔐 Comportement & Sécurité**")
        logged_in = st.selectbox("Connexion réussie", [0, 1],
                                 format_func=lambda x: "✅ Oui" if x else "❌ Non")
        num_failed_logins = st.number_input("Tentatives login échouées",
                                            min_value=0, max_value=10, value=0)
        serror_rate = st.slider("Taux d'erreur SYN", 0.0, 1.0, 0.0, 0.01,
                                help="Proportion de connexions avec erreur SYN (0–1)")

    # Valeurs par défaut pour les 34 features non affichées
    # (valeurs médianes/modes typiques du dataset NSL-KDD)
    raw_input = {
        "duration": duration,
        "protocol_type": protocol_type,
        "service": service,
        "flag": flag,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "land": 0,
        "wrong_fragment": 0,
        "urgent": 0,
        "hot": 0,
        "num_failed_logins": num_failed_logins,
        "logged_in": logged_in,
        "num_compromised": 0,
        "root_shell": 0,
        "su_attempted": 0,
        "num_root": 0,
        "num_file_creations": 0,
        "num_shells": 0,
        "num_access_files": 0,
        "num_outbound_cmds": 0,
        "is_host_login": 0,
        "is_guest_login": 0,
        "count": 1,
        "srv_count": 1,
        "serror_rate": serror_rate,
        "srv_serror_rate": serror_rate,
        "rerror_rate": 0.0,
        "srv_rerror_rate": 0.0,
        "same_srv_rate": 1.0,
        "diff_srv_rate": 0.0,
        "srv_diff_host_rate": 0.0,
        "dst_host_count": 255,
        "dst_host_srv_count": 255,
        "dst_host_same_srv_rate": 1.0,
        "dst_host_diff_srv_rate": 0.0,
        "dst_host_same_src_port_rate": 0.0,
        "dst_host_srv_diff_host_rate": 0.0,
        "dst_host_serror_rate": 0.0,
        "dst_host_srv_serror_rate": 0.0,
        "dst_host_rerror_rate": 0.0,
        "dst_host_srv_rerror_rate": 0.0,
    }

    st.markdown("<br>", unsafe_allow_html=True)

    # Bouton centré
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        analyze = st.button("⚡ ANALYSER L'ÉVÉNEMENT", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Résultat ──────────────────────────────────────────────────────────────
    if analyze:
        with st.spinner("🔍 Analyse en cours..."):
            try:
                pred_label, confidence = predire(
                    raw_input, rf_model, svm_model, preprocessor, model_key
                )
                is_normal = (pred_label == 0)
                conf_pct  = confidence * 100

                if is_normal:
                    st.markdown(f"""
                    <div class="alert-normal">
                      <div style="font-size:3.5rem;">✅</div>
                      <div class="status-txt-normal">TRAFIC NORMAL</div>
                      <div style="color:#6ee7b7;margin-top:8px;font-size:.9rem;">
                        Aucune menace détectée — Activité réseau conforme
                      </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="alert-attack">
                      <div style="font-size:3.5rem;">🚨</div>
                      <div class="status-txt-attack">ATTAQUE DÉTECTÉE !</div>
                      <div style="color:#fca5a5;margin-top:8px;font-size:.9rem;">
                        Comportement malveillant identifié — Alerte de sécurité émise
                      </div>
                    </div>""", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # Détails de la prédiction
                d1, d2 = st.columns(2)
                bar_color = "#34d399" if is_normal else "#f87171"
                bar_label = "Confiance — Normal" if is_normal else "Confiance — Attaque"
                bar_class = "metric-bar-rf" if is_normal else "metric-bar-svm"

                with d1:
                    st.markdown(f"""<div class="info-box">
                      <div style="font-size:.75rem;color:#475569;
                                  font-family:'IBM Plex Mono',monospace;margin-bottom:6px;">
                        {bar_label}
                      </div>
                      <div style="font-size:2rem;font-family:'IBM Plex Mono',monospace;
                                  color:{bar_color};font-weight:700;">
                        {conf_pct:.1f}%
                      </div>
                      <div class="metric-bar-wrap" style="margin-top:8px;">
                        <div class="{bar_class}" style="width:{conf_pct}%;"></div>
                      </div>
                    </div>""", unsafe_allow_html=True)

                with d2:
                    st.markdown(f"""<div class="info-box">
                      <div style="font-size:.75rem;color:#475569;
                                  font-family:'IBM Plex Mono',monospace;margin-bottom:10px;">
                        Détails de l'analyse
                      </div>
                      <div style="font-size:.85rem;line-height:2;">
                        <span style="color:#475569;">Modèle :</span>
                        <span style="color:#38bdf8;">{active_model_label}</span><br>
                        <span style="color:#475569;">Protocole :</span>
                        <span style="color:#c9d4e8;">{protocol_type.upper()}</span><br>
                        <span style="color:#475569;">Service :</span>
                        <span style="color:#c9d4e8;">{service}</span><br>
                        <span style="color:#475569;">Flag TCP :</span>
                        <span style="color:#c9d4e8;">{flag}</span><br>
                        <span style="color:#475569;">Src Bytes :</span>
                        <span style="color:#c9d4e8;">{src_bytes:,}</span>
                      </div>
                    </div>""", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Erreur de prédiction : {e}")
                st.info("Vérifiez que les modèles ont bien été entraînés (`python main.py`).")

    # ── Cas pré-définis ───────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("**🧪 Exemples NSL-KDD typiques — test rapide**")
    ex1, ex2, ex3 = st.columns(3)

    BASE = {k: 0 for k in raw_input}
    BASE.update({
        "count":1,"srv_count":1,"same_srv_rate":1.0,
        "dst_host_count":255,"dst_host_srv_count":255,"dst_host_same_srv_rate":1.0,
    })

    def run_example(features, label, col):
        with col:
            if st.button(f"▶ {label}", key=f"ex_{label}"):
                try:
                    p, c = predire(features, rf_model, svm_model, preprocessor, model_key)
                    is_n = (p == 0)
                    color  = "#34d399" if is_n else "#f87171"
                    icon   = "✅" if is_n else "🚨"
                    result = "NORMAL" if is_n else "ATTAQUE"
                    st.markdown(f"""
                    <div style="background:#0f1d35;border:2px solid {color};
                                border-radius:10px;padding:14px;text-align:center;
                                margin-top:8px;">
                      <div style="font-size:1.6rem;">{icon}</div>
                      <div style="font-family:'IBM Plex Mono',monospace;
                                  color:{color};font-weight:700;">{result}</div>
                      <div style="color:#475569;font-size:.75rem;">{c*100:.1f}% confiance</div>
                    </div>""", unsafe_allow_html=True)
                except:
                    st.warning("Modèle non disponible.")

    # HTTP normal
    ex_http = {**BASE, "duration":0,"protocol_type":"tcp","service":"http",
               "flag":"SF","src_bytes":232,"dst_bytes":8153,"logged_in":1}
    # DoS SYN Flood
    ex_dos  = {**BASE, "duration":0,"protocol_type":"tcp","service":"private",
               "flag":"S0","src_bytes":0,"dst_bytes":0,"logged_in":0,
               "serror_rate":1.0,"srv_serror_rate":1.0,"count":511,"srv_count":511}
    # Brute Force FTP
    ex_bf   = {**BASE, "duration":1,"protocol_type":"tcp","service":"ftp",
               "flag":"SF","src_bytes":0,"dst_bytes":0,"logged_in":0,"num_failed_logins":5}

    with ex1:
        st.markdown("<div style='text-align:center;color:#475569;font-size:.78rem;margin-bottom:6px;'>HTTP Normal</div>",
                    unsafe_allow_html=True)
    with ex2:
        st.markdown("<div style='text-align:center;color:#475569;font-size:.78rem;margin-bottom:6px;'>DoS SYN Flood</div>",
                    unsafe_allow_html=True)
    with ex3:
        st.markdown("<div style='text-align:center;color:#475569;font-size:.78rem;margin-bottom:6px;'>Brute Force FTP</div>",
                    unsafe_allow_html=True)

    run_example(ex_http, "HTTP Normal",       ex1)
    run_example(ex_dos,  "DoS SYN Flood",     ex2)
    run_example(ex_bf,   "Brute Force FTP",   ex3)


# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:14px 0;
            font-family:'IBM Plex Mono',monospace;font-size:.7rem;color:#1e3a5f;">
  SOC INTELLIGENT • MACHINE LEARNING IDS • NSL-KDD DATASET<br>
  <span style="color:#1e3a5f;">
    Random Forest (scikit-learn) + SVM RBF Kernel (scikit-learn)
  </span>
</div>
""", unsafe_allow_html=True)
