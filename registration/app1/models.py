from django.db import models  

class Videos(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    video_url = models.URLField()
    
    def __str__(self):
        return "%s " %(self.title) 
    class Meta:  
        db_table = "videos"  
