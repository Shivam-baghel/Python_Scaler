def checksSameArray(firstArray, secondArray):
    firstArray.sort() #sorting both the array so that it becomes easier to compare element.
    secondArray.sort()
    
    if firstArray == secondArray: #comparing the elements this is easy way by python. 
        return 1
    
    return 0

first_Array = list(map(int,input("Enter first array : ").split()))
second_Array = list(map(int,input("Enter second array : ").split()))

print(checksSameArray(first_Array,second_Array))