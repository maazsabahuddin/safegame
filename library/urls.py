from django.urls import path
from . import views

urlpatterns = [
    path('books_with_authors/', views.books_with_authors, name='books_with_authors'),
    path('authors/', views.get_authors, name='get_authors'),
    path('create_book/', views.create_book, name='create_book'),
]
