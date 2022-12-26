from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    
class UserDetall(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer    
    
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    
    
class PostDetall(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer        