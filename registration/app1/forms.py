from django import forms
from .models import Videos

class VideosForm(forms.ModelForm):
  class Meta:
    model=Videos
    fields=("title","description","image","video_url")