# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.utils.html import escape
from pygments.lexers import LEXERS
import json
import sys
import traceback
from contextlib import contextmanager
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required

from snippets.models import Snippet

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint


@contextmanager
def catch_stdout(buff):
    stdout = sys.stdout
    sys.stdout = buff
    yield
    sys.stdout = stdout


@csrf_exempt
def snippets(request, id=None):

    print(request.get_full_path())

    if id:
        snippet = Snippet.objects.get(pk=id)

    if request.method == 'POST':
        for key, value in request.POST.items():
            print(key)
            pp(value)
            print('##############################################################################################################################')
        buff = StringIO()
        raw_snippet = request.POST.get('source', '')
        try:
            with catch_stdout(buff):
                exec(raw_snippet)
        except:
            traceback.print_exc(file=buff)
        result = buff.getvalue()
    else:
        result = ''
        raw_snippet = """class ListHtmlFormatter(HtmlFormatter):
    def wrap(self, source, outfile):
        return self._wrap_div(self._wrap_pre(self._wrap_list(source)))
    def _wrap_list(self, source):
        yield 0, '<ol>'
        for i, t in source:
            if i == 1:
                # it's a line of formatted code
                t = '<li><div class="line">%s</div></li>' % t
            yield i, t
        yield 0, '</ol>'
    # a unicode comment: âăşţîÂĂŞŢÎ èéòçàù"""

    snippet = '<pre lang="python">' + escape(raw_snippet) + '</pre>'
    snippet_js = escape(raw_snippet)

    return render_to_response(
        'snippet.html',
        context={
            'snippet': snippet,
            'snippet_js': snippet_js,
            'react_on': True,
            'result': result
        }
    )
