from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post

def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')[:5]  # Get the last 5 posts

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'account/profile.html', context)