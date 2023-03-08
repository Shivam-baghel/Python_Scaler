"""
Q3. Valid Sudoku
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""


"""
Steps:
Check duplicate value in column, if it is return 0, else continue
Check duplicate value in row, if it is return 0, else continue
Check duplicate value in 9x9 box, if it is return 0, else continue
"""
def isValidSudoku(self, A):
    """This function will be checking, if the provided sudoku puzzle (in the format of a 2D list) is valid or not.

    Args:
        A (2-D List): 2-D list is provided in Arguments in sudoku puzzle format(9X9)

    Returns:
        Boolean: returns a boolean value True or False.
    """
    
    # Row checking
    for i in range(9):
        dic = {}
        count = 0
        for j in range(9):
            if A[i][j] in dic:
                return False
            if A[i][j] != ".":
                dic[A[i][j]] = 1

    #checking Column 

    for i in range(9):
        dic = {}
        count = 0
        for j in range(9):
            if A[j][i] in dic:
                return False
            if A[j][i] != ".":
                dic[A[j][i]] = 1

    #checking each box
    # Remember:
        # After completing each iteration we have to jump 3 to next box which
        # is there index away. That’s why increasing i and j value by 3
        
    for i in range(0,9,3):
        for j in range(0,9,3):
            dic = {}
            for k in range(3):
                for l in range(3):
                    Newi = i+k      #The new box row
                    Newj = j+l      # The new box column
                    if A[Newi][Newj] in dic:
                        return False
                    elif A[Newi][Newj] != ".":
                        dic[A[Newi][Newj]] = 1
    return True

input = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print(isValidSudoku)