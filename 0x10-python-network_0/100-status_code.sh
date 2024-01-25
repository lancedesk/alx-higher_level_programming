#!/bin/bash
# Use curl to send a request and write the status code to a file
curl -s -o /dev/null -w "%{http_code}" "$1"
