#!/bin/bash
#displays the body of the response URL from POST request
curl -s "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
