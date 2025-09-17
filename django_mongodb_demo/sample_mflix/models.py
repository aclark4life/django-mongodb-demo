from django.db import models  
from django_mongodb_backend.fields import ObjectIdField, EmbeddedModelField, ArrayField
from django_mongodb_backend.models import EmbeddedModel
  
# class Imdb(models.Model):  
#     rating = models.FloatField()  
#     votes = models.IntegerField()  
#     id = ObjectIdField()
#   
#     class Meta:  
#         abstract = True  
#   
#   
# class ViewerRating(models.Model):  
#     rating = models.FloatField()  
#     numReviews = models.IntegerField()  
#     meter = models.IntegerField()  
#   
#     class Meta:  
#         abstract = True  
#   
#   
# class Tomatoes(models.Model):  
#     viewer = models.EmbeddedField(  
#         model_container=ViewerRating  
#     )  
#     fresh = models.IntegerField()  
#     critic = models.JSONField()  # critic can be complex/nested  
#     rotten = models.IntegerField()  
#     lastUpdated = models.DateTimeField()  
#   
#     class Meta:  
#         abstract = True  


class Award(EmbeddedModel):
    wins = models.IntegerField(default=0)
    nominations = models.IntegerField(default=0)
    text = models.CharField(max_length=100)
  
  
class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField(blank=True)
    runtime = models.IntegerField(default=0)
    released = models.DateTimeField("release date", null=True, blank=True)
    awards = EmbeddedModelField(Award, null=True, blank=True)
    genres = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    class Meta:
        db_table = "movies"
        managed = False
    def __str__(self):
        return self.title
  
  
# class Comment(models.Model):  
#     id = models.ObjectIdField()  
#     name = models.CharField(max_length=255)  
#     email = models.EmailField()  
#     movie_id = models.ObjectIdField()  
#     text = models.TextField()  
#     date = models.DateTimeField()  
#   
#     class Meta:  
#         db_table = "comments"  
#   
#     def __str__(self):  
#         return f"{self.name} - {self.movie_id}"  
#   
#   
# class User(models.Model):  
#     id = models.ObjectIdField()  
#     name = models.CharField(max_length=255)  
#     email = models.EmailField(unique=True)  
#     password = models.CharField(max_length=255)  
#   
#     class Meta:  
#         db_table = "users"  
#   
#     def __str__(self):  
#         return self.name  
#   
#   
# class Location(models.Model):  
#     address = models.JSONField()  
#     geo = models.JSONField()  
#   
#     class Meta:  
#         abstract = True  
#   
#   
# class Theater(models.Model):  
#     id = models.ObjectIdField()  
#     theaterId = models.IntegerField()  
#     location = models.EmbeddedField(  
#         model_container=Location  
#     )  
#   
#     class Meta:  
#         db_table = "theaters"  
#   
#     def __str__(self):  
#         return f"Theater {self.theaterId}"  
