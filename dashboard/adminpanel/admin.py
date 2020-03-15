from django.contrib import admin
from .models import beacon,department,hit,notification

admin.site.register(beacon)
admin.site.register(department)
admin.site.register(hit)
admin.site.register(notification)
