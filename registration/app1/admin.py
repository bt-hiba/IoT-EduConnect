from django.contrib import admin
from .models import Videos , Comment , Courses , Projects , Questions , QuizLevel


# Register your models here.
admin.site.register(Videos)
admin.site.register(Comment)
admin.site.register(Courses)
admin.site.register(Projects)
admin.site.register(Questions)
admin.site.register(QuizLevel)