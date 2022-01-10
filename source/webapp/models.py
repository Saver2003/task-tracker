from django.db import models
from django.db.models.deletion import PROTECT

class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=3000, null=False, blank=True, verbose_name='Description')
    status = models.ForeignKey('webapp.Status', related_name='Task', on_delete=PROTECT, verbose_name='Status')
    task_type = models.ForeignKey('webapp.TaskType', related_name='Type', on_delete=PROTECT, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.pk, self.title, self.status, self.task_type)

class Status(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')

    def __str__(self) -> str:
        return "{}".format(self.title)

class TaskType(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')

    def __str__(self) -> str:
        return "{}".format(self.title)
