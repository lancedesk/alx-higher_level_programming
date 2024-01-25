#!/bin/bash
# Takes in a URL, sends a request to that URL
# Displays the size of the body of the response

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to get the size of the body and display it
size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')
echo "$size"
