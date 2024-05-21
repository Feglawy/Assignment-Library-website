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
    path('update/Authors/<str:name>', views.preview_author, name="preview_author"),
    path('update/Authors/new/', views.add_author, name="add_author_form"),
    path('update/Authors/edit/<str:name>', views.edit_author, name="edit_author_form"),
    path('update/Genres/', views.update_genres, name="update_genres"),
    path('update/Genres/<str:name>', views.preview_genre, name="preview_genre"),
    path('update/Types/', views.update_types, name="update_types"),
    path('update/Types/<str:name>', views.preview_type, name="preview_type"),
    path('book/<str:book_title>/', views.preview, name="preview"),
    path('update/new/', views.add_new_book, name="create_book"),
    path('update/edit/<int:book_id>', views.edit_book, name="edit_book"),
]
