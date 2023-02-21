#!/usr/bin/env python3

#   Write a method `happy_new_year` that outputs numbers starting at 10 and
#    counting down to 1. After reaching 1, print out "Happy New Year!"

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    if i == 1:
        print("Happy New Year!")

#   Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For
#   multiples of three, print "Fizz" instead of the number and for the multiples
#   of five print "Buzz". For numbers which are multiples of both three and five,
#   print "FizzBuzz".

def fizzbuzz_printer():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def square_integers(int_list):
    return [i ** 2 for i in int_list]

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

#   Write a method `reverse_string` that takes one argument, a string, and reverses
#   it. Don't use the built-in `.reverse` method. Instead, loop through the
#   characters in the input string and reverse it.

def reverse_string(string):
    
