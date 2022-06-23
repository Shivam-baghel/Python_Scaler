"""
Input:
input_string = 'My name is Shivam'

Desired Output:
output_string = 'Shivam is name My'

"""

def reverseString(string):
    # reverse string without using empty string

    lastIndex = len(string)-1
    # we will be swapping the individual characters one by one
    for index in range(0,len(string)//2): #we will go from 0 to half the length of entire list
        tempString = string[index]          # storing the character to tempString
        string[index] = string[lastIndex]   # swapping the first character with last character
        string[lastIndex] = tempString
        lastIndex -=1                       #Making sure the last index is updated every time we make a swap
    return string

def reverseWords(string,firstIndex,lastIndex):
    lIndex = lastIndex
    while firstIndex<lIndex:
        tempString = string[firstIndex]          # storing the character to tempString
        string[firstIndex] = string[lIndex]   # swapping the first character with last character
        string[lIndex] = tempString
        lIndex -=1
        firstIndex +=1
    return string
 

inputString = list(input())
startIndex = 0
for index in range(len(inputString)+1):
    
    if index == len(inputString) or inputString[index] == " ":
        # print(index,inputString[index])
        string = reverseWords(inputString,startIndex,index-1)
        startIndex = index+1

revString = reverseString(string)

print(" ".join(revString))

# print(string)

"""

x = input("Enter any string: ")
#take input from user

a = x.split()
#use split method to split at whitespaces
print(a)

a.reverse()
#reverse all the elements of the string 
print(a)
print(' '.join(a))
#concatenate them into a string

"""

