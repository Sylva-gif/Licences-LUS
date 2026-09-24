"""TP Django autonome : route et ORM en mémoire, aucun serveur exposé."""

from django.conf import settings

settings.configure(
    SECRET_KEY="cle-locale-ephemere-de-test-non-utilisable-en-production",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["testserver"],
    INSTALLED_APPS=[],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
)
import django

django.setup()
from django.db import models, connection, IntegrityError, transaction
from django.http import JsonResponse
from django.urls import path
from django.test import Client


class Animal(models.Model):
    identifiant = models.CharField(max_length=60, unique=True)
    espece = models.CharField(max_length=60)

    class Meta:
        app_label = "suivi"


def etat(request):
    return JsonResponse({"status": "ok", "animaux": Animal.objects.count()})


urlpatterns = [path("etat/", etat)]

if __name__ == "__main__":
    try:
        with connection.schema_editor() as schema:
            schema.create_model(Animal)
        Animal.objects.create(identifiant="A", espece="Bovin")
        response = Client().get("/etat/")
        assert response.status_code == 200 and response.json()["animaux"] == 1
        try:
            with transaction.atomic():
                Animal.objects.create(identifiant="A", espece="Bovin")
        except IntegrityError:
            print("Django : doublon refusé par la base")
        else:
            raise AssertionError("Unicité non appliquée")
        print("Django : route JSON et ORM vérifiés")
    finally:
        connection.close()
