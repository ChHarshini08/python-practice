def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=3
print(factorial(n))


def fib_series(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_series(n-1) + fib_series(n-2)

n=2
print(fib_series(n))


import math
def is_prime(n):
    if n<=0:
        return 'Invalid'
    for i in range(2, int((n**0.5)+1)):
        if n%i==0:
            return False
    return True
n=15 
print(is_prime(n))


   

