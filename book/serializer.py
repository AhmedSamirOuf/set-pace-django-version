from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'vendors', 'types', 'category', 'created_at', 'updated_at')
