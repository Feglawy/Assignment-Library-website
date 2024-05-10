from django.contrib import admin
from .models import * 


class BookModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display  = ['id', 'title', 'is_available']


admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book, BookModelAdmin)
admin.site.register(RecommendedBooks)
