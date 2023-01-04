""" 
Q3. Permutation
Given an integer array A of size N denoting collection of numbers , return all possible permutations.
NOTE:
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. 
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.

Problem Constraints
1 <= N <= 9

Input Format
Only argument is an integer array A of size N.

Output Format
Return a 2-D array denoting all possible permutation of the array.

Example Input
A = [1, 2, 3]

Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3] 
  [2, 3, 1] 
  [3, 1, 2] 
  [3, 2, 1] ]

Example Explanation
All the possible permutation of array [1, 2, 3].
"""

def printAllPermute(arr:list,n:int,i:int):
  if (i==n):
    print(arr)
    return
  
  for j in range(i,n):
    arr[i],arr[j]=arr[j],arr[i]
    printAllPermute(arr,n,i+1)
    arr[i],arr[j]=arr[j],arr[i]
    
    
def main():
  arr = [6,9,14]
  n = len(arr)
  printAllPermute(arr,n,0)
  

if __name__ == "__main__":
  main()
  