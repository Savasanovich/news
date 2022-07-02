from django.shortcuts import render
from .forms import *
from .services import get_news

# Create your views here.


def index(request):
    form = get_news
    ctx = {
        'form': form,
    }
    return render(request, 'index.html', ctx)


def about(request):

    forms = About
    ctx = {
        'forms': forms
     }

    return render(request, 'about.html', ctx)

def blog(request):

    return render(request, 'blog.html', {})

def category(request):

    return render(request, 'categori.html', {})

def contact(request):

    return render(request, 'contact.html', {})

def details(request):

    return render(request, 'details.html', {})

def elements(request):

    return render(request, 'elements.html', {})

def latest_news(request):

    return render(request, 'latest_news.html', {})

def main(request):

    return render(request, 'main.html', {})

def single_blog(request):

    return render(request, 'single-blog.html', {})
