from django.conf.urls import patterns, include, url
from django.contrib import admin

from punchTaskApp.home.views import HomePage

urlpatterns = patterns('',
    # Initial page
                       url(r'^$', HomePage.as_view(), name='home'),
                       url(r'^signup/$',
                           'punchTaskApp.contributors.views.contributor_new', name = 'cont_new'
                       ),
                       (r'^admin/', include(admin.site.urls)),
)
