from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from users.models import *
from .custom import is_valid_uuid
from rest_framework.decorators import action
from rest_framework import status


# here i am using viewsets for creating views because it is easy to manage

class BlogPosts(viewsets.ViewSet):
    def bloglist(self, request):
        queryset = BlogPost.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def blogpostdetailview(self,request,**kwargs):
        blog = BlogPost.objects.filter(blogid=kwargs.get('id')).first()
        print(blog)
        serializer = BlogSerializer(blog)
        print(serializer.data)
        return Response(serializer.data)
    
    def blogpostComment(self,request,**kwargs):
        blog = BlogPost.objects.filter(blogid=kwargs.get('id')).first()
        comments = BlogComment.objects.filter(OfBlog=blog)
        serializer = BlogCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    def addblogpost(self,request,**kwargs):
        title= request.data.get('title')
        user = request.data.get('user')
        content = request.data.get('content')
        
        user = User.objects.filter(email=user).first()
        if user!=None and user:
            BlogPost.objects.create(Title=title,Content=content,Author=user)
            return Response(status=201)
        else:
            return Response(status=401,data="User Not Found")
    
    def addCommentOnBlog(self,request):
        blogid= request.data.get('blogid')
        user = request.data.get('user')
        content = request.data.get('content')
        if is_valid_uuid(blogid):
            pass
        else:
            return Response(status=422, data="Invalid UUID as blogid")
        user = User.objects.filter(email=user).first()
        blog = BlogPost.objects.filter(blogid=blogid).first()
        if user!=None and user:
            if blog!=None and blog:
                BlogComment.objects.create(Content=content,OfUser=user,OfBlog=blog)
                return Response(status=201)
            else:
                return Response(status=404,data="Blog Not Found")
        else:
            return Response(status=401,data="User Not Found")
        
    @action(detail=True, methods=['put'])
    def updateblogpost(self, request, id):
        try:
            blog = BlogPost.objects.get(blogid=id)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Blog Not Found")

        title = request.data.get('title')
        content = request.data.get('content')
        user = request.data.get('user')
        
        user = User.objects.filter(email=user).first()
        
        # checking that current user and blog Author are same or not
        if user != blog.Author:
            return Response(status=401,data="You do not have permission to edit this blog")
        
        if user!=None and user:
            if title is not None:
                blog.Title = title
            if content is not None:
                blog.Content = content
            
            blog.save()
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:
            return Response(status=401,data="User Not Found")

