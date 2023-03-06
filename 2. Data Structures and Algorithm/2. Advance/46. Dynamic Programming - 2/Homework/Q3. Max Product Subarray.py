""" 
Q3. Max Product Subarray

Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
NOTE: Answer will fit in 32-bit integer value.

Problem Constraints
1 <= N <= 5 * 105
-100 <= A[i] <= 100

Input Format
First and only argument is an integer array A.

Output Format
Return an integer corresponding to the maximum product possible.

Example Input
Input 1:
 A = [4, 2, -5, 1]
Input 2:
 A = [-3, 0, -5, 0]

Example Output
Output 1:
 8
Output 2:
 0
 
Example Explanation
Explanation 1:
 We can choose the subarray [4, 2] such that the maximum product is 8.
Explanation 2:
 0 will be the maximum product possible.
"""

def maxSubarrayProduct(arr, n):

	# max positive product
	# ending at the current position
	max_ending_here = arr[0]

	# min negative product ending
	# at the current position
	min_ending_here = arr[0]

	# Initialize overall max product
	max_so_far = arr[0]

	# /* Traverse through the array.
	# the maximum product subarray ending at an index
	# will be the maximum of the element itself,
	# the product of element and max product ending previously
	# and the min product ending previously. */
	for i in range(1, n):
		temp = max(max(arr[i], arr[i] * max_ending_here),
				arr[i] * min_ending_here)
		min_ending_here = min(
			min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
		max_ending_here = temp
		max_so_far = max(max_so_far, max_ending_here)

	return max_so_far


# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(f"Maximum Sub array product is {maxSubarrayProduct(arr, n)}")

# This code is contributed by shinjanpatra
