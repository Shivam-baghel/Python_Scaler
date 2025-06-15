"""
Q1. Rotation Game

Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.

Problem Constraints
1 <= N <= 106
1 <= A[i] <=108
1 <= B <= 109

Input Format
There are 2 lines in the input
Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.
Line 2: A single integer B.

Output Format
Print array A after rotating it B times towards the right.

Example Input
Input 1 :
4 1 2 3 4
2

Example Output
Output 1 :
3 4 1 2

Example Explanation
Example 1 :
N = 4, A = [1, 2, 3, 4] and B = 2.

Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]

Final array = [3, 4, 1, 2]
"""


def rotation_game():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    def reversePart(array, startIndex, endIndex):
        while startIndex < endIndex:
            array[startIndex], array[endIndex] = array[endIndex], array[startIndex]
            startIndex += 1
            endIndex -= 1

    array = list(map(int, input().split()))
    n = array.pop(0)
    rotateNumber = int(input())

    rotateNumber = rotateNumber % n

    # reverse the array
    reversePart(array, 0, n - 1)

    # reverse first K elements
    reversePart(array, 0, rotateNumber - 1)

    # reverse last n-k elements
    reversePart(array, rotateNumber, n - 1)

    for i in range(len(array)):
        print(array[i], end=" ")

    return 0


if __name__ == '__main__':
    rotation_game()