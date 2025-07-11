from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TODOAPP

def delete_task(request, task_id):
    task = get_object_or_404(TODOAPP, id=task_id)
    task.delete()
    return redirect('home')

def complete_task(request, task_id):
    task = get_object_or_404(TODOAPP, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def reactivate_task(request, task_id):
    task = get_object_or_404(TODOAPP, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def home(request):
    # Handle POST request for adding new task
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            TODOAPP.objects.create(task_name=task_name)
        return redirect('home')
    
    # Get tasks from database
    active_tasks = TODOAPP.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = TODOAPP.objects.filter(is_completed=True).order_by('-updated_at')
    
    context = {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)