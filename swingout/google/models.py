from __future__ import unicode_literals

from django.db import models
from google.calendar import GoogleCalendar
from django.core.cache import cache

gc = GoogleCalendar()


class Calendar(models.Model):
    google_calendar_id = models.CharField(max_length=200)

    def get_summary(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        if 'summary' in events:
            # return cache.get_or_set("summary_{}".format(self.id), {'summary':
            # events['summary'], 'length': len(events['items'])}, 3600)
            return {'summary': events['summary'], 'length': len(events['items'])}
        else:
            return None

    def get_description(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        if 'description' in events:
            return events['description']
        else:
            return None

    def list_events(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        return events['items']

    def list_all_events(self):
        calendars = Calendar.objects.all()
        for calendar in calendars:
            return calendar.list_events()
