from django import forms
from .models import Comment, Post

class PostCreateForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ("text",)

class CommentCreateForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ("comment",)
