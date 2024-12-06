from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget
# File: blog/forms.py

from taggit.forms import TagField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'placeholder': 'Add tags separated by commas',
            }),
        }
class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Allow adding tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
