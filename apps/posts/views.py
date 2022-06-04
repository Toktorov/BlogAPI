from django.shortcuts import render
from rest_framework import generics
from apps.posts.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer,CommentSerializer,CommentCreateSerializer,CommentUpdateSerializer
from apps.posts.models import Post,PostComment

# Create your views here.
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCommentAPIView(generics.ListAPIView):
    queryset = PostComment.objects.all() 
    serializer_class = CommentSerializer

class PostCommentCreateAPIView(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentCreateSerializer


class PostCommentUpdateAPIView(generics.UpdateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = CommentUpdateSerializer


class PostCommentDeleteAPIView(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class =  CommentSerializer