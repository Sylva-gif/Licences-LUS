# Atelier Django : une route puis un modèle

Ce TP crée un projet séparé dans votre répertoire d'exercices. Il ne modifie pas la base de l'application PyQt5. Utiliser Python 3.11/3.12 et un environnement virtuel dédié.

```bash
python -m pip install 'Django>=5.2,<5.3'
django-admin startproject portail
cd portail
python manage.py startapp suivi
```

Ajouter `suivi` à `INSTALLED_APPS` dans `portail/settings.py`. Remplacer `suivi/views.py` par :

```python
from django.http import JsonResponse

def etat(request):
    return JsonResponse({"service": "elevage-tp", "status": "ok"})
```

Dans `portail/urls.py`, ajouter l'import `from suivi.views import etat`, puis `path('etat/', etat)` à `urlpatterns`. Créer dans `suivi/models.py` :

```python
from django.db import models

class Animal(models.Model):
    identifiant = models.CharField(max_length=60, unique=True)
    espece = models.CharField(max_length=60)

    def __str__(self):
        return self.identifiant
```

Exécuter les migrations et démarrer uniquement en boucle locale :

```bash
python manage.py makemigrations suivi
python manage.py migrate
python manage.py check
python manage.py runserver 127.0.0.1:8000
```

Ouvrir `http://127.0.0.1:8000/etat/`. Ajouter ensuite un `TestCase` utilisant `self.client.get('/etat/')`. Extension : enregistrer le modèle dans l'administration, créer un compte local avec `createsuperuser` et comparer cette interface à PyQt5. `runserver` est un serveur de développement. Les secrets et comptes générés restent dans votre environnement, pas dans ce dépôt.
