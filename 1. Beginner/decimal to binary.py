def decimalToBinary(number):
    lst = []
    while number > 0:
        remainder = number%2
        lst.append(remainder)
        number=number//2
    return lst

number = int(input())
binaryNumber = decimalToBinary(number)
count = binaryNumber.count(1)
print(count)

