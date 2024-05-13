from rest_framework import serializers
from accounts.models import *
from library.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
    
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'cover', 'authors', 'book_type', 'genres','is_available', 'language']
        read_only_fields = ['id']

    def create(self, validated_data):
        authors_data = validated_data.pop('creators')
        genres_data = validated_data.pop('genres')
        type_data = validated_data.pop('book_type')

        book = Book.objects.create(**validated_data)

        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(**author_data)
            book.authors.add(author)
        
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            book.genres.add(genre)
        
        book_type, _ = Type.objects.get_or_create(**type_data)
        book.book_type = book_type

        book.save()
        return book