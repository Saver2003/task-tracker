from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import Task
from webapp.forms import TaskForm

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'index.html', context)


class SingleTaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

class CreateTaskView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data.pop('status'),
                task_type=form.cleaned_data.pop('task_type')
            )
            print(task)
            return redirect('task', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})

class UpdateTaskView(TemplateView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'task_type': task.task_type,
            'status': task.status
        })
        return render(request, 'update.html', context={'task': task, 'form': form})
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.task_type = form.cleaned_data['task_type']
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('task', pk=task.pk)
        else:
            return render(request, 'update.html', context={'task': task, 'form': form})

class DeleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        print(request.method)
        print(pk)
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')