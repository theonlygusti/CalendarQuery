#!/usr/bin/python
import datetime
import os
import subprocess
import unittest

class CalendarEvent:
    """Represents a macOS calendar event."""
    __allowed_properties = {
            "name": str,
            "location": str,
            "starts": datetime.datetime,
            "ends": datetime.datetime,
            "repeat": datetime.timedelta,
            "end_repeat": datetime.datetime,
            "travel_time": datetime.timedelta,
            "alert": datetime.timedelta,
            "notes": str,
            "invitees": list
            }

    def __init__(self, **keyword_arguments):
        for key, value in keyword_arguments.items():
            if key in self.__allowed_properties:
                if type(value) is self.__allowed_properties[key]:
                    setattr(self, key, value)
                else:
                    raise TypeError("%s must be %s" % (key, str(self.__allowed_properties[key])))
        
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

class TestClasses(unittest.TestCase):
    """Test that the classes defined by this script function correctly."""

    def test_CalendarEvent(self):
        party_tomorrow = CalendarEvent(
                name = "After Prom",
                location = "The big barn",
                starts = datetime.datetime.today() + datetime.timedelta(days = 1),
                ends = datetime.datetime.today() + datetime.timedelta(days = 1, hours = 5),
                travel_time = datetime.timedelta(hours = 1),
                notes = "This is gonna be a load of fun."
                )

