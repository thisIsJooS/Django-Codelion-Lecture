"""Blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('formcreate/', views.formcreate, name='formcreate'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('detail/<int:post_id>/', views.detail, name="detail"),
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),
    path('login', accounts_views.login, name='login'),
    path('logout', accounts_views.logout, name='logout'),
    path('signup', accounts_views.signup, name='signup'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)