from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def posts_list(request):
    cs_posts = Post.objects.filter(subject="CS")
    eng_posts = Post.objects.filter(subject="Eng")
    engl_posts = Post.objects.filter(subject="Engl")
    ds_posts = Post.objects.filter(subject="DS")
    math_posts = Post.objects.filter(subject="Math")

    return render(request, 'posts/posts_list.html', {
        'cs_posts': cs_posts,
        'eng_posts': eng_posts,
        'engl_posts': engl_posts, 
        'ds_posts': ds_posts,
        'math_posts': math_posts
    })


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })