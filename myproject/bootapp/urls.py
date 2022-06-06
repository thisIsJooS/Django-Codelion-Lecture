from django.urls import path
from bootapp import views

urlpatterns = [
    path('', views.boot, name='home'),
    path('about/', views.about, name='about'),
]
