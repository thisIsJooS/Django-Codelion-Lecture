from django.contrib import admin
from django.urls import path, include
from myapp import views as myappViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myappViews.first),
    path('product/', include('product.urls')),
    path('board/', include('board.urls')),
]
