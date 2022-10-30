from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.listed_books, name="bookshelf"),
    path('books/<int:book_id>/', views.books_detail, name='books_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]