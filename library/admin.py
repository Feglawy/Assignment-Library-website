from django.contrib import admin
from .models import * 


class BookModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display  = ['__str__','id', 'is_available']

class BorrowModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['user', 'borrowed_book','returned']

admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book, BookModelAdmin)
admin.site.register(RecommendedBooks)
admin.site.register(BorrowingRecord, BorrowModelAdmin)

