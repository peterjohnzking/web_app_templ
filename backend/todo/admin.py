from django.contrib import admin

# Register your models here.
from .models import Task, Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'completed')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Register your models here.

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)