
from dataclasses import field
from rest_framework import  serializers
from apps.posts.models import Post, PostComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Post 
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"