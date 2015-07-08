"""Json Service 1.0."""
import requests

status_code = None

def get_json(url, header_auth):
    global status_code
    """HTTPBasicAuth is faling,this is another way."""
    r = requests.get(url, headers=header_auth)

    # The statuscode should be 200 if everything is ok
    status_code = r.status_code

    # Convert the response to JSON
    r.headers['content-type']
    r.encoding
    return r.json()
