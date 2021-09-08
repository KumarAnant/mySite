from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, 'blog/welcome.html')

def posts(request, posts):
    return render(request, 'blog/posts.html', {
        'posts': posts
    })

def postDetail(request, postdetail):
    return render(request, 'blog/postdetail.html', {
        'postDetail': postDetail
    })