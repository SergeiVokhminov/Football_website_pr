from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "publication_sign")
    list_filter = ("publication_sign",)
    search_fields = ("title", "article")
