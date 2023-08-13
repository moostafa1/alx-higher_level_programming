#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    sign_func = {'+':add, '-':sub, '*':mul, '/':div}

    argv = argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[1] not in sign_func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{} {} {} = {}".format(argv[0],
                                     argv[1],
                                     argv[2],
                                     sign_func[argv[1]](int(argv[0]),
                                     int(argv[2]))))
