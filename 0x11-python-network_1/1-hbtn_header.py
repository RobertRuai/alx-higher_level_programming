#!/usr/bin/python3
"""script that fetches  X-Request-Id variable"""
import sys

if __name__ == "__main__":
    import urllib.request as req
    with req.urlopen(sys.argv[1]) as res:
        if res:
            val = res.headers.get("X-Request-Id")
            print(val)
