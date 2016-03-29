import json
import webbrowser
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from django.conf import settings


CLIENT_SECRETS = os.path.join(os.path.dirname(
    __file__), 'client_secret_terminal.json')

FLOW = client.flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar.readonly',
    redirect_uri='http://localhost:8000/oauth2callback')

credentials = tools.run_flow(FLOW)
print credentials