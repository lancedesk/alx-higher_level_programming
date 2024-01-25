#!/bin/bash
# Takes URL, sends a request & displays response body size
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
