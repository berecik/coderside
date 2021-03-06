# -*- coding: utf-8 -*-

import pprint
import json
import os

__author__ = 'beret'


try:
    from django.conf import settings
    BASE_DIR = settings.BASE_DIR
    DEBUG_FILE = getattr(settings, 'DEBUG_FILE', os.path.join(BASE_DIR, '_debug_log.log'))
except ImportError:
    BASE_DIR = os.path.join(os.path.abspath(__file__), '..')
    DEBUG_FILE = os.path.join(BASE_DIR, '_debug_log.log')

_cout = True
_pp = pprint.PrettyPrinter(indent=2)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def try_int(data, default=None):
    try:
        if isinstance(data, (list, tuple)):
            return try_int(data[0], default)
        return int(data)
    except:
        return default


def _get_write(f):
    if f:
        if f == True:
            _debug_file = open(DEBUG_FILE, 'a')
        else:
            _debug_file = f
        return _debug_file.write
    return False


def get_pp(*args, **kwargs):
    def __pp(data):
        return pp(data, *args, **kwargs)
    return __pp


def pp(txt, parse=None, cout=_cout, f=True, string=None):
    if string==None:
        string = not cout
    if parse == 'json':
        _txt = json.loads(txt)
    elif parse:
        _txt = parse(txt)
    else:
        _txt = txt
    w = _get_write(f)
    if w:
        w(_txt)
    if cout:
        _pp.pprint(_txt)
    if string:
        return _pp.pformat(_txt)


def p(parse=None, cout=_cout, f=True, **kwargs):
    def __pp(*txts):
        for txt in txts:
            pp(txt=txt, parse=parse, cout=cout, f=f, **kwargs)
    return __pp


def jprint(json_txt, f=False):
    if f:
        cout = False
    else:
        cout = True
    return pp(txt=json_txt, parse='json', cout=cout, f=f)


def del_key(dict, key):
    if key in dict:
        del dict[key]
        return True
    return False


def env(fun):
    def _fun_wrap(*args, **kwargs):
        import os
        import sys

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coderside.settings")
        sys.path.append(BASE_DIR)

        return fun(*args, **kwargs)

    return _fun_wrap
