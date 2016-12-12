from django.conf.urls import url, include
from django.contrib import admin

import index
import locatorr
from locatorr import views
from . import views

urlpatterns = [
    url(r'^createForm', views.createForm, name='createForm'),
    url(r'^created/', index.views.create, name='create'),
    url(r'^addmembers/(?P<group_id>[0-9]+)', index.views.addmembers, name='addMembers'),
    url(r'^addmember/(?P<group_id>[0-9]+)', index.views.addmember, name='addMember'),
    url(r'^api/welcome$', views.apiwelcome, name='apiwelcome'),
    url(r'^$', views.welcome, name='welcome'),
]
