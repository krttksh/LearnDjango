"""
Definition of urls for BasicProject.
"""

#from datetime import datetime
#from django.conf.urls import url
#import django.contrib.auth.views

#import app.forms
#import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls import include,url
import HelloDjangoApp.views

urlpatterns = [
    url(r'^$',HelloDjangoApp.views.index,name='index'),
    url(r'^home$',HelloDjangoApp.views.index,name='home'),
    ]
