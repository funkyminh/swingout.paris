from google.calendar import GoogleCalendar


gc = GoogleCalendar()
events = gc.get_calendar_events('{}'.format('7cqclq8acds1p9lirvovfug4lc@group.calendar.google.com'))
print len(events['items'])
for event in events['items']:
    print event['id']
    if 'summary' in event:
        print event['summary']
