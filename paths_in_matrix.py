"""


Paths in matrix (problem)

Given a matrix where a cell has the value of 1 if it's a wall and 0 if not, find the number of ways to go from the top-left cell to the bottom-right cell, knowing that it's not possible to pass from a wall and we can only go to the right or to the bottom


Example:

input:
matrix = [
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

output: 7

"""





def paths(matrix, i=0, j=0, lookup=None):

    lookup = {} if lookup is None else lookup 

    n, m = len(matrix), len(matrix[0])

    if (i, j) in lookup:

        return lookup[(i, j)]
    
    if i == n or j == m or matrix[i][j] == 1:
    

        return 0
    
    elif i == n-1 and j == m-1:
    

        return 1
    
    else:

        lookup[(i, j)] = paths(matrix, i+1, j, lookup) + paths(matrix, i, j+1, lookup)
        return lookup[(i, j)]
    

def paths(matrix):
    n, m = len(matrix), len(matrix[0])
    prev_dp = [0]*m
    dp = [0]*m    
    prev_dp[0] = 1 if (matrix[0][0] == 0) else 0
    for j in range(1, m):
        prev_dp[j] = prev_dp[j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[0] = prev_dp[0] if matrix[i][0] == 0 else 0
        for j in range(1, m):
            dp[j] = prev_dp[j] + dp[j-1] if matrix[i][j] == 0 else 0
        prev_dp = dp
        dp = [0]*m
    return prev_dp[m-1]


if __name__ == '__main__':


    matrix = [
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0]
    ]

    print(paths(matrix, i=0, j=0, lookup=None))
   