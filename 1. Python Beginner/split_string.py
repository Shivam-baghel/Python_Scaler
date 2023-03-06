"""
Input: 
input_list =  ['red', 'blue', 'green&blue&yellow', 'pink', 'yellow&red&blue']

Output:
input_list = ['red','blue', 'green', 'blue', 'yellow', 'pink', 'yellow', 'red','blue']

"""

# solved without using split() function

def splitString(input_list):
    newList = []
    for item in range(len(input_list)):
        start = 0
        index = 0

        for index, char in enumerate(input_list[item]):
            if char == '&':
                element = input_list[item][start:index]
                newList.append(element)
                start +=index+1
        
        alnum_word = ""
        for element in input_list[item][::-1]:
            if element != '&':
                alnum_word += element
            else:
                break
        newList.append(alnum_word[::-1])
    return newList

input_list = ['red', 'blue', 'green&blue&yellow', 'pink', 'yellow&red&blue']
print(splitString(input_list))
    

