#!/usr/bin/env python
# encoding: utf-8

"""
@author: david
@time: 5/25/17 5:44 PM
"""

from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]