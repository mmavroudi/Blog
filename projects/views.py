from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def post_detail_view(request):
    print(request)
    template = "post_detail_view.html"
    context = {}
    return render(request, template, context)


