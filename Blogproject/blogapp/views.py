from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    return render(request, 'index.html')

# 블로그 글 작성 
def new(request):
    return render(request, 'new.html')

# 블로그 글 저장
def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')