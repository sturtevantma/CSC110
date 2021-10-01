# Matthew Sturtevant and Tim Hourihan

def fact(n: int) -> int:
    '''
    Returns n factorial
    '''
    j = 1
    while n > 0:
        j *= n
        n -= 1
    return j

def comb(n: int, r: int) -> float:
    '''
    Returns the result of the combination function
    '''
    return fact(n)//(fact(n-r)*fact(r))