from django.contrib import admin
from django.urls import path, include
from myapp import views as myappViews
from staticapp import views as staticappViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myappViews.first),
    path('product/', include('product.urls')),
    path('board/', include('board.urls')),
    path('statics/', staticappViews.home),
    path('bootapp/', include('bootapp.urls')),
]
