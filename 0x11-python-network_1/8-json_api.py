#!/usr/bin/python3
""" sends POST request to URL with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    res = requests.post(url, data={'q': q})
    try:
        jsn = res.json()
        if jsn:
            print("[{}] {}".format(jsn.get("id"), jsn.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
