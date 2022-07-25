from django.contrib import admin
from .models import Lead, LeadLabel, UnsubscribeReason, UnsubscribeEvent

# Register your models here.
admin.site.register(LeadLabel)
admin.site.register(Lead)
admin.site.register(UnsubscribeReason)
admin.site.register(UnsubscribeEvent)