from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import BookSerializer, BookshelfSerializer, UserSerializer, UserSerializerWithToken
from .models import Book, Bookshelf
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('bookshelf')
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all().order_by('title')
        bookshelf = self.request.query_params.get('bookshelf', None)
        if bookshelf is not None:
            queryset = queryset.filter(bookshelf=bookshelf)
        return queryset

class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer

    def get_queryset(self):
        queryset = Bookshelf.objects.all().order_by('name')
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

