#!/usr/bin/python3
""" sends POST request to URL with the email as a parameter"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        if res:
            html = res.read()
            print(html.decode('utf-8'))
