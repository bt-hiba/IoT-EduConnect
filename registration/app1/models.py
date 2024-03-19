from django.db import models
from django.contrib.auth.models import AbstractUser ,  Group , Permission

# Create your models here.

class User(AbstractUser):
    country = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='')
    school_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
def __str__(self):
  return self.country

class Videos(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(upload_to="img/%y")
    video_url = models.FileField(upload_to="videos/%Y")
    
def __str__(self):
  return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Videos, related_name='comments', on_delete=models.CASCADE) 
    user_name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
  
class Courses(models.Model):  
     title = models.CharField(max_length=100)
     description = models.TextField()
     image=models.ImageField(upload_to="img/%y")
     pdf = models.FileField(upload_to='course_pdfs/', default='default.pdf')
    
def __str__(self):
  return self.title

class Projects(models.Model):  
     title = models.CharField(max_length=100)
     description = models.TextField()
     image=models.ImageField(upload_to="img/%y")
     link = models.URLField(max_length=200,default='')
    
def __str__(self):
  return self.title
