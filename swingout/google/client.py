from oauth2client import client
from django.conf import settings
import os

CLIENT_SECRETS = os.path.join(os.path.dirname(
    __file__), 'client_id.json')

print CLIENT_SECRETS

FLOW = client.flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar.readonly',
    redirect_uri='http://localhost:8000/oauth2callback')

auth_uri = FLOW.step1_get_authorize_url()
credentials = FLOW.step2_exchange(auth_code)
