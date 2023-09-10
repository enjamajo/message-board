from django.db import models

# Create your models here.

def __str__(self): 
    return self.text[:50]

class Post(models.Model):
    text = models.TextField()
