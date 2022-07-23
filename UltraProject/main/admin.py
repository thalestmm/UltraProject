from django.contrib import admin
from .models import Discipline, Area, Subject, Question, Exam

# Register your models here.
admin.site.register(Discipline)
admin.site.register(Area)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Exam)