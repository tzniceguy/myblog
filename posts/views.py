from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Post
from .serializers import PostSerializer

# Generic views for list and detail actions
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
