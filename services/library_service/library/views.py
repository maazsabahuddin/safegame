# Rest framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Local Imports
from library.models.libray_model import Author, Book
from library.serializers import BookSerializer, AuthorSerializer
from library.utils import decorators, response_utils, constants

# Django Imports
from django.db import transaction


@api_view(['GET'])
@decorators.logging
def books_with_authors(request):
    """
    This API will return the all the books with the author name and the tags associated with the book.
    :param request:
    """
    # Retrieve all books with author and tags (optimized with select_related and prefetch_related)
    books = Book.objects.select_related('author').prefetch_related('tags').all()
    serializer = BookSerializer(books, many=True)

    response = response_utils.get_response_object(response_code=status.HTTP_200_OK,
                                                  response_data=serializer.data,
                                                  response_message=constants.SUCCESS)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@decorators.logging
def get_authors(request):
    """
    This API will return the all the Authors in the database.
    :param request:
    """
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    response = response_utils.get_response_object(response_code=status.HTTP_200_OK,
                                                  response_data=serializer.data,
                                                  response_message=constants.SUCCESS)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
@decorators.logging
@decorators.validator(['title', 'author', 'tags'])
def create_book(request):
    """
    This API will return create the book and associate it with the author name and the tags provided.
    :param request:
    """
    serializer = BookSerializer(data=request.data)

    if not serializer.is_valid():
        response = response_utils.get_response_object(response_code=status.HTTP_400_BAD_REQUEST,
                                                      response_message=serializer.errors)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    with transaction.atomic():
        serializer.save()

    response = response_utils.get_response_object(response_code=status.HTTP_201_CREATED,
                                                  response_data=serializer.data,
                                                  response_message=constants.SUCCESS)
    return Response(response, status=status.HTTP_200_OK)
