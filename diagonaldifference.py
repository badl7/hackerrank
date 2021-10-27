"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix

is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal =1+5+9=15
. The right to left diagonal =3+5+9=17 . Their absolute difference is |15 - 17|=2. """

def diagonal(arr):
    lsum = 0
    rsum = 0
    i = 0
    for x in range(0,len(arr)):
        lsum += arr[x][x]
        rsum += arr[x][len(arr)-1- x]
    return abs(lsum - rsum)
arrs = [[1, 2, 3],[4, 5, 6],[9, 8, 9]]
print(diagonal(arrs))