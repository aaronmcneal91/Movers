from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import Users

@api_view (['GET'])
@permission_classes([AllowAny])
def get_users(request):
    user = Users.objects.all()
    if request.method == 'GET':
        serializers = UserSerializer(user, many=True)
        return Response (serializers.data)
