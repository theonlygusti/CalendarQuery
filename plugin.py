#!/usr/bin/python
import datetime
import os
import subprocess
import unittest

class CalendarEvent:
    """Represents a macOS calendar event."""
    def __init__(self, **keyword_arguments):
        self.__allowed_properties = ["starts", "ends", "repeat", "end_repeat", "travel_time", "alert", "notes", "invitees"]
        for key, value in keyword_arguments:
            if key in self.__allowed_properties:
                setattr(self, key, value)
        
def find_time_of_event(event):
    """Return a CalendarEvent with properties associated with the unparsed user-inputted string event."""
    return CalendarEvent(
            starts=datetime.datetime.now(),
            ends = datetime.datetime.now() + datetime.timedelta(hours = 1),
            repeat = datetime.timedelta(days = 1),
            end_repeat = datetime.datetime(year = 2017, month = 12, day = 31),
            travel_time = datetime.timedelta(minutes = 20),
            alert = datetime.timedelta(minutes = 20),
            notes = "just a single-line string",
            invitees = []
            )

def find_events_of(period):
    """Return a list of CalendarEvent which occurr within the given, unparsed user-inputted time period."""
    return [CalendarEvent()]

def results(fields, original_query):
    if original_query.lower().startswith("when is"):
        find_time_of_event(fields["~event"])
    if original_query.lower().startswith("what time is"):
        find_time_of_event(fields["~event"])
    elif original_query.lower().startswith("what do I have"):
        find_events_of(fields["~period"])
    return {
        "title": "Calendar Query",
        "run_args": [],
        "webview_transparent_background": True,
        "html": str(fields) + "<br>" + str(original_query)
        }

def run(query):
    os.system("open -a Calendar")
