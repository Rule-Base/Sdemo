from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$',
         'sample_project.views.django_hello_world',
          name='django_home_page'),
     url(r'^django-hello-world/$',
         'sample_project.views.django_hello_world',
          name='django-hello-world'),
)
