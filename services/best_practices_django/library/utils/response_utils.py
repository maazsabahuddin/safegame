
def get_response_object(response_code, response_data=None, response_message=None):

    response = {
        "response_code": response_code
    }
    if response_data:
        response.update({
            "response_data": response_data
        })
    if response_message:
        response.update({
            "response_message": response_message
        })
    return response
