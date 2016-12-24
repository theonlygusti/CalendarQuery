#!/usr/bin/python
import subprocess

def results(fields, original_query):
    return {
        "title": "Calendar Query",
        "run_args": [],
        "html": str(fields) + "<br>" + str(original_query)
    }

def run(query):
    import os
    os.system("open -a Calendar")
