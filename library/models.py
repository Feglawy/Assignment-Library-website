from django.db import models
from django.urls import reverse
from django.conf import settings


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
    cover = models.ImageField(upload_to='book_covers/', default='book_covers/default.png')
    authors = models.ManyToManyField(Author)
    book_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    is_available = models.BooleanField(default=True)


    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("preview", kwargs={"book_id": self.pk})

class RecommendedBooks(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name = ("Recommended Book")
        verbose_name_plural = ("Recommended Books")

    def __str__(self) -> str:
        return self.book.title


