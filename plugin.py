#!/usr/bin/python
import subprocess

def find_time_of_event(event):
    return "tomorrow"

def find_events_of(period):
    return "tomorrow"

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
    import os
    os.system("open -a Calendar")
