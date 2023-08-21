from django.urls import path, include
from .views import *


# defining the function of specific url path and defining the http request protocol like get,post,put,delete
blog_list = BlogPosts.as_view({
    'get': 'bloglist',
})
blog_page = BlogPosts.as_view({
    'get':'blogpostdetailview',
})
blog_comments = BlogPosts.as_view({
    'get':'blogpostComment'
})
add_blog = BlogPosts.as_view({
    'post':'addblogpost'
})
add_comment_on_blog = BlogPosts.as_view({
    'post':'addCommentOnBlog'
})
blog_update = BlogPosts.as_view({
    'put': 'updateblogpost',
})
# url for our users app
urlpatterns = [
    path('blogs', blog_list),
    path('blog/<str:id>', blog_page),
    path('blogcomments/<str:id>',blog_comments),
    path('addblog',add_blog),
    path('addcomment',add_comment_on_blog),
    path('updateblog/<str:id>',blog_update),
    
]