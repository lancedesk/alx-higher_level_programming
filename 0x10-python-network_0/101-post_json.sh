#!/bin/bash
# Use curl to send a POST request with the contents of the JSON file and display the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
