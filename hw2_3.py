# Matthew Sturtevant
# Due September 19, 2021
# Homework 2

# Init a list
bugs = []

# Get the number of bugs for each day
for i in range(1,8):
    bugs.append(int(input(f'How many bugs did you collect on day {i}? ')))


# print the average of the numbers in the list
print(f'The average number of bugs collected this week is  {round(sum(bugs)/len(bugs), 2)}') # make sure to round to the 100ths place
