# Matthew Sturtevant
# Due October 4
# Homework 4

def prodDigits(n: int) -> int:
    '''
    Multiplies the digits of an integer together
    '''
    x = 1
    for i in str(n):
        x *= int(i)
    return x

def prodDivisible(limit: int) -> list:
    ans = []
    # check if i is divisble by 0 after that prodDigits is not 0
    for i in range(1, limit):
        x = prodDigits(i)
        if x != 0:
            if i % x == 0:
                ans.append(i)
    return ans

