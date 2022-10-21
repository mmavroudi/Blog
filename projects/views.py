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
    import random
    print(request)
    posts = Post.objects.all()
    featured_post = random.choice(posts)
    template = "room86.html"
    context = {
        'myposts': posts,
        'randompost': featured_post
    }
    return render(request, template, context)





