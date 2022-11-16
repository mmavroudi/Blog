from django.shortcuts import render, get_object_or_404
from .models import Post
import random


# Create your views here.
def home(request):
    print('Hello ')
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})


def post_detail_view(request):
    print(request)
    posts = Post.objects
    template = "post_detail_view.html"
    context = {}
    return render(request, template, {'posts': posts}, context)


def random_post(request):
    posts = Post.objects.all()
    rand_post = random.choice(posts)
    content_post = Post.content

    print(rand_post)
    template = "random_post_view.html"
    context = {
        'posts': posts,
        'rand_post': rand_post,
        'content_post': content_post
    }
    return render(request, template, context)


def single_post_view(request, post_id):
    print("Single Post")
    single_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'single_post.html', {'post': single_post})




