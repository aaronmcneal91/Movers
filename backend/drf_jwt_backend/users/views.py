from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import Users

@api_view (['GET', 'POST'])
@permission_classes([AllowAny])
def get_users(request):
    users = Users.objects.all()
    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

