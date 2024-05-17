import requests
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serlializers import *
from library.models import *
from accounts.models import CustomUser

@api_view(['GET'])
def ApiOverView(request):
    api_urls = {
        'Retrive all Authors' : '/authors',
        'Retrive all Genres' : '/genres',
        'Retrive all Types' : '/types',
        'Create book': '/book/create/',
        'Retrive book by id': '/book/id',
        'Retrive book by title': '/book/title',
        'Update book': '/book/update/id',
        'Delete book': '/book/delete/id',
        'search': '/book/?search=search_query&searchBy=search_by_[title, genre, author, type, language, is_available]',
        'random quote':'/random/quote/',
        'borrow a book':'/borrow/',
        'return a book':'/return/',
        'get borrowed books' : '/borrowed_books/'
    }

    return Response(api_urls)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_book(request): # Create book
    book = BookSerializer(data=request.data)

    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Trying to create a book that already exists use update instead")
    
    if book.is_valid():
        book.save()
        return Response(book.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_authors(requset):
    try:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_409_CONFLICT)
    
@api_view(['GET'])
def get_genres(request):
    try:
        Genres = Genre.objects.all()
        serializer = GenreSerializer(Genres, many=True)
        return Response(data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_409_CONFLICT)
    
@api_view(['GET'])
def get_types(request):
    try:
        Types = Type.objects.all()
        serializer = TypeSerializer(Types, many=True)
        return Response(data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_409_CONFLICT)
    
@api_view(['GET'])
def get_book_by_id(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = BookSerializer(book)
    return Response(data.data)

@api_view(['GET'])
def get_book_by_title(request, title):
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = BookSerializer(book)
    return Response(data.data)


@api_view(['GET'])
def search_books(request): # Retrive books
    try:
        books = Book.objects.all()

        search_query = request.GET.get('search', '')
        search_by_query = request.GET.get('searchBy', '')

        results = []

        if search_query and search_by_query:
            if search_by_query == 'title':
                books = books.filter(title__icontains=search_query)
            elif search_by_query == 'author':
                books = books.filter(authors__name__icontains=search_query)
            elif search_by_query == 'genre':
                books = books.filter(genres__name__icontains=search_query)
            elif search_by_query == 'language':
                books = books.filter(language__icontains=search_query)
            elif search_by_query == 'available':
                books = books.filter(is_available=1)
        
        results = [{"pk":book.pk,"title": book.title, "cover": book.cover.url, "url":book.get_absolute_url()} for book in books]
        return Response(results)
    
    except requests.RequestException as e:
        return Response({"error": str(e)})

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = BookSerializer(instance=book, data=request.data, partial = True)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) # Delete book
@permission_classes([IsAdminUser])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



@api_view(['GET'])
def random_quote(request):
    try:
        # old api https://github.com/Sumansourabh14/recite it was slow
        # the new one might return a quote with @ in the end of thee quote also sometimes it doesn't return an author
        response = requests.get("https://stoic.tekloon.net/stoic-quote")
        response.raise_for_status()

        # Parse the JSON response
        quote_data = response.json()

        response_data = {
            "quote": quote_data["quote"],
            "author": quote_data["author"],
        }
        return Response(response_data)
    
    except requests.RequestException as e:
        return Response({"error": str(e)}, status=response.status_code)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def borrow(request):
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'book does not exist'},status=status.HTTP_404_NOT_FOUND)
    
    user = request.user

    borrow, created = BorrowingRecord.objects.get_or_create(
        user=user,
        borrowed_book=book,
        returned = False
    )

    if not created:
        return Response({'error': f'you already borrowed {book.title}'},status=status.HTTP_400_BAD_REQUEST)

    serializer = BorrowedBooksSerializer(borrow)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def return_book(request):
    user = request.user
    borrow_id = request.data.get('borrow_id')
    try:
        borrowed_books = BorrowingRecord.objects.get(pk=borrow_id)
    except BorrowingRecord.DoesNotExist:
        return Response({'error': 'borrowing record does not exist'},status=status.HTTP_404_NOT_FOUND)

    borrowed_books.returned = True
    borrowed_books.save()
    serializer = BorrowedBooksSerializer(borrowed_books)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def borrowed_books(request):
    user = request.user
    borrowed_books = BorrowingRecord.objects.filter(user=user, returned = False)
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)