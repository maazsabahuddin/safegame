from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Using raw SQL for complex queries
from django.db import connection


# Using select_related to fetch related author data in one query
@api_view(['GET'])
def books_with_authors(request):
    books = Book.objects.select_related('author').all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


# Using prefetch_related to fetch many-to-many related tags
@api_view(['GET'])
def books_with_tags(request):
    books = Book.objects.prefetch_related('tags').all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


# Using only() to load specific fields (e.g., only title and author)
@api_view(['GET'])
def books_with_only_title(request):
    books = Book.objects.only('title', 'author__name')
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def books_by_author_sql(request, author_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM library_book WHERE author_id = %s", [author_id])
        books = cursor.fetchall()
        # Simulate JSON response; ideally, transform data into a dictionary
        response_data = [{'id': book[0], 'title': book[1]} for book in books]
    return JsonResponse(response_data, safe=False)


@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return JsonResponse(serializer.data, safe=False)