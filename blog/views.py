from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def home(request):
    twoposts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/home.html', {'twoposts':twoposts})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/myblog.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def aboutme(request):
    return render(request, 'blog/aboutme.html')
