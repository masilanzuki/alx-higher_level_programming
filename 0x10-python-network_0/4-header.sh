#!/bin/bash
# curl takes URL sends GET request and displays the body of the response
#displays header x-school-user-id with a value 98
curl -sH "X-School-User-Id:98" "$1"
