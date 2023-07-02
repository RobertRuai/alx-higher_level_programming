#!/usr/bin/python3
"""
sends commit get request to githubAPI
with the username,repo_name as a parameters
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    res = requests.get(url)
    jsn = res.json()
    for commit in jsn[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
