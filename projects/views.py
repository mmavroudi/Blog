from django.shortcuts import render
from .models import Post
import random


# Create your views here.
def home(request):
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

    print(rand_post)
    template = "random_post_view.html"
    context = {
        'posts': posts,
        'rand_post': rand_post
    }
    return render(request, template, context)





