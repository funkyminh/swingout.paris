from django.views.generic import TemplateView
from google.models import Calendar


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['calendars'] = Calendar.objects.all()
        return context


class CalendarView(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        calendar = Calendar.objects.get(id=kwargs['calendar_id'])
        context = super(CalendarView, self).get_context_data(**kwargs)        
        context['events'] = calendar.list_events()
        return context

class EventView(TemplateView):
    template_name = 'all_events.html'

    def get_context_data(self, **kwargs):
        calendar = Calendar()
        context = super(EventView, self).get_context_data(**kwargs)        
        context['events'] = calendar.list_all_events()
        return context    