from user_api.models import CustomUser
from rest_framework.exceptions import NotFound


class APIRequestCheck:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if not user.is_authenticated:
            raise NotFound
        else:
            return self.get_response(request)
        

