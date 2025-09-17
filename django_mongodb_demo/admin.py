from django.contrib import admin
from .models import Author, Article, Comment

from .models.polls.admin import QuestionAdmin, PollAdmin, ChoiceAdmin  # noqa: F401
# from .sample_mflix.admin import MovieAdmin, ActorAdmin, CommentAdmin, UserAdmin  # noqa: F401  
from .models.sample_mflix.admin import MovieAdmin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    search_fields = ("title", "content")


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("article", "user_name", "created_at")
