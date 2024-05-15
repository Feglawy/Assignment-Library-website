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
    users_borrowed_records = BorrowingRecord.objects.filter(user=request.user, returned=False)
    return HttpResponse(borrowedHTML.render({'user':request.user, 'books':users_borrowed_records}))

@staff_member_required
def update(request) -> HttpResponse:
    updateHTML = loader.get_template('library/UpdateBooks.html')
    books = Book.objects.all()
    return HttpResponse(updateHTML.render(context={'books':books,'user':request.user}))

def available(request) -> HttpResponse:
    availableHTML = loader.get_template('library/AvailableBooks.html')
    books = Book.objects.all()
    return HttpResponse(availableHTML.render(context={'books':books, 'user':request.user}))

def preview(request, book_title) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    book = Book.objects.get(title=book_title)
    is_borrowed = True
    borrow_record = BorrowingRecord()
    try:
        borrow_record = BorrowingRecord.objects.get(user=request.user, borrowed_book=book, returned=False)
    except BorrowingRecord.DoesNotExist:
        is_borrowed = False
    context = {'book':book, 
               'user':request.user, 
               'borrow_record':borrow_record if borrow_record else None,
               'borrowed':is_borrowed
               }

    return HttpResponse(previewHTML.render(context))