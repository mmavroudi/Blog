from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Category
import random


# Create your views here.
def home(request):
    posts = Post.objects.all()
    rand_post = random.choice(posts)
    template = loader.get_template('home.html')
    culture_posts = posts.objects.filter(categories="Culture")
    business_posts = posts.objects.filter(categories="Business")
    lifestyle_posts = posts.objects.filter(categories="Lifestyle")
    context = {
        'posts': posts,
        'rand_post': rand_post,
        'culture_posts': culture_posts,
        'business_posts': business_posts,
        'lifestyle_posts': lifestyle_posts,
    }
    return HttpResponse(template.render(context, request))

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

def category_view(request, category_slug):
    print("Category")
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'category.html', {'category': category})

#def about_view(request):
 #   template = "about.html"
 #   return render(request, template)




