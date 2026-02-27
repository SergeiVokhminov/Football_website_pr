from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(publication_sign=True)


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # fields = ("title", "article", "image", "publication_sign")
    success_url = reverse_lazy("blogs:blog_list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # fields = ("title", "article", "image", "publication_sign")
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
