from django.db import models

# Create your models here.
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
     content = models.TextField() 
    
def __str__(self):
  return self.title
