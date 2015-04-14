from django.conf.urls import patterns, url

task_urls = patterns('',
                     url(r'^$',
                         'punchTaskApp.tasks.views.task_detail', name='task_detail'
                     ),
            )
