from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts' : posts })

@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.get_username()
            post.save()
        else:
            print(form, form.is_valid())
        return redirect('detail', post.pk)
    else:
        form = PostForm()
        return render(request, 'new.html', {'form' : form})


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    # return render(request, 'detail.html', { 'post' : post })

    if request.method == "POST":
        # post=Post.objects.get(pk = post_pk)
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user.get_username()
        comment.post = post
        comment.save()
        return redirect('detail', post_pk)
    else:
        # post = Post.objects.get(pk = post_pk)
        form = CommentForm()
        return render(request, 'detail.html', { 'post':post, 'form':form })
        #render -> html

@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    #해당 comment 찾기
    comment.delete()
    #찾은 comment 지워라
    return redirect('detail', post_pk)
    #redirect -> url

@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post_pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', { 'form' : form })

@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        error = "아이디가 이미 존재합니다"
        return render(request, 'registration/signup.html', {'form':form}, {'error': error})