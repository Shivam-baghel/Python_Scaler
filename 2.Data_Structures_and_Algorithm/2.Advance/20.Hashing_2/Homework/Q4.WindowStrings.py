""" 

Q4. Window String

Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index and length )


Problem Constraints
1 <= size(A), size(B) <= 106

Input Format
The first argument is a string A.
The second argument is a string B.

Output Format
Return a string denoting the minimum window.


Example Input
Input 1:

 A = "ADOBECODEBANC"
 B = "ABC"
Input 2:

 A = "Aa91b"
 B = "ab"


Example Output
Output 1:

 "BANC"
Output 2:

 "a91b"


Example Explanation
Explanation 1:

 "BANC" is a substring of A which contains all characters of B.
Explanation 2:

 "a91b" is the substring of A which contains all characters of B.
 """


def minWindow(A, B):
    counts = {c: 0 for c in B}
    target_counts = {}
    # stores the frequency of all character in B
    for c in B:
        if c in target_counts:
            target_counts[c] += 1
        else:
            target_counts[c] = 1
    cover = 0
    shortest = None
    start, end = 0, 0
    while end < len(A) or cover == len(counts):
        if cover < len(counts):
            end += 1
            if A[end - 1] in counts:
                # We check if the current character represented by end caused a character
                # to be included which is relevant to B and is still in deficit.
                if counts[A[end - 1]] == target_counts[A[end - 1]] - 1:
                    cover += 1
                counts[A[end - 1]] += 1
        else:
            # move the start pointer popping out the character that
            # still makes sure that all characters in B are covered.
            if A[start] in counts:
                counts[A[start]] -= 1
                if counts[A[start]] == target_counts[A[start]] - 1:
                    cover -= 1
            start += 1
        # check if we have all characters in B covered
        if cover == len(counts):
            if shortest is None or end - start < shortest[0]:
                shortest = end - start, start, end
    if shortest is None:
        return ""
    return A[shortest[1] : shortest[2]]
