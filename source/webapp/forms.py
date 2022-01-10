from re import S
from django import forms
from django.forms import widgets
from webapp.models import TaskType, Status

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Title')
    description = forms.CharField(max_length=3000, required=False, label='Description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(required=True, label='Status', queryset=Status.objects.all())
    task_type = forms.ModelChoiceField(required=True, label='Type', queryset=TaskType.objects.all())