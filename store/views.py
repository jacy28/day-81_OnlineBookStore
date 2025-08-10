from django.shortcuts import render
from .models import Author, Book, Category

def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    categories = Category.objects.all()

    return render(request, 'store/home.html', {
        'authors': authors,
        'books': books,
        'categories': categories
    })
