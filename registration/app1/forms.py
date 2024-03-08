from django import forms
from app1.models import Videos

class VideosForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = "__all__"
