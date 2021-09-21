# Matthew Sturtevant & Timothy Hourihan

# Init counters
evens, odds = 0, 0

# Take input and check if even
for x in range(10):
    num = int(input('Enter integer: '))
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

# Print answers
print(f'There are {evens} even numbers in the list')    
print(f'There are {odds} odd numbers in the list')