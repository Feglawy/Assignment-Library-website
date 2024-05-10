import requests
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View

from .models import *
import os
# Create your views here.


def index(request):
    recommended =  RecommendedBooks.objects.all()
    return render(request, 'library/index.html', context={'recommended':recommended, 'user':request.user})

def about(request):
    return render(request, 'library/about.html', context={'user': request.user})

def search(request) -> HttpResponse:
    search_input = request.GET.get('search', '')
    search_by = request.GET.get('searchBy', '')

    books = Book.objects.all()

    if search_input and search_by:
        if search_by == 'title':
            books = books.filter(title__icontains=search_input)
        elif search_by == 'author':
            books = books.filter(authors__name__icontains=search_input)
        elif search_by == 'genre':
            books = books.filter(genres__name__icontains=search_input)
        
    searchHTML = loader.get_template('library/Search.html')
    return HttpResponse(searchHTML.render({'books': books, 'user':request.user}))

@login_required
def borrowed(request) -> HttpResponse:
    borrowedHTML = loader.get_template('library/BorrowedBooks.html')
    return HttpResponse(borrowedHTML.render({'user':request.user}))

@staff_member_required
def update(request) -> HttpResponse:
    updateHTML = loader.get_template('library/UpdateBooks.html')
    books = Book.objects.all()
    return HttpResponse(updateHTML.render(context={'books':books,'user':request.user}))

def available(request) -> HttpResponse:
    availableHTML = loader.get_template('library/AvailableBooks.html')
    books = Book.objects.all()
    books = books.filter(is_available=True)
    return HttpResponse(availableHTML.render(context={'books':books, 'user':request.user}))

def preview(request, book_title) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    book = Book.objects.get(title=book_title)
    return HttpResponse(previewHTML.render({'book':book, 'user':request.user}))

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
    
class SearchBooksAPI(View):
    def get(self, request):
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
            return JsonResponse(results, safe=False)
        
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)})