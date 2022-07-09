from django.contrib import admin
from .models import Student, Subject, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Course)