import numpy as np


def fib(n):
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, len(dp)):

        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

if __name__ == '__main__':

    print(fib(6)) 
    # 0 1 1 2 3 5 8 
    # complexity O(min(n,m))
