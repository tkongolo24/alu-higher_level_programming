#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    argc = len(argv)
    
    # Print number of arguments
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    
    # Print each argument with position
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))


if __name__ == "__main__":
    main()
