from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('loggedin',views.loggedin,name='loggedin'),
]
