from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('borrowed/', views.borrowed, name="borrowed"),
    path('books/', views.available, name="available"),
    path('update-books/', views.update, name="update"),
    path('book/<str:book_title>/', views.preview, name="preview"),
    path('update-books/new/', views.add_new_book, name="create_book"),
]