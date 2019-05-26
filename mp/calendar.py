# pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client httplib2
# python3 add_event.py --noauth_local_webserver

# Reference: https://developers.google.com/calendar/quickstart/python
# Documentation: https://developers.google.com/calendar/overview

# Be sure to enable the Google Calendar API on your Google account by following the reference link above and
# download the credentials.json file and place it in the same directory as this file.

from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class Calendar:
    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = "https://www.googleapis.com/auth/calendar"
        self.store = file.Storage("token.json")
        self.creds = self.store.get()
        if(not self.creds or self.creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", self.SCOPES)
            self.creds = tools.run_flow(flow, self.store, noauth_local_webserver=True)
        self.service = build("calendar", "v3", http=self.creds.authorize(Http()))

    def main(self):
        """
        Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user"s calendar.
        """

        # Call the Calendar API.
        now = datetime.utcnow().isoformat() + "Z" # "Z" indicates UTC time.
        print("Getting the upcoming 10 events.")
        events_result = self.service.events().list(calendarId = "primary", timeMin = now,
            maxResults = 10, singleEvents = True, orderBy = "startTime").execute()
        events = events_result.get("items", [])

        if(not events):
            print("No upcoming events found.")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    def insert(self, lmsuserid: str, bookid: str, title: str, author: str):
        today = datetime.now()
        due_date = (today + timedelta(days = 14)).strftime("%Y-%m-%d")
        time_start = "{}T06:00:00+10:00".format(today)
        time_end = "{}T17:00:00+10:00".format(due_date)
        event = {
            "summary": "Return Book: [" + bookid + "] " + title + " - " + author,
            "location": "PIOT Smart Library",
            "description": "Borrower ID: " + lmsuserid,
            "start": {
                "dateTime": time_start,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "attendees": [
                { "email": "piots3666994@gmail.com" },
            ],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    { "method": "email", "minutes": 5 },
                    { "method": "popup", "minutes": 10 },
                ],
            }
        }

        event = self.service.events().insert(calendarId = "primary", body = event).execute()
        print("Event created: {}".format(event.get("htmlLink")))

