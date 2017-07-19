# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from .views import band, all_bands, BandList, BandDetail, MemberList, MemberDetail, MusicanList, MusicanDetail

__author__ = 'beret'

urlpatterns = [
    url(r'^$', all_bands),
    url(r'(?P<band_id>\d+)/$', band),
]
