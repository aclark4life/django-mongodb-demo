from djongo import models  
  
class Imdb(models.Model):  
    rating = models.FloatField()  
    votes = models.IntegerField()  
    id = models.IntegerField()  
  
    class Meta:  
        abstract = True  
  
  
class ViewerRating(models.Model):  
    rating = models.FloatField()  
    numReviews = models.IntegerField()  
    meter = models.IntegerField()  
  
    class Meta:  
        abstract = True  
  
  
class Tomatoes(models.Model):  
    viewer = models.EmbeddedField(  
        model_container=ViewerRating  
    )  
    fresh = models.IntegerField()  
    critic = models.JSONField()  # critic can be complex/nested  
    rotten = models.IntegerField()  
    lastUpdated = models.DateTimeField()  
  
    class Meta:  
        abstract = True  
  
  
class Movie(models.Model):  
    id = models.ObjectIdField()  
    title = models.CharField(max_length=255)  
    plot = models.TextField()  
    genres = models.ArrayField(model_container=models.CharField(max_length=50))  
    runtime = models.IntegerField()  
    cast = models.ArrayField(model_container=models.CharField(max_length=255))  
    num_mflix_comments = models.IntegerField()  
    countries = models.ArrayField(model_container=models.CharField(max_length=50))  
    released = models.DateTimeField()  
    directors = models.ArrayField(model_container=models.CharField(max_length=255))  
  
    rated = models.CharField(max_length=50, null=True, blank=True)  
    awards = models.JSONField()  
    lastupdated = models.CharField(max_length=50)  
    year = models.IntegerField()  
  
    imdb = models.EmbeddedField(  
        model_container=Imdb  
    )  
  
    tomatoes = models.EmbeddedField(  
        model_container=Tomatoes,  
        null=True,  
        blank=True  
    )  
  
    type = models.CharField(max_length=50, null=True, blank=True)  
  
    class Meta:  
        db_table = "movies"  
  
    def __str__(self):  
        return self.title  
  
  
class Comment(models.Model):  
    id = models.ObjectIdField()  
    name = models.CharField(max_length=255)  
    email = models.EmailField()  
    movie_id = models.ObjectIdField()  
    text = models.TextField()  
    date = models.DateTimeField()  
  
    class Meta:  
        db_table = "comments"  
  
    def __str__(self):  
        return f"{self.name} - {self.movie_id}"  
  
  
class User(models.Model):  
    id = models.ObjectIdField()  
    name = models.CharField(max_length=255)  
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=255)  
  
    class Meta:  
        db_table = "users"  
  
    def __str__(self):  
        return self.name  
  
  
class Location(models.Model):  
    address = models.JSONField()  
    geo = models.JSONField()  
  
    class Meta:  
        abstract = True  
  
  
class Theater(models.Model):  
    id = models.ObjectIdField()  
    theaterId = models.IntegerField()  
    location = models.EmbeddedField(  
        model_container=Location  
    )  
  
    class Meta:  
        db_table = "theaters"  
  
    def __str__(self):  
        return f"Theater {self.theaterId}"  
