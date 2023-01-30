from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post
from author.models import Author
from book.models import Book


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'created', 'user']


class UserSerializer(serializers.ModelSerializer):
    #posts = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    posts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'posts']
        
  
class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.first_name')
    
    class Meta:
        model = Book
        fields = ['title', 'summary', 'price', 'amount', 'author']    
        
 
class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'books']      