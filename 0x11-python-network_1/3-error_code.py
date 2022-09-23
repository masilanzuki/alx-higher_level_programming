#!/usr/bin/python3
'''
Take in a URL, send a request to URL, and display body of response in utf-8.
Manager urllib's error exceptions.
'''
import sys
from urllib import request
from urllib import error

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.URLError as e:
        print(f"Error code: {e.code}")
