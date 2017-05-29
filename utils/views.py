# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.conf import settings

from coderside import common_settings

__author__ = 'beret'


def settings_js(request):
    _settings = {}
    _settings_names = dir(common_settings)
    for _name in _settings_names:
        if _name[0] != '_' and _name[0].isupper():
            _settings[_name] = getattr(settings, _name, None)
    context = {
        "settings_dir": json.dumps(_settings)
    }
    response = render(request, "utils/settings.js", context)
    return response
