#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
