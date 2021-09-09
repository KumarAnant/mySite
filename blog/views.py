from django.shortcuts import render
from django.urls import reverse

# Create your views here.

post1Detail = {
    'title':    'qw-we-er',
    'details':  'sdjkhfsduk syfsfsopf oshfow yhfwhrif wiusyhithds'
}

post2Detail = {
    'title':    'as-sd-df',
    'details':  's;lkgp dipgdropi rt0w9sejfjwdfwe iu0w8spdokf we-38'
}

post3Detail = {
    'title':    'zx-xc-cv',
    'details':  'sdlkfj oeuroqwe[po oe9ru[opweruw39r8 lcaskcmosd'
}

allPosts    =   [post1Detail, post2Detail, post3Detail]
allTitles    =   [post1Detail['title'], post2Detail['title'], post3Detail['title']]


def welcome(request):
    return render(request, 'blog/welcome.html', {
        'allTitles': allTitles
    })

def posts(request):
    return render(request, 'blog/posts.html', {
        'allPosts': allPosts
    })

def postDetail(request, postTitle):
    toekn = False
    for post in allPosts:
        if post['title'] == postTitle:
            toekn = True
            break
        else:
            print('Post not found')
            token = False
    print(post)
    return render(request, 'blog/postdetails.html', {
        'post'      :   post,
        'postTitle' :   postTitle
    })