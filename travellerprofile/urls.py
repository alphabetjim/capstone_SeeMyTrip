from django.urls import path
from . import views

urlpatterns = [
    path('', views.TravellerList.as_view(), name='profile'),
    path('view_traveller/', views.view_traveller, name='view_traveller'),
]