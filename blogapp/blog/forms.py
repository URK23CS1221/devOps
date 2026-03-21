from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for creating a new blog post."""

    class Meta:
        model = Post
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter post title...',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your name...',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Write your blog post here...',
                'rows': 10,
            }),
        }
