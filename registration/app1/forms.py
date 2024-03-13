from django import forms
from .models import Videos , Courses , Projects

class VideosForm(forms.ModelForm):
  class Meta:
    model=Videos
    fields=("title","description","image","video_url")
    

class CoursesForm(forms.ModelForm):
  class Meta:
    model=Courses
    fields=("title","description","image","pdf")
    
    
class ProjectsForm(forms.ModelForm):
  class Meta:
    model=Projects
    fields=("title","description","image","link")