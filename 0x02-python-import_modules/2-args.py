#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argv = argv[1:]
    if len(argv) == 0:
        print("{} arguments.".format(len(argv)))
    elif len(argv) == 1:
        print("{} argument:\n1: {}".format(len(argv), argv[0]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i+1, argv[i]))
