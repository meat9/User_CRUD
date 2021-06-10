from rest_framework import serializers
from .models import Author, Book, User

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name', 'added_by', 'created_date']

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title', 'description', 'author', 'added_by', 'created_date']
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user