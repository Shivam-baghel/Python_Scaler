"""
Input:
input_string = 'My name is Shivam'

Desired Output:
output_string = 'Shivam is name My'

"""

def reverse_string(string):
    # reverse string without using empty string

    last_index = len(string)-1
    # we will be swapping the individual characters one by one
    for index in range(0,len(string)//2): #we will go from 0 to half the length of entire list
        temp_string = string[index]          # storing the character to tempString
        string[index] = string[last_index]   # swapping the first character with last character
        string[last_index] = temp_string
        last_index -=1                       #Making sure the last index is updated every time we make a swap
    return string

def reverse_words(string,first_index,last_index):
    l_index = last_index
    while first_index<l_index:
        temp_string = string[first_index]          # storing the character to tempString
        string[first_index] = string[l_index]   # swapping the first character with last character
        string[l_index] = temp_string
        l_index -=1
        first_index +=1
    return string
 

inputString = list(input())
startIndex = 0
for index in range(len(inputString)+1):
    
    if index == len(inputString) or inputString[index] == " ":
        # print(index,inputString[index])
        string = reverse_words(inputString,startIndex,index-1)
        startIndex = index+1

revString = reverse_string(string)

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

