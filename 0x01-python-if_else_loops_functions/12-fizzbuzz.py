#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not i % 3 and not i % 5:
            i = "FizzBuzz"
        elif not i % 3:
            i = "Fizz"
        elif not i % 5:
            i = "Buzz"

        if i != 100:
            print(i, end=" ")
        else:
            print(i)
