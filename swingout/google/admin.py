from django.contrib import admin
from google.models import Calendar


class CalendarAdmin(admin.ModelAdmin):
    list_display = ('google_calendar_id', 'summary', 'description')


admin.site.register(Calendar, CalendarAdmin)
