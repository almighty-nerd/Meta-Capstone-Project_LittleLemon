from django.urls import path 
from . import views

# url / app level 

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]