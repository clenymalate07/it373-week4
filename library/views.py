from django.shortcuts import render
from .models import Book, Category

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'library/book_list.html', {'books': books, 'categories': categories})

