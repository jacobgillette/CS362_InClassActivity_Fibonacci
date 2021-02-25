import unittest


def fib(n):
    #Error handle
    if n < 0:
        print("Please Enter a correct input")
    #base case
    elif n == 1:
        return 0
    #base cases
    elif n == 1 or n == 2:
        return 1
    #recursive return
    else:
        return (fib(n-1)+fib(n-2))

#Simple factorial function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
