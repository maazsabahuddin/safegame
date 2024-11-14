# Python Imports
from functools import wraps
import logging

# Django Imports
# from django.http import JsonResponse
from django.conf import settings

# Rest framework Imports
from rest_framework import status
from rest_framework.response import Response

# Local Imports
from library.utils import response_utils


def validator(required_fields):
    def decorator(view_function):
        @wraps(view_function)
        def wrapper(request, *args, **kwargs):
            # Ensure required_fields is not empty
            if not required_fields:
                return view_function(request, *args, **kwargs)

            # Extract JSON payload
            data = request.data if hasattr(request, 'data') else request.POST

            # Validate required fields
            missing_fields = [field for field in required_fields if field not in data or data.get(field) in [None, ""]]

            # If missing fields, return an error response
            if missing_fields:
                message = f"Missing parameter keys: {', '.join(missing_fields)}"
                response = response_utils.get_response_object(response_code=status.HTTP_400_BAD_REQUEST,
                                                              response_message=message)
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

            # Pass validated data to the view function
            return view_function(request, *args, **kwargs)

        return wrapper

    return decorator


# Set up logging
logger = logging.getLogger('best_practices_django')


def logging(view_function):
    @wraps(view_function)
    def wrapper(request, *args, **kwargs):
        try:
            # Call the view function
            # Check request origin and log it
            origin = request.META.get('HTTP_HOST')
            logger.info(f"Request origin: {origin}")

            # Validate origin if configured
            if getattr(settings, 'VALIDATE_ORIGIN', False) and origin not in getattr(settings, 'ALLOWED_ORIGINS', []):
                return Response({"code": 405, "message": "Unable to entertain request"}, status=405)

            # Execute the view function and return its response
            return view_function(request, *args, **kwargs)

        except Exception as e:
            logger.error("An error occurred: %s", str(e), exc_info=True)

            # Return a generic error message to the client
            response = (
                response_utils.get_response_object(response_code=status.HTTP_400_BAD_REQUEST,
                                                   response_message="Something went wrong. Please try again later.")
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    return wrapper


def blocked(view_function):
    @wraps(view_function)
    def wrapper(request, *args, **kwargs):
        # Assuming `response_utils.get_response_object` returns a dictionary
        response = response_utils.get_response_object(
            response_code=301,
            response_message="This API is Depreciated"
        )
        return Response(response, status=410)  # HTTP 410 Gone for deprecated endpoints

    return wrapper
