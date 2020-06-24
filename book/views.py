from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book.serializer import BookSerializer


@api_view(['POST'])
def add_book(request):
    book_info = request.data
    serializer = BookSerializer(data=book_info)
    if serializer.is_valid():
        serializer.save()
        return Response(book_info, status=status.HTTP_201_CREATED)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
