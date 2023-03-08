""" 
Q4. Check even/odd
Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

Problem Constraints
1 <= N <= 1000000

Input Format
One line containing an integer N.

Output Format
Print either 1 or 0 as per the question.

Example Input
Input 1:
5
Input 2:

000

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
Clearly, 5 is odd.
Explanation 2:
Clearly, 1000 is even.
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    n = int(input())
    if(n%2==1):
        print('1')
    else:
        print('0')
    return 0

if __name__ == '__main__':
    main()