from django.conf.urls import patterns, url

task_urls = patterns('',
                     url(r'^$',
                         'punchTaskApp.tasks.views.task_detail', name='task_detail'
                     ),
                     url(r'^edit/$',
                         'punchTaskApp.tasks.views.task_cru', name='task_update'
                     ),
            )
