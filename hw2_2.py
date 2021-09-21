# Matthew Sturtevant
# Due September 19, 2021
# Homework 2

# Init a list
scores = []

# Get each score as input
for i in range(9):
    scores.append(int(input('Enter score: ')))

# Sort the list such that lowest score is first
scores.sort()

print(f'Your lowest score for the three weeks is: {scores[0]}') # print only the 0th index of the list