# Matthew Sturtevant
# Due September 27
# Homework 3

# Initialize two variable small and large
small, large = None, None

# loop through the months for input storing largest and smallest numbers only
for i in range(1, 13):
    x = int(input(f'Enter the number of wagons sold in month {i} : '))
    if i == 1:
        small, large = x, x
    if x > large:
        large = x
    elif x < small:
        small = x

# print results
print(f'The difference between the most wagons sold and the least wagons sold is  {large-small}')