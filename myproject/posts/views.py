from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    post = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': post})
