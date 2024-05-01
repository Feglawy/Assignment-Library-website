import requests
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Book
import os
# Create your views here.

books = {'books': Book.objects.all()}

def index(request) -> HttpResponse:
    indexHTML = loader.get_template('library/index.html')
    return HttpResponse(indexHTML.render())

def about(request) -> HttpResponse:
    aboutHTML = loader.get_template('library/about.html')
    return HttpResponse(aboutHTML.render())

def search(request) -> HttpResponse:
    searchHTML = loader.get_template('library/Search.html')
    return HttpResponse(searchHTML.render())

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

def preview(request) -> HttpResponse:
    previewHTML = loader.get_template('library/preview.html')
    return HttpResponse(previewHTML.render())

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
    