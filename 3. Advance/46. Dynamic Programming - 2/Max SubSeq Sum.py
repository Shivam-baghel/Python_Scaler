

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    arr = [2,-1,4,5,3,-1,4,2]
    num = len(arr)
    dp = [-1]*(num)

    def MaxSub(arr,i):
        if i < 0:
            return 0
        if dp[i] == -1:
            dp[i] = max(MaxSub(arr,i-1) , MaxSub(arr,i-2)+arr[i])
        
        return dp[i]
    print(MaxSub(arr,num-1))
    return 

if __name__ == '__main__':
    main()