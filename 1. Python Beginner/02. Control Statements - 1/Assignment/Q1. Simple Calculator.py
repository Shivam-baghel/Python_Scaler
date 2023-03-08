""" 
Q1. A Simple Calculator
Given two numbers A and B. Print A+B, A*B, A-B, A/B in the same order.

Problem Constraints
1 <= A, B <= 104

Input Format
There are two input lines
The first line has a single integer A.
The second line has a single integer B.

Output Format
Print in a single line separated by space A+B, A*B, A-B, A/B in the same order.

Example Input
Input 1:-
4
5
Input 2:-
16
2

Example Output
Output 1:-
9 20 -1 0
Output 2:-
18 32 14 8

Example Explanation
Explanation 1:-
4 + 5 = 9, 4 * 5 = 20, 4 - 5 = -1, 4 / 5 = 0
Explanation 2:-
16 + 2 = 18, 16 * 2 = 32, 16 - 2 = 14, 16 / 2 = 8
"""
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    a = int(input())
    b = int(input())
    print(a+b,a*b,a-b,int(a/b))
    
    return 0

if __name__ == '__main__':
    main()
