#!/bin/bash
# Use curl to send a GET request & display the body if status code is 200
curl -sfL "$1" -X GET
