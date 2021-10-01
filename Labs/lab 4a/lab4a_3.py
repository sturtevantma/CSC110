# Matthew Sturtevant and Tim Hourihan

def sumOfMultiples(n: int, a: int, b: int) -> int:
    '''
    Finds the sum of all the multiples of a or b on the domain [0,n)
    input (n, a, b)
    '''
    ans = 0
    for i in range(n):
        if i % a == 0 or i % b == 0:
            ans += i
    return ans

print(sumOfMultiples(1000, 3, 5))