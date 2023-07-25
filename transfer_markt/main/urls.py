from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about_page),
    path('contacts', views.contact_page),
    path('player/<int:pk>', views.player_page),
    path('category/<str:pk>', views.category_page),
    path('search', views.search_player),
    path('create', views.create, name='create'),
]