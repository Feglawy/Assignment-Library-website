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
    return render(request, 'library/index.html', context={'recommended':recommended})

def about(request):
    return render(request, 'library/about.html', context={})

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
        
    searchHTML = 'library/Search.html'
    context = {'books': books,}
    return render(request, searchHTML, context=context)

@login_required
def borrowed(request) -> HttpResponse:
    borrowedHTML = 'library/BorrowedBooks.html'
    users_borrowed_records = BorrowingRecord.objects.filter(user=request.user, returned=False)
    context = {'books':users_borrowed_records}
    return render(request, borrowedHTML, context=context)

@staff_member_required
def update(request) -> HttpResponse:
    updateHTML = 'library/UpdateBooks.html'
    books = Book.objects.all()
    context = {'books':books, }
    return render(request, updateHTML, context=context)

@staff_member_required
def update_authors(request) -> HttpResponse:
    updateHTML = 'admin/UpdateAuthor.html'
    authors = Author.objects.all()
    form = AuthorForm()
    context = {'items':authors, 'type':'authors', 'form':form}
    return render(request, updateHTML, context=context)

@staff_member_required
def update_genres(request) -> HttpResponse:
    updateHTML = 'admin/UpdateGenre.html'
    genres = Genre.objects.all()
    form = GenreForm()
    context = {'items':genres,'type':'genres',  'form':form}
    return render(request, updateHTML, context=context)

@staff_member_required
def update_types(request) -> HttpResponse:
    updateHTML = 'admin/UpdateType.html'
    types = Type.objects.all()
    form = TypeForm()
    context = {'items':types, 'type':'types',  'form':form }
    return render(request, updateHTML, context=context)


def available(request) -> HttpResponse:
    availableHTML = 'library/AvailableBooks.html'
    books = Book.objects.all()
    
    context = {'books':books, 
               }

    return render(request, availableHTML, context=context)


def preview(request, book_title):
    previewHTML = 'library/preview.html'
    book = Book.objects.get(title=book_title)
    try:
        borrow_record = BorrowingRecord.objects.get(borrowed_book=book, returned=False)
        context = {
            'book':book, 
            'returned_by':borrow_record.return_by
            }

    except BorrowingRecord.DoesNotExist:
        context = {
            'book':book, 
            }
    return render(request, previewHTML, context=context)

def preview_author(request, name):
    preview_tag_template = 'library/preview_item.html'
    try:
        author = Author.objects.get(name=name)
        books = Book.objects.filter(authors=author)
    except Author.DoesNotExist:
        return HttpResponse("not found")

    context = {
        'item':author,
        'books':books,
    }
    return render(request, preview_tag_template, context=context)


def preview_genre(request, name):
    preview_tag_template = 'library/preview_item.html'
    try:
        genre = Genre.objects.get(name=name)
        books = Book.objects.filter(genres=genre)
    except Author.DoesNotExist:
        return HttpResponse("not found")

    context = {
        'item':genre,
        'books':books,
    }
    return render(request, preview_tag_template, context=context)

def preview_type(request, name):
    preview_tag_template = 'library/preview_item.html'
    try:
        type = Type.objects.get(name=name)
        books = Book.objects.filter(book_type=type)
    except Author.DoesNotExist:
        return HttpResponse("not found")

    context = {
        'item':type,
        'books':books,
    }
    return render(request, preview_tag_template, context=context)


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
        'form': form,
    }
    create_book_HTML = 'library/create_book.html'
    return render(request, create_book_HTML, context)

@staff_member_required
def edit_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse("not found")


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
        'form':form,
        'book':book,
    }
    return render(request, edit_book_HTML, context=context)


@staff_member_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_authors')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            
    else:
        form = AuthorForm()
    
    context = {
        'form':form,
    }
    add_author_template = 'library/add_author.html'
    return render(request, add_author_template, context)

@staff_member_required
def edit_author(request, name):
    try:
        author = Author.objects.get(name=name)
    except Author.DoesNotExist:
        return HttpResponse("not found")


    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()
            return redirect('update_authors')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    else:
        form = AuthorForm(instance=author)
    edit_author_template = 'library/add_author.html'
    
    context= {
        'form':form,
    }
    return render(request, edit_author_template, context=context)