# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from .views import snippets

__author__ = 'beret'

urlpatterns = [
    url(r'^$', snippets),
]
