lis = [int(input('Enter age: ')) for x in range(int(input('How many ages have been collected? ')))]
print(f'The sampled list is:\n\n{[v for k, v in enumerate(lis) if k % 3 == 0]}')