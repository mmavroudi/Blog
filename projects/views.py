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


def room86(request):
    print(request)
    posts = Post.objects.all()
    featured_post = random_posts(posts)
    template = "room86.html"
    context = {
        'myposts': featured_post
    }
    return render(request, template, context)


def random_posts(request):
    """ we'll create here a sample functionality similar to what we want for room products using posts instead """
    import random
    posts = Post.objects.all()
    print(random.choice(posts))


