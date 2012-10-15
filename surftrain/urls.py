# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from surftrain.views import home

urlpatterns = patterns('surftrain.views',
    url(r'',home),
)
