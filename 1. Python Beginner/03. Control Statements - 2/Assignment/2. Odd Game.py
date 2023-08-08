""" 
Q2. Odd Game
Write a program to print all odd numbers from 1 to N where you have to take N as input from user. Here N is inclusive.

Problem Constraints
1 <= N <= 2000000

Input Format
A single line representing N

Output Format
All odd numbers from 1 to N separated by spaces.

Example Input
Input 1:
5
Input 2:
10

Example Output
Output 1:
1 3 5 
Output 2:
1 3 5 7 9 

"""

def main():
    
    n = int(input())
    # use for loop to print all the odd number from 1 to N
    for i in range(1,n+1):
        if i % 2 == 1:
            print(i,end=" ")
    
    return 0

if  __name__ == '__main__':
    main()