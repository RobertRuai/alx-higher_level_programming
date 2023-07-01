#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions and print error codes"""
import requests
import sys

if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        print(res.text)
    except:
        print("Error code: {}".format(res.status_code))
