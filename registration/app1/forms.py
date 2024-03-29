from django import forms
from .models import Videos , Courses , Projects , QuizLevel, Questions
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

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

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class QuizLevelForm(forms.ModelForm):
    class Meta:
        model = QuizLevel
        fields = ('level_name', 'description', 'total_questions')

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('level', 'question_text', 'choice1', 'choice2', 'choice3', 'choice4', 'correct_answer')


    def calculate_score(self):
        score = 0
        for name, value in self.cleaned_data.items():
            question = Questions.objects.get(pk=name.split('_')[1])
            if value == question.correct_answer:
                score += 1
        return score


