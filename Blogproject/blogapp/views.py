from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


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


# django form을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능한 함수
def formcreate(request):
    if request.method == 'GET':
        form = BlogForm()
    elif request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid(): # 폼 데이터를 자동으로 유효성 검사를 해줌
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    return render(request, 'form_create.html', {'form': form})
        
        
def modelformcreate(request):
    if request.method == 'GET':
        form = BlogModelForm()
    elif request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid(): # 폼 데이터를 자동으로 유효성 검사를 해줌
            form.save()
            return redirect('home')
    return render(request, 'form_create.html', {'form': form})