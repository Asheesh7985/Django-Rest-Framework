from django.contrib import admin
from .models import Author,Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','gender']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','publish_date','author']
