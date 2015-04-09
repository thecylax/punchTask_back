from django.conf.urls import patterns, include, url
from django.contrib import admin

from punchTaskApp.home.views import HomePage

urlpatterns = patterns('',
    # Initial page
                       url(r'^$', HomePage.as_view(), name='home'),
   #                    url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', HomePage.as_view(), name='sub_new'),
)
