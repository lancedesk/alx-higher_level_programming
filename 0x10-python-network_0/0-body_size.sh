#!/bin/bash
# Takes in a URL, sends a request to that URL
# Displays the size of the body of the response

# Use curl to get the size of the body and display it
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
