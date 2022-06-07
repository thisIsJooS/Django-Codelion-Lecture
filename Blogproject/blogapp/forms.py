from django import forms
from .models import Blog

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__' # Model의 Blog 모델을 전부 입력받을 것이다
        fields = ['title', 'body']  # 특정 필드만 입력받고 싶을 때
        