# function to calculate diagonal difference
def diagonalDifference(arr):
    leftDiagonal = 0
    rightDiagonal = 0

    for n in range(len(arr)):
        leftDiagonal += arr[n][n]

    for m in range(len(arr)):
        rightDiagonal += arr[m][len(arr) - 1 - m]

    # return absolute difference
    return abs(leftDiagonal - rightDiagonal)





