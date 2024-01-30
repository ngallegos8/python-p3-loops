#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while(num > 0):
        print(num)
        num -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # return [i ** 2 for i in int_list]
    new_list = []
    for i in int_list:
        i = i ** 2
        new_list.append(i)
    return(new_list)

print(square_integers([1, 2, 3, 4, 5]))


def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz()
