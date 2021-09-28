# Matthew Sturtevant
# Due October 4
# Homework 4

def prodDigits(n: int) -> int:
    '''
    Multiplies the digits of an integer together
    '''
    x = 1
    # Multiply digit by the next digit until no more digits
    for i in str(n):
        x *= int(i)
    return x

