""" 
Q4. Maximum Subarray Easy
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.

Problem Constraints
1 <= A <= 103
1 <= B <= 109
1 <= C[i] <= 106

Input Format
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.

Output Format
Return a single integer which denotes the maximum sum.

Example Input
Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
Input 2:
A = 3
B = 1
C = [2, 2, 2]

Example Output
Output 1:
12
Output 2:
0

Example Explanation
Explanation 1:
We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
Explanation 2:
All elements are greater than B, which means we cannot select any subarray.
Hence, the answer is 0.
"""

def findMaxSubarraySum(arr, n, sumb):
	
	# To store current sum and
	# max sum of subarrays
	curr_sum = arr[0]
	max_sum = 0
	start = 0;

	# To find max_sum less than sum
	for i in range(1, n):
		
		# Update max_sum if it becomes
		# greater than curr_sum
		if (curr_sum <= sumb):
			max_sum = max(max_sum, curr_sum)

		# If curr_sum becomes greater than sum
		# subtract starting elements of array
		while (curr_sum + arr[i] > sumb and start < i):
			curr_sum -= arr[start]
			start += 1
		
		# Add elements to curr_sum
		curr_sum += arr[i]

	# Adding an extra check for last subarray
	if (curr_sum <= sumb):
		max_sum = max(max_sum, curr_sum)

	return max_sum

# Driver Code
if __name__ == '__main__':
	arr = [6, 8, 9]
	n = len(arr)
	sum = 20

	print(findMaxSubarraySum(arr, n, sum))

# This code is contributed by
# Surendra_Gangwar
