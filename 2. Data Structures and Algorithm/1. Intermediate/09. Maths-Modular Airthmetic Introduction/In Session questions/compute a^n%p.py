"""
Given a,n,p and compute a^n % p?
Note: No inbuilt function allowed.

Modular Arithmetic Properties:
1st property: addition property
(a + b) % m = (a % m + b % m) % m
2nd property: multiplication property
(a * b) % m = (a % m * b % m) % m

"""


# Bruteforce : as this approach does not handle overflow.
def power(a: int, n: int, p: int):
    ans = 1
    while (n > 0):
        ans = ans * a
        n -= 1

    return ans % p


# Optamization : this approach will easily handle overflow.
def optamisedPower(a: int, n: int, p: int):
    ans = 1
    while (n > 0):
        ans = (ans * a) % p  # here we are using multiplication property check line 9
        n -= 1

    return ans % p


a, n, p = map(int, input().split())
print(power(a, n, p))
print(optamisedPower(a, n, p))
