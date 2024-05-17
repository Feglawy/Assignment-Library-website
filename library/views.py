import requests
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpRequest, JsonResponse
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

    borrowed_records = None
    borrow_dict = {}
    
    if request.user.is_authenticated:
        borrowed_records = BorrowingRecord.objects.filter(user=request.user, returned=False).values_list('id','borrowed_book_id')
        borrow_dict = {borrow_id: book_id for book_id, borrow_id in borrowed_records}
    context = {'books':books, 
               'user':request.user, 
               'borrow_records':borrow_dict
               }

    return HttpResponse(availableHTML.render(context=context))

def preview(request, book_title) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    book = Book.objects.get(title=book_title)

    borrow_record = None
    borrowed_dict = {}

    if request.user.is_authenticated:
        try:
            borrow_record = BorrowingRecord.objects.filter(user=request.user, borrowed_book=book, returned=False).values_list('id','borrowed_book_id')
            borrowed_dict = {borrow_id: book_id for book_id, borrow_id in borrow_record}
        except BorrowingRecord.DoesNotExist or Exception as e:
            print("book not borrowed")
    
    context = {'book':book, 
            'user':request.user, 
            'borrow_record':borrow_record if borrow_record else None,
            'borrowed_dict':borrowed_dict
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
