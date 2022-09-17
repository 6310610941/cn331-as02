from django.contrib import admin

# Register your models here.

from .models import Course, Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ['subname', 'semester', 'year', 'seat', 'status']

admin.site.register(Course)
admin.site.register(Info, InfoAdmin)