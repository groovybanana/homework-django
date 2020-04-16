import requests
from django.http import HttpResponse
from django.shortcuts import render

nav = [
    {
        'title': 'Home',
        'path': '/',
        'active': 'active',
    },
    {
        'title': 'About',
        'path': '/about',
        'active': 'active',
    },
    {
        'title': 'Blog',
        'path': '/blog',
        'active': 'active',
    },
    {
        'title': 'Contact',
        'path': '/contact',
        'active': 'active',
    },
    {
        'title': 'Portfolio',
        'path': '/portfolio',
        'active': 'active',
    },
    {
        'title': 'GitHub',
        'active': 'active',
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




# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://api.github.com/users/kickstartcoding/repos')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)

    # return HttpResponse('''
    #     <h1>Welcome to my home page!</h1>
    #     <a href="/about-me">About me</a> <br />
    #     <a href="/github-api-example">See my GitHub contributions</a> <br />
    # ''')


# def about_me(request):
#     # Django comes with a "shortcut" function called "render", that
#     # lets us read in HTML template files in separate directories to
#     # keep our code better organized.
#     context = {
#         'name': 'Ash Ketchum',
#         'pokemon': 'Pikachu',
#     }
#     return render(request, 'about_me.html', context)
