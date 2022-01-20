from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    content = models.TextField(max_length=300)





