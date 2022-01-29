import copy
from collections import defaultdict

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        rules = defaultdict(list)
        messages = []
        first_part = True
        for line in file:
            if first_part == True:
                if line == '\n':
                    first_part = False
                else:
                    id = int(line.split(':')[0])
                    options = line.split(':')[1].replace('\"','')
                    for option in options.split('|'):
                        try:
                            rules[id] += [[int(d.strip()) for d in option.split()]]
                        except ValueError as e:
                            # a and b
                            rules[id] = [[d.strip() for d in option.split()]]
            else:
                messages.append(line.strip())
    return rules, messages

def reduce_rule(ruleid,rules):
    pass

def first_star():
    rules, messages = get_puzzle_input('../data/inputday19.txt')
    print(rules) 

def second_star():
    pass

if __name__ == '__main__':
    first_star()
    second_star()