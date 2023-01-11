from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.mail import send_mail
from .models import Post, Category, Contact_Details, Album
from .forms import ContactForm, PostForm
import random


# Create your views here.
def home(request):
    posts = Post.objects.all()
    menu_categories = Category.objects.all()
    rand_post = random.choice(posts)
    template = loader.get_template('home.html')
    culture_posts = posts.filter(categories__slug='culture')
    business_posts = posts.filter(categories__slug='business')
    lifestyle_posts = posts.filter(categories__slug='lifestyle')

    if request.method == "POST":
        form = MyFormClass(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()

    context = {
        'posts': posts,
        'menu_categories': menu_categories,
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


def single_post_view(request, slug):
    print("Single Post")
    single_post = get_object_or_404(Post, slug=slug)
    posts = Post.objects.all()
    post_popular = posts.filter(tags__name__in=['popular'])
    post_trending = posts.filter(tags__name__in=['trending'])
    post_latest = posts.order_by('-pub_date')
    context = {
        'post': single_post,
        'post_popular': post_popular,
        'post_trending': post_trending,
        'post_latest': post_latest,
    }
    return render(request, 'single_post.html', context)

def category_view(request, category_slug):
    print("Category")
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'category.html', {'category': category})

def contact_view(request):
    form = ContactForm()

    if form.is_valid():
        name = form.cleaned_data['name']
        sender = form.cleaned_data['sender']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['info@example.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(name, sender, subject, message, recipients)
        return HttpResponseRedirect('/thanks/')

    rendered_form = form.render('contact.html')
    context = {
        'form': rendered_form,
    }
    return render(request, 'contact.html', context)

def album_detail(request, album_slug):
    print("Album")
    album_detail = get_object_or_404(Album, slug=album_slug)
    return render(request, 'album_detail.html', {'album': album_detail})









