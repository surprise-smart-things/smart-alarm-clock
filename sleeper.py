from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from google.auth.transport.requests import AuthorizedSession

import datetime
import csv

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read', "https://www.googleapis.com/auth/fitness.sleep.read"]


def convertN2D(time_in_nanos):
    return datetime.datetime.fromtimestamp(time_in_nanos / 1000000000.0)


def convertM2D(time_in_millis):
    return datetime.datetime.fromtimestamp(time_in_millis / 1000.0)


def fitapi(day):
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
    t = day
    date = datetime.datetime.today().strftime("%Y-%m-%d-") + "20:00"
    date = datetime.datetime.strptime(date, "%Y-%m-%d-%H:%M")
    try:
        authed_session = AuthorizedSession(creds)
        body = {
                  "aggregateBy": [
                    {
                      "dataTypeName": "com.google.sleep.segment"
                    }
                  ],
                  "endTimeMillis": int((date - datetime.timedelta(days=t) - datetime.datetime.utcfromtimestamp(0)).total_seconds()*1000),
                  "startTimeMillis": int((date - datetime.timedelta(days=t+1) - datetime.datetime.utcfromtimestamp(0)).total_seconds()*1000)
                }
        response = authed_session.post(
            url='https://fitness.googleapis.com/fitness/v1/users/me/dataset:aggregate', json=body)
        sleep = response.json()
        return sleep["bucket"][0]["dataset"][0]["point"]

    except HttpError as err:
        print(err)


def sleepcal(day):
    sleep = fitapi(day)
    light = 0
    deep = 0
    for i in sleep:
        if i['value'][0]['intVal'] == 4:
            light += (int(i['endTimeNanos']) - int(i['startTimeNanos']))/1000000000
        elif i['value'][0]['intVal'] == 5:
            deep += (int(i['endTimeNanos']) - int(i['startTimeNanos']))/1000000000
    if not sleep: return ()
    date = datetime.datetime.today().strftime("%Y-%m-%d-") + "20:00"
    date = datetime.datetime.strptime(date, "%Y-%m-%d-%H:%M") - datetime.timedelta(days=day+1)
    start = convertN2D(int(sleep[0]['startTimeNanos'])) - date
    end = convertN2D(int(sleep[-1]['endTimeNanos'])) - date

    return light, deep, start.seconds, end.seconds


if __name__ == '__main__':
    print(sleepcal(0))