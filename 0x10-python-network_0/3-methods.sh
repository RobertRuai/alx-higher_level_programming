#!/bin/bash
#displays the available methods of the response URL
curl -sI "$1" | grep -i 'Allow:' | cut -f2- -d ' '
