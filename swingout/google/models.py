from __future__ import unicode_literals

from django.db import models


class Calendar(models.Model):    
    google_calendar_id = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs):
    	self.summary = 'test'
    	super(Calendar, self).save(*args, **kwargs)