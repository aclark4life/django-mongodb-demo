# Via GenAI-Showcase
# 
# https://github.com/mongodb-developer/GenAI-Showcase
#
# Dublin City Center Pub Finder
# 
# https://github.com/mongodb-developer/GenAI-Showcase/blob/bda943ce45b3c702cf2bb86c093bb3ae6925bfcf/apps/django_langchain_voyageai/finder/dublinfinder/models.py

from django.db import models
from django_mongodb_backend.fields import ArrayField, EmbeddedModelField
from django_mongodb_backend.managers import MongoManager
from django_mongodb_backend.models import EmbeddedModel


# Embedded, so it doesn't have it's own collection.
class DisplayName(EmbeddedModel):
    text = models.CharField(max_length=200)
    languageCode = models.CharField(max_length=10, blank=True, null=True)


# Main model is our Places.
class Place(models.Model):
    types = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    formattedAddress = models.CharField(max_length=300, blank=True, null=True)
    displayName = EmbeddedModelField(DisplayName, blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    # This is where our embedding will go when generated.
    embedding = ArrayField(models.FloatField(), blank=True, null=True)

    objects = MongoManager()

    class Meta:
        db_table = "places"
        managed = False

    def __str__(self):
        return self.displayName.text
