# Matthew Sturtevant
# Due September 27
# Homework 3

lis = []
# get length of list and get each age
for i in range(int(input('How many ages have been collected? '))):
    lis.append(int(input('Enter age: ')))

# print result
print('The sampled list is:\n')
print([v for k, v in enumerate(lis) if k % 3 == 0]) # gets each third value in the list