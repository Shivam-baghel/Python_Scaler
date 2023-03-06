
def checkPalindrome(strg):
    # a = list(strg)
    # a.reverse()
    # b=list(strg)
    # String=strg.lower()

    a=str(strg)
    a=a.lower()
    if a[::] == a[::-1]:
        # flag = True
        return True
    else:
        # flag = False
        return False
        
    # return flag

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
