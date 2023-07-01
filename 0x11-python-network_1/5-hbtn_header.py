#!/usr/bin/python3
"""script that fetches  X-Request-Id variable"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    val = res.headers.get("X-Request-Id")
    print(val)
