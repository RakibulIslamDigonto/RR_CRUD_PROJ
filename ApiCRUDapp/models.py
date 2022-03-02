from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PostModel(models.Model):
    author= models.ForeignKey(User, max_length=50, on_delete=models.CASCADE, related_name = 'author')
    title = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.title

