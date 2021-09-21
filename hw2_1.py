# Matthew Sturtevant
# Due September 19, 2021
# Homework 2

# Get initial cost
cost_before_sale = int(input('Enter amount of sale: $'))

# Check the price going up incrementally to limit the need for multiple comparisons in each statement
discount = 1.0
if cost_before_sale <= 2500:
    discount = 0.9
elif cost_before_sale <= 3500:
    discount = 0.85
elif cost_before_sale <= 4500:
    discount = 0.8
else:
    discount = 0.75

# Multiply discount by sale price and print result
print(f'Your discounted sale amount is $ {cost_before_sale*discount}')
