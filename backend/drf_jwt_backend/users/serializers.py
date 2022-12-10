from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =['id', 'first_name', 'last_name', 'email', 'address', 'type', 'type_id']
        depth = 1
    type_id = serializers.IntegerField(write_only=True)