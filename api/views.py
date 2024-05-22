import requests
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, generics
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
        'Retrive book by id': '/book/<int:id>',
        'Retrive book by title': '/book/<str:title>',
        'Update book': '/book/update/<int:id>',
        'Delete book': '/book/delete/<int:id>',
        'search': '/book/?search=search_query&searchBy=search_by_[title, genre, author, type, language, is_available]',
        'random quote':'/random/quote/',
        'borrow a book':'/borrow/',
        'return a book':'/return/',
        'check book borrow timeout and return it':'borrow_timeout/',
        'get borrowed books' : '/borrowed_books/',
        'add a recommendation' : '/add_recommendation/',
        'delete a recommendation' : '/delete_recommendation/<int:book_id>',
    }

    return Response(api_urls)


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
def get_authors_like(request, name):
    authors = Author.objects.filter(name__icontains=name)
    serializer = AuthorSerializer(authors, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_genres_like(request, name):
    genres = Genre.objects.filter(name__icontains=name)
    serializer = AuthorSerializer(genres, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_types_like(request, name):
    types = Type.objects.filter(name__icontains=name)
    serializer = TypeSerializer(types, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_books_like(request, title):
    books = Book.objects.filter(title__icontains=title)
    serializer = BookSerializer(books, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

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





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def borrow(request):
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'book does not exist'},status=status.HTTP_404_NOT_FOUND)
    
    user = request.user

    record, created = BorrowingRecord.objects.get_or_create(
        user=user,
        borrowed_book=book,
        returned = False
    )

    if not created:
        return Response({'error': f'you already borrowed {book.title}'},status=status.HTTP_400_BAD_REQUEST)
    
    record.borrow()
    serializer = BorrowedBooksSerializer(record)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def return_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(pk=book_id)
        borrowed_book = BorrowingRecord.objects.get(
            user=user,
            borrowed_book=book,
            returned = False
        )
    except BorrowingRecord.DoesNotExist:
        return Response({'error': 'borrowing record does not exist'},status=status.HTTP_404_NOT_FOUND)

    borrowed_book.return_book()
    serializer = BorrowedBooksSerializer(borrowed_book)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def borrowed_book_timeout(request):
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(pk=book_id)
        borrowed_book = BorrowingRecord.objects.get(
            borrowed_book=book,
            returned = False
        )
    except BorrowingRecord.DoesNotExist:
        return Response({'error': 'borrowing record does not exit'}, status=status.HTTP_404_NOT_FOUND)
    except Book.DoesNotExist:
        return Response({'error':'book does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if borrowed_book.is_timeout():
        borrowed_book.return_book()
    serializer = BorrowedBooksSerializer(borrowed_book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def borrowed_books(request):
    user = request.user
    borrowed_books = BorrowingRecord.objects.filter(user=user, returned = False)
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_recommendation(request):
    book_id = request.data.get('book_id')

    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        ERROR_MESSAGE = 'This book id does not exist in the database'
        return Response({'error': ERROR_MESSAGE}, status=status.HTTP_404_NOT_FOUND)
    
    recommendation, created = RecommendedBooks.objects.get_or_create(
        book=book
    )

    if not created:
        ERROR_MESSAGE = 'This book is already recommended'
        return Response({'error': ERROR_MESSAGE}, status=status.HTTP_302_FOUND)

    serializer = RecommendedBooksSerializer(recommendation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_recommendation(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        recommendation = RecommendedBooks.objects.get(book=book)
    except RecommendedBooks.DoesNotExist:
        ERROR_MESSAGE = 'This book is not recommended'
        ERROR_RESPONSE = {'error': ERROR_MESSAGE}
        return Response(data=ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)
    except Book.DoesNotExist:
        ERROR_MESSAGE = 'This book does not exist in our database'
        ERROR_RESPONSE = {'error': ERROR_MESSAGE}
        return Response(data=ERROR_RESPONSE, status=status.HTTP_404_NOT_FOUND)

    serializer = RecommendedBooksSerializer(recommendation)
    recommendation.delete()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def recommended_books(request):
    recommended = RecommendedBooks.objects.all()
    serializer = RecommendedBooksSerializer(recommended, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAdminUser]

class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]