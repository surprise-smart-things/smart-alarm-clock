from __future__ import print_function

import csv
import datetime
import os.path
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/fitness.activity.read', "https://www.googleapis.com/auth/fitness.sleep.read"]


def get_calendar():
    """
    This function connects the python program to the Google Calendar
    of the user
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service


def get_events(x):
    """
    This function gets the events for a particular day from the calendar
    :param x: The day to be checked
            x => int 0 -> today
                     1 -> tomorrow
                     -1 -> yesterday ...
    """
    # Call the Calendar API
    service = get_calendar()

    now = (datetime.datetime.now() - datetime.timedelta(days=(1 - x))).isoformat() + 'Z'  # 'Z' indicates UTC time
    now = now[:11] + '18:30:00.000000Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=50, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    todayData = []
    event = events[0]
    start = event['start']['dateTime']
    date = event['start'].get('dateTime', event['start'].get('date'))[:10]
    if date == str(datetime.date.today() + datetime.timedelta(days=x)):
        # print(event['summary'])
        todayData = [date, start, event['location']]
    else:
        pass
    # print(events)
    return todayData

# print(get_events(1))

