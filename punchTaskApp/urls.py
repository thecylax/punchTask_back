from django.conf.urls import patterns, include, url
from django.contrib import admin

from punchTaskApp.home.views import HomePage
from punchTaskApp.tasks.views import TaskList
from punchTaskApp.tasks.urls import task_urls

urlpatterns = patterns('',
    # Initial page
                       url(r'^$', HomePage.as_view(), name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
                       url(r'^signup/$', 'punchTaskApp.contributors.views.contributor_new', name = 'cont_new'),
                       
                       url(r'^task/list/$', TaskList.as_view(), name='task_list'),
                       url(r'^task/new/$', 'punchTaskApp.tasks.views.task_cru', name='task_new'),
                       url(r'^task/(?P<uid>[\w-]+)/', include(task_urls)),
                       
                       (r'^admin/', include(admin.site.urls)),
)
