"""Json Service 1.0."""
import requests


def get_json(url, header_auth):
    """HTTPBasicAuth is faling,this is another way."""
    r = requests.get(url, headers=header_auth)

    # Convert the response to JSON
    r.headers['content-type']
    r.encoding
    return r.json()
