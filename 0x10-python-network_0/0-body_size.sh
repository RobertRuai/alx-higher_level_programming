#!/bin/bash
#displays the size of the body of the response URL
curl -sI "$1" | grep -i 'Content-Length:' | cut -f2 -d ' '
