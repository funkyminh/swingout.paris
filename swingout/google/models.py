from __future__ import unicode_literals

from django.db import models
from google.calendar import GoogleCalendar

gc = GoogleCalendar()


class Calendar(models.Model):
    google_calendar_id = models.CharField(max_length=200)

    def get_summary(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        if 'summary' in events:
            return events['summary']
        else:
            return None

    def get_description(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        if 'description' in events:
            return events['description']
        else:
            return None

    def get_number_events(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        return len(events['items'])

    def list_events(self):
        events = gc.get_calendar_events('{}'.format(self.google_calendar_id))
        return events['items']
