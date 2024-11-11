from django.urls import path
from . import views

urlpatterns = [
    path('books_with_authors/', views.books_with_authors, name='books_with_authors'),
    path('books_with_tags/', views.books_with_tags, name='books_with_tags'),
    path('books_with_only_title/', views.books_with_only_title, name='books_with_only_title'),
    path('authors/', views.get_authors, name='get_authors'),
    path('books_by_author_sql/<int:author_id>/', views.books_by_author_sql, name='books_by_author_sql'),
]
