from django.contrib import admin  
# from .models import Movie, Comment, User, Theater  
from .models import Movie
  
  
@admin.register(Movie)  
class MovieAdmin(admin.ModelAdmin):  
    pass
    # list_display = ("title", "year", "rated", "runtime", "lastupdated")  
    # search_fields = ("title", "plot", "cast", "directors")  
    # list_filter = ("year", "rated", "countries", "genres")  
    # ordering = ("-year",)  
    # date_hierarchy = "released"  
  
  
# @admin.register(Comment)  
# class CommentAdmin(admin.ModelAdmin):  
#     list_display = ("name", "movie_id", "date")  
#     search_fields = ("name", "email", "text")  
#     list_filter = ("date",)  
#     ordering = ("-date",)  
#   
#   
# @admin.register(User)  
# class UserAdmin(admin.ModelAdmin):  
#     list_display = ("name", "email")  
#     search_fields = ("name", "email")  
#     ordering = ("name",)  
#   
#   
# @admin.register(Theater)  
# class TheaterAdmin(admin.ModelAdmin):  
#     list_display = ("theaterId",)  
#     search_fields = ("theaterId", "location__address")  
