from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from accounts.models import CustomUser
import os

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Type(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"

class Author(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255,null=False,unique=True)
    desc = models.TextField()
    cover = models.ImageField(upload_to='book_covers\\', default='book_covers\\default.png', null=False)
    authors = models.ManyToManyField(Author)
    book_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    is_available = models.BooleanField(default=True)


    LANGUAGES = [
        ('en', 'English'),
        ('ar', 'Arabic'),
    ]
    DEFAULT_LANGUAGE = 'en'

    language = models.CharField(max_length=2, choices=LANGUAGES, default=DEFAULT_LANGUAGE)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("preview", kwargs={"book_title": self.title})

    def save(self, *args, **kwargs):
        if self.cover:
            dir_path, file = os.path.split(self.cover.name)
            image_name, ext = os.path.splitext(file)
            
            if image_name == "default": # checks if the image is the default one so it doesn't change it
                super().save(*args, **kwargs)
                return

            saved_image_name = f"{dir_path + "\\" if dir_path else ""}{self.title.replace(' ', '_')}{ext}"
            self.cover.name = saved_image_name

        super().save(*args,**kwargs)

class RecommendedBooks(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, unique=True, related_name='recommended_books')

    def __str__(self) -> str:
        return self.book.title


class BorrowingRecord(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    borrowed_at = models.DateTimeField(auto_now_add=timezone.now)
    return_by = models.DateTimeField(default=timezone.now)

    def borrow(self):
        self.return_by = timezone.now() + timedelta(days=14)
        self.borrowed_book.is_available = False
        self.borrowed_book.save()
        self.returned = False
        self.save()

    def return_book(self):
        self.borrowed_book.is_available = True
        self.borrowed_book.save()
        self.returned = True
        self.save()

    def is_timeout(self):
        return self.return_by < timezone.now() + timedelta()
    

    def __str__(self) -> str:
        return f"{self.user.username} borrowed {self.borrowed_book.title}"
