
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('accounts/',include('accounts.urls')),
    path('posts/',include('posts.urls')),
    path('blueprint/',views.blueprint,name='blueprint'),
    path('search/',views.search,name='search'),
]

handler404 = 'myapp.views.error_404_view'
