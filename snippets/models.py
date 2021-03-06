from django.db import models

import hashlib

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    @property
    def edition(self):
        return Edition.objects.filter(snippet=self).last()

    @property
    def hash(self):
        return self.edition.hash

    @property
    def source(self):
        return self.edition.source

    @source.setter
    def source(self, source):
        hl = hashlib.md5()
        hl.update(source.encode('utf-8'))
        _hash = hl.hexdigest()
        Edition.objects.create(hash=_hash, snippet=self, source=source)


class Edition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=64, db_index=True)
    source = models.TextField()
    snippet = models.ForeignKey(Snippet)
