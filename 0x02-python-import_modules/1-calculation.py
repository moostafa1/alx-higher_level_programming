#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

sign_func = {'+': add, '-': sub, '*': mul, '/': div}

for op in sign_func:
    print(f"{a} {op} {b} = {sign_func[op](a, b)}")
