from rest_framework import serializers
from .models import *

class BlogSerializer(serializers.ModelSerializer):
    Author = serializers.CharField(source="Author.name")
    class Meta:
        model = BlogPost
        fields = ['blogid','Title','Content','Author','CreatedAt','UpdatedAt']

class BlogCommentsSerializer(serializers.ModelSerializer):
    OfBlog = serializers.CharField(source="OfBlog.blogid")
    OfUser = serializers.CharField(source="OfUser.name")
    class Meta:
        model = BlogComment
        fields = ['OfBlog','Content','OfUser','CreatedAt','UpdatedAt']
            