import requests
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
import os
# Create your views here.

books = {'books': Book.objects.all(),}
recommended = {'recommended': RecommendedBooks.objects.all(),}

def index(request) -> HttpResponse:
    indexHTML = loader.get_template('library/index.html')
    return HttpResponse(indexHTML.render(recommended))

def about(request) -> HttpResponse:
    aboutHTML = loader.get_template('library/about.html')
    return HttpResponse(aboutHTML.render())

def search(request) -> HttpResponse:
    search_input = request.GET.get('search-bar', '')
    search_by = request.GET.get('search-by', '')

    books = Book.objects.all()

    if search_input and search_by:
        if search_by == 'title':
            books = books.filter(title__icontains=search_input)
        elif search_by == 'author':
            books = books.filter(authors__name__icontains=search_input)
        elif search_by == 'genre':
            books = books.filter(genres__name__icontains=search_input)
        
    searchHTML = loader.get_template('library/Search.html')
    return HttpResponse(searchHTML.render({'books': books}))

def login(request) -> HttpResponse:
    loginHTML = loader.get_template('library/login.html')
    return HttpResponse(loginHTML.render())

def signup(request) -> HttpResponse:
    signupHTML = loader.get_template('library/signup.html')
    return HttpResponse(signupHTML.render())

def borrowed(request) -> HttpResponse:
    borrowedHTML = loader.get_template('library/BorrowedBooks.html')
    return HttpResponse(borrowedHTML.render())

def available(request) -> HttpResponse:
    availableHTML = loader.get_template('library/AvailableBooks.html')
    return HttpResponse(availableHTML.render(context=books))

def update(request) -> HttpResponse:
    updateHTML = loader.get_template('library/UpdateBooks.html')
    return HttpResponse(updateHTML.render())

def preview(request, book_id) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    book = Book.objects.get(pk=book_id)
    return HttpResponse(previewHTML.render({'book':book}))

#_______________________________________________________________
# end point using https://github.com/Sumansourabh14/recite api 
def random_quote(request) -> JsonResponse:
    try:
        response = requests.get("https://stoic.tekloon.net/stoic-quote")
        response.raise_for_status()

        # Parse the JSON response
        quote_data = response.json()

        response_data = {
            "quote": quote_data["quote"],
            "author": quote_data["author"],
        }
        return JsonResponse(response_data)
    
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    