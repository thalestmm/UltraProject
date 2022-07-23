from django.contrib import admin
from .models import Lead, LeadLabel

# Register your models here.
admin.site.register(LeadLabel)
admin.site.register(Lead)