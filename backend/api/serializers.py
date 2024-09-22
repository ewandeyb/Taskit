""" 
A serializer is a class that is responsible for converting complex data types, such as querysets and model instances, 
into native Python data types that can then be easily rendered into JSON, XML, or other content types.

Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

"""

from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']