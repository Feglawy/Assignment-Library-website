from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiOverView, name="api-overview"),
    path('random/quote/', random_quote, name='quote'),
    path('book/create/', add_book, name='create-book'),
    path('book/<int:id>', get_book_by_id, name='get-book-by-id'),
    path('book/update/<int:pk>', update_book, name='update-book'),
    path('book/delete/<int:pk>', delete_book, name='delete-book'),
    path('search/',search_books, name="search-books")
]
