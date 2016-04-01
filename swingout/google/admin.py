from django.contrib import admin
from google.models import Calendar


class CalendarAdmin(admin.ModelAdmin):
    #list_display = ('google_calendar_id', 'summary', 'description', 'number_events', )
    list_display = ('google_calendar_id', 'summary', 'number_events')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        calendar = Calendar.objects.get(pk=object_id)
        extra_context['data'] = calendar.list_events()
        return super(CalendarAdmin, self).change_view(request, object_id,
                                                      form_url, extra_context=extra_context)

    def summary(self, obj):
        return obj.get_summary()['summary']

    def description(self, obj):
        return obj.get_description()

    def number_events(self, obj):
        return obj.get_summary()['length']


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Calendar, CalendarAdmin)
