from rest_framework import serializers
from .models import Client


class CLient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [ 'id', 'type']