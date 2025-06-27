#!/usr/bin/python3

import sys

if __name__ == "__main__":
    
    argc = len(argv)
    
   
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))
