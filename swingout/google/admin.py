from django.contrib import admin
from google.models import Calendar, Event


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('google_calendar_id', 'summary', 'description')

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Event, EventAdmin)