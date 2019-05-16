from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta : 
        model = Post
        fields = ('title', 'contents', 'price', 'star_rate', 'picture')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widget= {
            'password' : forms.PasswordInput()
        }