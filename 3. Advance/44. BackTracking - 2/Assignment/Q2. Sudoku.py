""" 
Q2. Sudoku
Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.

A sudoku puzzle,
Note : sudoku image is provide please do check
and its solution numbers marked in red.

Problem Constraints
N = 9

Input Format
First argument is an array of array of characters representing the Sudoku puzzle.

Output Format
Modify the given input to the required answer.

Example Input
Input 1:

A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]

Example Output
Output 1:
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]

Example Explanation
Explanation 1:
Look at the diagrams given in the question.

"""
global ans 
ans = []

def valid(arr,row,col,value):
    
    #iterate on that respective column

    for i in range(9):
        if arr[i][col]== value:
                return False

    #iterate on that respective row

    for column in range(9):
        if arr[row][column] == value:
                return False

    # check the cube in which that cell lies
    x = row-(row%3)
    y = col-(col%3)
    for i in range(x,x+3):
        for j in range(y,y+3):
            if arr[i][j] == value:
                return False

    # returning True if there is no queen in either of the above checked direction.
    return True

def add_solution(arr):
    curr_list = []
    
    for row in range(len(arr)):
        sol = ""
        for col in range(len(arr)):
            val = arr[row][col]
            # if val == 0:
            #     sol+='.'
            # else:
            sol+=str(val)
        curr_list.append(sol)

    ans.append(curr_list)
    return

def sudoku(mat, i):
    if i == 81:
        add_solution(mat)
        return
    
    # at pos i 
    # cell at mat[row][col]
    row = i//9
    col = i%9
    
    if mat[row][col] != 0:  # cell is already filled
        sudoku(mat,i+1)     # go to next unfilled cell
    else:   # cell is not filled
        
        for j in range(1,10):
            # at cell mat[row][col] == j
            # check if we can place j at mat[row][col]
            
            if valid(mat,row,col,j):
                mat[row][col] = j
                sudoku(mat,i+1)
                mat[row][col] = 0
    
    return
""" 
MY Approach:
accepting the matrix.
giving the matrix the to sudoku function with 0th pos.
sudoku function considers matrix a single list having 81 cells.
get row and column number through cell index or the position provided in the sudoku function
check if cell is filled or not if filled move to next cell by updating the position by 1 and giving to sudoku function.
if cell is not filled. create a loop going through 1 to 9 and check for each value, if value is valid or not. to insert
if yes then updated the position and go tho the next cell. if anything goes wrong backtrack.

"""
def main():

    array = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    sudoku(array,0)
    print(ans)
    

if __name__ == "__main__":
    main()