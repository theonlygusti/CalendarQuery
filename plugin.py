def results(fields, original_query):
    message = fields["~message"]
    html = "Lorem ipsum dolor sit amet"
    return {
        "title": "When '{0}'".format(message),
        "run_args": [message],
        "html": html
    }

def run(query):
    import os
    os.system("open -a Calendar")
