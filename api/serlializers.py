from rest_framework import serializers
from accounts.models import *
from library.models import *



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'cover', 'authors', 'book_type', 'genres','is_available', 'language']
        read_only_fields = ['id']