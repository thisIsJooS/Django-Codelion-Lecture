from django.contrib import admin
from django.urls import path
from snsapp import views as snsappViews
from accounts import views as accountsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snsappViews.home, name='home'),
    path('postcreate/', snsappViews.postcreate, name='postcreate'),
    path('detail/<int:post_id>', snsappViews.detail, name='detail'),
    path('new_comment/<int:post_id>', snsappViews.new_comment, name='new_comment'),
    path('login/', accountsViews.login, name='login'),
    path('logout/', accountsViews.logout, name='logout'),
    path('freehome/', snsappViews.freehome, name='freehome'),
    path('freepostcreate/', snsappViews.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', snsappViews.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', snsappViews.new_freecomment, name='new_freecomment'),
    path('signup/', accountsViews.signup, name='signup'),
]
