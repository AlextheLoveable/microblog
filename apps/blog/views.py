from django.shortcuts import render, redirect

from .models import Blog

# Create your views here.
def index(request):
    context = {
        "messages": Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)

def user(request):
    if request.method == "POST":
        request.session['username'] = request.POST['username']
        return render(request, 'blog/post.html')

def createmessage(request):
    return render(request,'blog/post.html')
