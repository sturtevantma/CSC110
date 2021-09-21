# Matthew Sturtevant and Tim Hourihan

# Take inputs
star_rating = int(input('Enter star rating: '))
num_shares = int(input('Enter number of shares: '))

threshold = (0,0) # Used to compare against num_shares

# Check star rating
if star_rating <= 2:
    threshold = (1000, 2)
elif star_rating <= 4:
    threshold = (2500, 3)
else:
    threshold = (5000, 4)

# Check number of shares & compute
ans = None
if num_shares < threshold[0]:
    ans = star_rating * num_shares * threshold[1]
else:
    ans = star_rating * num_shares

# output score
print(f'The score is :  {ans}')
