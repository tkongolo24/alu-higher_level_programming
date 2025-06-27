#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Get command line arguments (excluding the script name)
    argv = sys.argv[1:]
    argc = len(argv)
    
    # Print number of arguments with proper grammar
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print(f"{argc} arguments:")
    
    # Print each argument with its position
    for i in range(argc):
        print(f"{i + 1}: {argv[i]}")
