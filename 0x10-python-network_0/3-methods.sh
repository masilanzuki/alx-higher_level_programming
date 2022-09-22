#!/bin/bash
# takes in URL and displays all HTTP methods the server wull accept.
curl -sI | grep Allow | cut -d " " -f2-
