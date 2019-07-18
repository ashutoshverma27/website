from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('loggedin',views.loggedin,name='loggedin'),
   path('logout/',views.logout,name='logout'),
   path('profile/', views.profile,name='profile'),
   path('reset_pass/',views.reset_pass,name='reset_pass'),
   path('cart/',views.cart,name='cart'),
]
