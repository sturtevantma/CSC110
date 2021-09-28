# Matthew Sturtevant and Timothy Hourihan

# Take inputs
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

# Init answer equal to a
answer = a

# Compute answer
for i in range(b-1):
    answer*=a

# print answer
print(f"{a} ** {b} = {answer}")