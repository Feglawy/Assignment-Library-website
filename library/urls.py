from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('borrowed/', views.borrowed, name="borrowed"),
    path('books/', views.available, name="available"),
    path('update/', views.update, name="update"),
    path('update/Books/', views.update, name="update_books"),
    path('update/Authors/', views.update_authors, name="update_authors"),
    path('update/Genres/', views.update_genres, name="update_genres"),
    path('update/Types/', views.update_types, name="update_types"),
    path('book/<str:book_title>/', views.preview, name="preview"),
    path('update-books/new/', views.add_new_book, name="create_book"),
    path('update-books/edit/<int:book_id>', views.edit_book, name="edit_book"),

]