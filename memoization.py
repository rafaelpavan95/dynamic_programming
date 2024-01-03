import numpy as np


def fact(n):

    if n == 1:
        return 1
    
    else:
        return n*fact(n-1)
    

def fib(n, lookup=None):
    
    lookup = {} if lookup is None else lookup

    if n in lookup:

        return lookup[n]
    
    if n == 1:
        return 1
    
    elif n == 0: 
        return 0
    
    else:

        lookup[n] = fib(n-1)+fib(n-2)

        return lookup[n]



if __name__ == '__main__':

    print(fib(6)) 
    # 0 1 1 2 3 5 8 
    # complexity O(n)