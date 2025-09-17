from django.contrib import admin
from .models import Author, Article, Comment

from .models.polls.admin import QuestionAdmin, PollAdmin, ChoiceAdmin  # noqa: F401
# from .sample_mflix.admin import MovieAdmin, ActorAdmin, CommentAdmin, UserAdmin  # noqa: F401  
from .models.sample_mflix.admin import MovieAdmin
from .models.patient.admin import PatientAdmin, PatientRecordAdmin, BillingAdmin  # noqa: F401

from django.utils.html import format_html_join  
from django.utils.safestring import mark_safe  
  
  
@admin.register(Author)  
class AuthorAdmin(admin.ModelAdmin):  
    list_display = ("name", "email", "bio_snippet")  
    search_fields = ("name", "email", "bio")  
    ordering = ("name",)  
  
    def bio_snippet(self, obj):  
        return (obj.bio[:75] + "...") if len(obj.bio) > 75 else obj.bio  
    bio_snippet.short_description = "Bio"  
  
  
@admin.register(Article)  
class ArticleAdmin(admin.ModelAdmin):  
    list_display = (  
        "title",  
        "author",  
        "published_at",  
        "display_tags",  
    )  
    list_filter = ("published_at", "author")  
    search_fields = ("title", "content", "tags")  
    date_hierarchy = "published_at"  
    ordering = ("-published_at",)  
    autocomplete_fields = ("author",)  
  
    def display_tags(self, obj):  
        """Show tags as comma-separated values"""  
        return ", ".join(obj.tags)  
    display_tags.short_description = "Tags"  
  
  
@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):  
    list_display = ("short_text", "user_name", "article", "created_at")  
    list_filter = ("created_at", "article")  
    search_fields = ("user_name", "text", "article__title")  
    ordering = ("-created_at",)  
    autocomplete_fields = ("article",)  
  
    def short_text(self, obj):  
        return (obj.text[:50] + "...") if len(obj.text) > 50 else obj.text  
    short_text.short_description = "Comment"  

