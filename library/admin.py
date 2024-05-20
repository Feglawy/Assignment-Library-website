from django.contrib import admin
from .models import * 


class TagModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']


class BookModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display  = ['__str__','id', 'is_available']

class BorrowModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['user', 'borrowed_book','returned', 'borrowed_at', 'return_by']

admin.site.register(Type, TagModelAdmin)
admin.site.register(Genre, TagModelAdmin)
admin.site.register(Author, TagModelAdmin)
admin.site.register(Book, BookModelAdmin)
admin.site.register(RecommendedBooks)
admin.site.register(BorrowingRecord, BorrowModelAdmin)

