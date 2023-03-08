""" 
Q2. Unbounded Knapsack

Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could fit in this quantity.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.

Problem Constraints
1 <= A <= 1000
1 <= |B| <= 1000
1 <= B[i] <= 1000
1 <= C[i] <= 1000

Input Format
First argument is the Weight of knapsack A
Second argument is the vector of values B
Third argument is the vector of weights C

Output Format
Return the maximum value that fills the knapsack completely

Example Input
Input 1:
A = 10
B = [5]
C = [10]
Input 2:
A = 10
B = [6, 7]
C = [5, 5]

Example Output
Output 1:
 5
Output 2:
14

Example Explanation
Explanation 1:
Only valid possibility is to take the given item.
Explanation 2:
Take the second item twice.
"""

def GetMaxUnbounded( A, B, C):
    weight = C
    value = B 
    max_weight = A
    n = len(weight)
    # lets create a dp matrix.
    dp = []
    for i in range(n):
        col = []
        for j in range(max_weight+1):
            col.append(None)
        dp.append(col)

    # let's create a knapsack function to fill the entire dp matrix.
    def knapSack(i,j,w:list,v:list):
        
        if i<0 or j==0:
            return 0
        
        if dp[i][j] == None:
            a = knapSack(i-1,j,w,v)

            if (j>=w[i]):
                a = max(a,knapSack(i,j-w[i],w,v)+v[i])
            
            dp[i][j] = a 

        return dp[i][j]
    
    return knapSack(n-1,max_weight,weight,value)

def main():
    A = 10
    B = [5]
    C = [10]
    print(GetMaxUnbounded(A,B,C))
    
if __name__ == "__main__":
    main()