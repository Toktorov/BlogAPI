from unicodedata import category
from rest_framework import serializers
from apps.categories.models import Category
from apps.posts.serializers import PostSerializer

class CategorySerializer(serializers.ModelSerializer):
    category = PostSerializer(read_only = True, many = True)
    class Meta:
        model = Category
        fields = "__all__"

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
