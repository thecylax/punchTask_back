from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
            task_list = Task.objects.filter(product__icontains=a, assignee=self.request.user)
        else:
            task_list = Task.objects.filter(assignee=self.request.user)
        return task_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskList, self).dispatch(*args, **kwargs)

@login_required()
def task_detail(request, ticket):
    task = Task.objects.get(ticket=ticket)
    if task.assignee != request.user:
        return HttpResponseForbidden()
    context = {'task': task,}

    return render(request, 'tasks/task_detail.html', context)

@login_required()
def task_cru(request, ticket=None):

    if ticket:
        task = get_object_or_404(Task, ticket=ticket)
        if task.assignee != request.user:
            return HttpResponseForbidden()
    else:
        task = Task(assignee=request.user)
        try:
            max_ui = Task.objects.latest('ticket').ticket
        except Task.DoesNotExist:
            max_ui = 0

    if request.POST:
        form = TaskForm(request.POST, instance=task)
        print ">> entrou"
        if form.is_valid():
            task = form.save(commit=False)
            print ">> valid"
            if not ticket:
                task.ticket = max_ui + 1
            task.assignee = request.user
            print ">> before save"
            task.save()
            print ticket
            redirect_url = reverse('punchTaskApp.tasks.views.task_detail', args=(task.ticket,))
            
            return HttpResponseRedirect(redirect_url)
    else:
        print ">> no post"
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    
    if request.is_ajax():
        template = 'tasks/task_item_form.html'
    else:
        template = 'tasks/task_cru.html'
    return render(request, template, context)
