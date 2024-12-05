from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello DJango")

def say_hi(request):
    return render(request, 'hi.html', {'name' : 'John Samuel Jamandron'})

def blog_list(request):
    posts = Post.objects.all()  # Fetch all posts
    context = {
        'blog_list': posts
    }
    return render(request, 'blog_list.html', context)

def blog_details(request, id):
    # Get the specific post by ID
    each_post = Post.objects.get(id=id)

    context = {
        'blog_detail': each_post
    }
    return render(request, 'blog_details.html', context)