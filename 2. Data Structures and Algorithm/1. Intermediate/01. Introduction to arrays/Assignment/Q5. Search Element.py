"""
Q5. Search Element
You are given an integer T (number of test cases). You are given array A and an integer B for each test case. You have to tell whether B is present in array A or not.

Problem Constraints

1 <= T <= 10
1 <= A <= 105
1 <= A[i], B <= 109


Input Format

First line of the input contains number of test cases as single integer T .
Next, each of the test case consists of 3 lines:

First line contains a single integer A denoting the length of array
Second line contains A integers denoting the array elements
Third line contains a single integer B


Output Format
For each test case, print on a separate line 1 if the element exists, else print 0.

Example Input

Input 1:

 1
 5
 4 1 5 9 1
 5
Input 2:

 1
 3
 7 7 2
 1


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

  B = 5  is present at position 3 in A
Explanation 2:

  B = 1  is not present in A.
"""


def search_ele():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    test_Cases = int(input())
    while (test_Cases > 0):

        array = list(map(int, input().split()))
        array.pop(0)
        number = int(input())
        flag = 0

        for i in range(len(array)):
            if array[i] == number:
                flag = 1
                break

        if flag > 0:
            print(flag)
        else:
            print(flag)

        test_Cases -= 1
    return 0


if __name__ == '__main__':
    search_ele()