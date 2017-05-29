# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import settings_js

__author__ = 'beret'

urlpatterns = [
    url(r'common-settings\.js', settings_js, name='js_settings'),
]
