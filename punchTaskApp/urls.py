from django.conf.urls import patterns, include, url
from django.contrib import admin

from punchTaskApp.home.views import HomePage
from punchTaskApp.tasks.views import TaskList

urlpatterns = patterns('',
    # Initial page
                       url(r'^$', HomePage.as_view(), name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
                       url(r'^signup/$',
                           'punchTaskApp.contributors.views.contributor_new', name = 'cont_new'
                       ),
                       url(r'^task/list/$', TaskList.as_view(), name='task_list'),
                       (r'^admin/', include(admin.site.urls)),
)
