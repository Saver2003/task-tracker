from django.contrib import admin
from webapp.models import Task, TaskType, Status

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'task_type']
    list_filter = ['title', 'status', 'task_type']
    search_field = ['title']
    fields = ['title', 'status', 'description', 'task_type']
    readonly_fields = ['created_at', 'updated_at']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    search_field = ['title']
    fields = ['title']

admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(TaskType)
