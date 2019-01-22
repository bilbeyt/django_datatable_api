from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_api.models import CustomUser
from user_api.serializers import CustomUserSerializer
from django.views.generic.base import TemplateView


class CustomUserAPIView(APIView):

    def get(self, request, format=None):
        filter_params = self.request.query_params
        users = CustomUser.objects.filter(**filter_params.dict())
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class HomepageView(TemplateView):
    template_name = 'homepage.html'

