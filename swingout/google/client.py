from oauth2client import client
from django.conf import settings
import os

flow = client.flow_from_clientsecrets(
    settings.API_JSON,
    scope='https://www.googleapis.com/auth/calendar.readonly',
    redirect_uri='http://www.example.com/oauth2callback')

auth_uri = flow.step1_get_authorize_url()
credentials = flow.step2_exchange(auth_code)