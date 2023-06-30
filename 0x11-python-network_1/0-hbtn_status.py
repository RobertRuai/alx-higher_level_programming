#!/usr/bin/python3
"""script that fetches alx status"""

if __name__ == "__main__":
    import urllib.request as req
    with  req.urlopen('https://alx-intranet.hbtn.io/status') as res:
        if res:
            html = res.read()
            print("Body response:")
            print("\t - type: {}".format(type(html)))
            print("\t - content: {}".format(html))
            print("\t - utf8 content: {}".format(html.decode('utf-8')))
