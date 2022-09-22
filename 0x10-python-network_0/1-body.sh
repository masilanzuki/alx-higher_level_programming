#!/bin/bash
#takes in URL , sends a GET reqeust to the URL, and displays the body of the response
curl -sfL "$1" -X GET
