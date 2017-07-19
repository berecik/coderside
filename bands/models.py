from django.db import models
from datetime import date

YEARS = [(None, '...')]
YEARS += [(year, str(year)) for year in range(1955, date.today().year+10)]


class Musican(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    start = models.IntegerField(choices=YEARS, null=True, blank=True)
    end = models.IntegerField(choices=YEARS, null=True, blank=True)
    members = models.ManyToManyField(Musican, through='Member')

    def __str__(self):
        return self.name


class Member(models.Model):
    musican = models.ForeignKey(Musican)
    band = models.ForeignKey(Band)
    instrument = models.CharField(max_length=255)
    start = models.IntegerField(choices=YEARS, null=True, blank=True)
    end = models.IntegerField(choices=YEARS, null=True, blank=True)

    def __str__(self):
        return " ".join([self.musican, self.band, self.instrument])
