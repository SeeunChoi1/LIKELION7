from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = ('title', 'contents', 'price', 'star_rate')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)