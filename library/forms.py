from django import forms
from .models import Book, Author, Genre, Type, RecommendedBooks



class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class RecommendedBooksForm(forms.ModelForm):
    class Meta:
        model = RecommendedBooks
        fields = '__all__'
