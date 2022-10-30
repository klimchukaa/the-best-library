from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book
from django.template import loader

# Create your views here.

def listed_books(request):
    books_list = Book.objects.all()
    context = {
        'books_list' : books_list
    }
    return render(request, 'library/listed_books.html', context)

def books_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'library/books_detail.html', {'book' : book})

def author_detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'library/author_detail.html', {'author' : author})