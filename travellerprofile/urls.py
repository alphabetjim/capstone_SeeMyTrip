from django.urls import path
from . import views

urlpatterns = [
    path('create_traveller/', views.create_traveller, name='create_traveller'),
    path('../home', views.home_page, name='home'),
    path('', views.TravellerList.as_view(), name='profile'),
    path('view_traveller/', views.view_traveller, name='view_traveller'),
]