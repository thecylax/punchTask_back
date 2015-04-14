from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from punchTaskApp.tasks.models import Task
from punchTaskApp.tasks.forms  import TaskForm

class TaskList(ListView):
    model = Task
    paginate_by = 12
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        try:
            a = self.request.GET.get('task',)
        except KeyError:
            a = None
        if a:
            task_list = Task.objects.filter(name__icontains=a, owner=self.request.user)
        else:
            task_list = Task.objects.filter(owner=self.request.user)
        return task_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskList, self).dispatch(*args, **kwargs)

@login_required()
def task_detail(request, uid):
    task = Task.objects.get(uid=uid)
    if task.owner != request.user:
        return HttpResponseForbidden()
    context = {'task': task,}

    return render(request, 'tasks/task_detail.html', context)

@login_required()
def task_cru(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            redirect_url = reverse('punchTaskApp.tasks.views.task_detail', args=(task.uid,))
            
            return HttpResponseRedirect(redirect_url)
        else:
            form = TaskForm()

        context = {'form': form,}
        template = 'tasks/task_cru.html'

        return render(request, template, context)
