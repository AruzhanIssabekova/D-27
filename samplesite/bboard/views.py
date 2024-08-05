from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Task, Comment
from .forms import TaskForm, CommentForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})



def create_task_with_comments(request, task_id=None):
    task = get_object_or_404(Task, id=task_id) if task_id else None
    CommentFormSet = inlineformset_factory(Task, Comment, form=CommentForm, extra=3)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        formset = CommentFormSet(request.POST, instance=task)
        if task_form.is_valid() and formset.is_valid():
            task = task_form.save()
            formset.instance = task
            formset.save()
            return redirect('success')
        else:
            pass
    else:
        task_form = TaskForm(instance=task)
        formset = CommentFormSet(instance=task)

    return render(request, 'formset.html', {'task_form': task_form, 'formset': formset})


def success(request):
    return render(request, 'success.html')
