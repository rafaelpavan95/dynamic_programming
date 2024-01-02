import numpy as np


def fact(n):

    if n == 1:

        return 1
    
    else:

        return n*fact(n-1)
    

def fib(n):

    if n == 1:

        return 1
    
    elif n == 0: 

        return 0
    
    else:

        return fib(n-1)+fib(n-2)
    



if __name__ == '__main__':

    print(fact(3)) 
    # 3! = 3*2 = 6
    # complexity O(n!)

    print(fib(6)) 
    # 0 1 1 2 3 5 8 
    # complexity O(phi^n)