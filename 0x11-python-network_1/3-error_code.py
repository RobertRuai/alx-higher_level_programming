#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions and print error codes"""
import urllib.error
import sys

if __name__ == "__main__":
    import urllib.request as req
    try:
        with req.urlopen(sys.argv[1]) as res:
            if res:
                val = res.read()
                print(val.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
