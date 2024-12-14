from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
#from .forms import SearchForm #change here

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

# added view definition to handle the search - testing with strip
def search(request):
    query = request.GET.get('q', '').strip()
    title = request.GET.get('title', '').strip()
    author = request.GET.get('author', '').strip()
    affiliation = request.GET.get('affiliation', '').strip()
    date = request.GET.get('date', '').strip()

    posts = Post.objects.all()

    # Ensure we reset results for an empty query - testing for error in search
    if not query and not title and not author and not affiliation and not date:
       return render(request, 'posts/search_results.html', {'query': '', 'posts': []})
    
    if query:
        posts = posts.filter(Q(keywords__icontains=query) | Q(subject__icontains=query))
    if title: #got rid of the &= and Q
        posts = posts.filter(Q(title__icontains=title))
    if author:
        posts = posts.filter(Q(authors__icontains=author))
    if affiliation:
        posts = posts.filter(Q(affiliation__icontains=affiliation))
    if date:
        posts = posts.filter(Q(date=date))

    return render(request, 'posts/search_results.html', {
        'query': query,
        'title': title,
        'author': author,
        'affiliation': affiliation,
        'date': date,
        'posts': posts
    })
  