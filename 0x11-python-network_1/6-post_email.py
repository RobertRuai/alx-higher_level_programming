#!/usr/bin/python3
""" sends POST request to URL with the email as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    res = requests.post(url, data=val)
    print(res.text)
