from django.contrib import admin
from .models import Videos , Comment , Courses


# Register your models here.
admin.site.register(Videos)
admin.site.register(Comment)
admin.site.register(Courses)