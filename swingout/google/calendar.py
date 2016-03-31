from apiclient.discovery import build
from django.conf import settings


class GoogleCalendar(object):

    def __init__(self):
        self.service = build(
            'calendar', 'v3', developerKey=settings.API_GOOGLE)

    def get_calendar_events(self, calendar_id):
        pageToken = None
        maxResults = 2500
        events = self.service.events().list(calendarId=calendar_id,
                                            pageToken=pageToken, maxResults=maxResults).execute()
        return events

