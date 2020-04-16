import requests
from django.http import HttpResponse
from django.shortcuts import render

nav = [
    {
        'title': 'Home',
        'path': '/',
    },
    {
        'title': 'About',
        'path': '/about',
    },
    {
        'title': 'Blog',
        'path': '/blog',
    },
    {
        'title': 'Contact',
        'path': '/contact',
    },
    {
        'title': 'Portfolio',
        'path': '/portfolio',
    },
    {
        'title': 'GitHub',
        'path': '/github',
    },
]

def index(request):
    context = {
        'page_title': 'Home',
        'nav': nav,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'page_title': 'About Me',
        'nav': nav,
    }
    return render(request, 'about.html', context)

def blog(request):
    context = {
        'page_title': 'Blog',
        'nav': nav,
    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        'page_title': 'Contact Me',
        'nav': nav,
    }
    return render(request, 'contact.html', context)

def portfolio(request):
    context = {
        'page_title': 'Portfolio',
        'nav': nav,
    }
    return render(request, 'portfolio.html', context)

def github_api(request):
    '''Get my github repos'''
    response = requests.get('https://api.github.com/users/groovybanana/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
        'page_title': 'GitHub',
        'nav': nav,
    }
    return render(request, 'github.html', context)
