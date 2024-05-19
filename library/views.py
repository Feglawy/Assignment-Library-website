import requests
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.views.generic import View

from .models import *
from .forms import *
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
    
    context = {'books':books, 
               'user':request.user, 
               }

    return HttpResponse(availableHTML.render(context=context))

def preview(request, book_title) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    book = Book.objects.get(title=book_title)
    try:
        borrow_record = BorrowingRecord.objects.get(borrowed_book=book, returned=False)
        context = {
            'book':book, 
            'user':request.user, 
            'returned_by':borrow_record.return_by
            }

    except BorrowingRecord.DoesNotExist:
        context = {
            'book':book, 
            'user':request.user, 
            }

    return HttpResponse(previewHTML.render(context))

@staff_member_required
def add_new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            
    else:
        form = BookForm()
    
    context = {
        'user': request.user,
        'form': form,
    }
    create_book_HTML = 'library/create_book.html'
    return render(request, create_book_HTML, context)

@staff_member_required
def edit_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Resource not found")

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('update')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    else:
        form = BookForm(instance=book)
    edit_book_HTML = 'library/create_book.html'
    
    context= {
        'user':request.user,
        'form':form,
        'book':book,
    }
    return render(request, edit_book_HTML, context=context)