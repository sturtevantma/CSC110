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
