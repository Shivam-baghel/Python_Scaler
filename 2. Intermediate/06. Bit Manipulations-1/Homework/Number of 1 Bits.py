"""


"""

def numSetBits(num:int):
    counter = 0
    while num>0:
        rem = num%2
        num = num//2
        if rem == 1:
            counter +=1
    return counter

number = int(input())
print(numSetBits(number))