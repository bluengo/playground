#!/usr/bin/env python3

import os

def getUsername():
    username = os.getenv("USER")
    return username

def main():
    message = "Hello, {}!".format(getUsername())
    print(message) 


if __name__ == "__main__":
    try:
        main()
    except:
        os.exit(1)

