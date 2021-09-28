# Matthew Sturtevant && Timothy Hourihan

# Take user input
limit = int(input("Enter the highest number to consider: ")) - 1

# get number of multiples in limit
threes = limit // 3
fives = limit // 5

# counter go brrrrr
ans = 0

# add 3s
for i in range(1, threes + 1):
    ans += 3 * i

# add 5s unless they are mulitple of 3
for i in range(1, fives + 1):
    if (5 * i) % 3 != 0:
        ans += 5 * i

# subtract the limit becuase thats what works for some reason
print(f"The sum of all multiples of 3 and 5 below {limit + 1} is:  {ans}")