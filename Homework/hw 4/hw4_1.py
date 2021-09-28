# Matthew Sturtevant
# Due October 4
# Homework 4

def getStates() -> tuple:
    '''
    Collects data from user
    Returns two lists
    '''
    states = []
    pop = []
    # Collect user input
    for _ in range(int(input('How many states are in your list? '))):
        states.append(input('Enter state abbreviation: '))
        pop.append(int(input('Enter state population: ')))
    # return lists as a tuple
    return states, pop

def searchState(abbrs: list, query: str) -> int:
    '''
    returns the index of the query or -1 if not found
    '''
    # find and return the index of the query in the list
    for k, v in enumerate(abbrs):
        if v == query:
            return k
    else:
        return -1

def higherPopStates(abbrs: list, pop: list, index: int) -> list:
    '''
    returns a list of all states with a higher population than the given
    '''
    # finds the higher pops via sorting the lists by population
    x = sorted(zip(abbrs, pop), key=lambda pair : pair[1])
    states = [i[0] for i in x]
    return [x for x in abbrs if x in states[searchState(states, abbrs[index]) + 1:]]

def printResults(state: str, index: int, pop: list, higher_pops: list) -> None:
    print(f'The population of {state} is {pop[index]}\nThe states with a higher population than RI are:\n{higher_pops}')

def main():
    states, pop = getStates()
    query = input('\nEnter a state to find population of: ')
    index = searchState(states, query)
    if index == -1:
        print('No state found')
        return
    higher = higherPopStates(states, pop, index)
    printResults(query, index, pop, higher)