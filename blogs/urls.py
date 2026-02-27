from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView

app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
