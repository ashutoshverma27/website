from django.urls import path,include
from . import views


urlpatterns = [
    path('add/',views.add, name='add'),
    path('added/',views.added,name='added'),

]
