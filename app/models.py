from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Note(models.Model):
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, blank=True, null=True)
    additional_tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='add_notes')
