from django.db import models
from users.models import User
import uuid
# Create your models here.

class BlogPost(models.Model):
    blogid = models.UUIDField(default=uuid.uuid4, editable=True)
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.Title[0:len(self.Title)-len(self.Title)//2]
    
class BlogComment(models.Model):
    OfBlog =  models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    Content = models.TextField()
    OfUser = models.ForeignKey(User,on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Content} comment of {self.OfBlog.Title[:len(self.OfBlog.Title)//2]}"