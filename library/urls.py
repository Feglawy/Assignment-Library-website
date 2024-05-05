from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('borrowed/', views.borrowed, name="borrowed"),
    path('available-books/', views.available, name="available"),
    path('update-books/', views.update, name="update"),
    path('book/<int:book_id>/', views.preview, name="preview"),
    path('random/quote/', views.random_quote, name="quote"),

]