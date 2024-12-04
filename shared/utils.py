import os


def load_config(key, default=None):
    """
    Load a configuration value from environment variables.

    Args:
        key (str): The configuration key.
        default: The default value if the key is not found.

    Returns:
        str: The configuration value.
    """
    return os.getenv(key, default)


def format_error_response(message, status_code):
    """
    Format a standardized error response.

    Args:
        message (str): Error message.
        status_code (int): HTTP status code.

    Returns:
        dict: Formatted error response.
    """
    return {
        "error": {
            "message": message,
            "status_code": status_code
        }
    }
