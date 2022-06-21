
def checkPalindrome(strg):
    a = list(strg)
    a.reverse()

    b=list(strg)
    if a==b:
        flag = True
    else:
        flag = False
        
    return flag

def removeSpecialChar(strg):
    a = ""
    for i in strg:
        if i.isalpha():
            a =a+i
        else:
            pass

    return a

aString = input()
bString = removeSpecialChar(aString)
print(checkPalindrome(bString))
