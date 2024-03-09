from django.db import models

# Create your models here.
class Videos(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(upload_to="img/%y")
    video_url = models.URLField()
    
def __str__(self):
  return self.title
    