#!/bin/bash
# Use curl to make a request that causes the server to respond with "You got me!"
curl -sLX PUT -d 'user_id=98' -H 'Origin:School' "0.0.0.0:5000/catch_me"
