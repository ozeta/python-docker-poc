#!/usr/bin/python
import logging
import requests
import sys, getopt

def main(argv):
    response = requests.get("https://petstore.swagger.io/v2/store/inventory")
    print("status: {}".format(response.status_code))
    print(response.json())
    if len(argv) > 0:
        print("Hello, {}!".format(argv[0]))
    else:
        print("Hello, STD!")
    return
if __name__ == "__main__":
   main(sys.argv[1:])