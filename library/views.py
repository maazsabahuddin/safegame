# Rest framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Local Imports
from library.models.libray_model import Author, Book
from library.serializers import BookSerializer, AuthorSerializer

# Django Imports
from django.db import transaction
# from django.http import JsonResponse


# Using select_related to fetch related author data in one query
@api_view(['GET'])
def books_with_authors(request):
    # Retrieve all books with author and tags (optimized with select_related and prefetch_related)
    books = Book.objects.select_related('author').prefetch_related('tags').all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            serializer.save()
            # serialized_data = BookSerializer.custom_serialize_book(book_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
