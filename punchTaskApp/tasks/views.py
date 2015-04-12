from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from punchTaskApp.tasks.models import Task

class TaskList(ListView):
    model = Task
    paginate_by = 12
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        task_list = Task.objects.filter(owner=self.request.user)
        return task_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskList, self).dispatch(*args, **kwargs)
