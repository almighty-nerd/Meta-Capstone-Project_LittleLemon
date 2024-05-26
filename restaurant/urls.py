from django.urls import path 
from . import views

# url / app level 

urlpatterns = [
    path('',views.index,name='index'),
]