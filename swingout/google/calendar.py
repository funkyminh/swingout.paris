from apiclient.discovery import build
from django.conf import settings
from google.models import Calendar


class GoogleCalendar(object):

    def __init__(self):
        self.service = build(
            'calendar', 'v3', developerKey=settings.API_GOOGLE)

    def get_calendar_info(self, calendar_id):
        calendar = self.service.calendars().get(calendarId=calendar_id).execute()
        return calendar

    def get_calendar_events(self, calendar_id):
        pageToken = None
        events = self.service.events().list(calendarId=calendar_id,
                                            pageToken=pageToken).execute()
        return events
