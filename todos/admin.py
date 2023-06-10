from django.contrib import admin
from .models import Task

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['task','is_completed','created_at','updated_at']
    search_fields = ('task',)

admin.site.register(Task,TaskModelAdmin)
