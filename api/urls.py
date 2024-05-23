from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'types', TypesViewSet)
router.register(r'genres', GenresViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include(router.urls)),
    path('random/quote/', random_quote, name='quote'),

    path('book_like/<str:title>', get_books_like, name='book-like'),
    path('autor_like/<str:name>/', get_authors_like, name='author-like'),
    path('genre_like/<str:name>/', get_genres_like, name='genre-like'),
    path('type_like/<str:name>/', get_types_like, name='type-like'),
 

    path('book/create/', add_book, name='create-book'),
    path('book/<int:id>', get_book_by_id, name='get-book-by-id'),
    path('book/<str:title>', get_book_by_title, name='get-book-by-title'),
    path('book/update/<int:pk>', update_book, name='update-book'),
    path('book/delete/<int:pk>', delete_book, name='delete-book'),
    
    path('search/', search_books, name="search-books"),
    
    path('borrow/', borrow, name='borrow'),
    path("return/", return_book, name="return"),
    path("borrow_timeout/", borrowed_book_timeout, name="borrow-timeout"),
    path('borrowed_books/', borrowed_books , name='borrowed_books'),
    
    path('add_recommendation/', add_recommendation, name='add_recommendation'),
    path('delete_recommendation/<int:book_id>', delete_recommendation, name='delete_recommendation'),
]