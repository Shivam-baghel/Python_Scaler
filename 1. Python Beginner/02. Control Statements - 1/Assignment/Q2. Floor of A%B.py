""" 
Q2. Floor of A/B
Given two numbers A and B. Print the floor of A/B.

Problem Constraints
1 <= A, B <= 104

Input Format
There are two input lines
The first line has a single integer A.
The second line has a single integer B.

Output Format
Print the floor of A/B in a single line.

Example Input
Input 1:-
4
5
Input 2:-
16
2

Example Output
Output 1:-
0
Output 2:-
8

Example Explanation
Explanation 1:-
floor(4/5) = 0
Explanation 2:-
floor(16/2) = 8
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    a=int(input())
    b=int(input())
    c=a//b
    print(c)
    return 0

if __name__ == '__main__':
    main()