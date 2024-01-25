#!/bin/bash
# Use curl to send a POST request with specified parameters and display the body
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
