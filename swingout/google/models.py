from __future__ import unicode_literals

from django.db import models
from google.calendar import GoogleCalendar


class Calendar(models.Model):
    google_calendar_id = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)    

    def save(self, *args, **kwargs):
        gc = GoogleCalendar()
        try:
            calendar = gc.get_calendar_events('{}'.format(self.google_calendar_id))
            self.summary = calendar['summary']
            self.description = calendar['description']            
        except:
            pass
        super(Calendar, self).save(*args, **kwargs)


class Event(models.Model):
    google_event_id = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    html_link = models.CharField(max_length=300)
    summary = models.CharField(max_length=200)
    calendar = models.ForeignKey(Calendar)