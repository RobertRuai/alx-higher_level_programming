#!/bin/bash
#displays the status response from request
curl -o /dev/null -w '%{http_code}' -sI "$1"
