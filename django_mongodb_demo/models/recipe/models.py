from django.db import models
from django.db.models import Q, F
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField
from django_mongodb_backend.indexes import SearchIndex, VectorSearchIndex

class Nutrition(EmbeddedModel):
    calories = models.IntegerField(default=0)
    carb_grams = models.IntegerField(default=0)
    protein_grams = models.IntegerField(default=0)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200)
    cook_time = models.IntegerField(default=0)
    allergens = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    ratings = ArrayField(models.IntegerField(default=0), size=10)
    nutrition = EmbeddedModelField(Nutrition, null=True, blank=True)

    class Meta:
        db_table = "recipes"

    def __str__(self):
        return self.title
