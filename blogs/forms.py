from django import forms
from blogs.models import Blog


class BlogForm(forms.ModelForm):
    """Форма для представления блога."""

    class Meta:
        model = Blog
        exclude = ("created_at", "publication_sign", "views")

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
