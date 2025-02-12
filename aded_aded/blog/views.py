from django.shortcuts import render, get_object_or_404
from .models import NewsArticle  # Importing class from models file
from django.contrib.auth.decorators import login_required

@login_required
def user_login(request):
    """
    Render the login page for users.
    
    :param request: The HTTP request object.
    :return: Rendered login template.
    """
    return render(request, 'blog/login.html')

def home(request):
    """
    Render the home page.
    
    :param request: The HTTP request object.
    :return: Rendered home template.
    """
    return render(request, 'blog/home.html')

@login_required
def about(request):
    """
    Render the about page.
    
    :param request: The HTTP request object.
    :return: Rendered about template.
    """
    return render(request, 'blog/about.html')

@login_required
def news(request):
    """
    Display a list of news articles.
    
    :param request: The HTTP request object.
    :return: Rendered news template with a list of articles.
    """
    articles = NewsArticle.objects.all()
    return render(request, 'blog/news.html', {'articles': articles})

def blog_list(request):
    """
    Display a list of blog posts.
    
    :param request: The HTTP request object.
    :return: Rendered post template with a list of posts.
    """
    posts = NewsArticle.objects.all()  # Fetching all posts from the database
    return render(request, 'blog/post.html', {'posts': posts})

def blog_detail(request, post_id):
    """
    Display details of a specific blog post.
    
    :param request: The HTTP request object.
    :param post_id: The ID of the blog post to retrieve.
    :return: Rendered post template with the specific blog post.
    """
    one_post = get_object_or_404(NewsArticle, id=post_id)  # Fetch specific post
    print(one_post)
    return render(request, 'blog/post.html', {'one_post': one_post})
