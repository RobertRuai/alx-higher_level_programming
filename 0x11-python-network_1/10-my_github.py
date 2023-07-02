#!/usr/bin/python3
"""
sends  ID get request to githubAPI
with the username,password as a parameters
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    url = ' https://api.github.com/user'
    uname = sys.argv[1]
    pswd = sys.argv[2]
    res = requests.get(url, auth=HTTPBasicAuth(uname, pswd))
    jsn = res.json()
    print(jsn.get('id'))
