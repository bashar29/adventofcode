
from collections import defaultdict, namedtuple
import collections

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        rules=[]
        for line in file:
            outer_bag = line.strip().split(' ')[0] + ' ' + line.strip().split(' ')[1]
            rule = line.strip().split(',')
            for i,r in enumerate(rule):
                if i == 0:
                    inner_bag = r.split(' ')[5] + ' ' + r.split(' ')[6]
                    nb_inner_bag = r.split(' ')[4]
                    if nb_inner_bag != 'no':
                        rules.append((outer_bag,int(nb_inner_bag),inner_bag))
                else:
                    inner_bag = r.strip().split(' ')[1] + ' ' + r.strip().split(' ')[2]
                    nb_inner_bag = r.strip().split(' ')[0]
                    if nb_inner_bag != 'no': 
                        rules.append((outer_bag,int(nb_inner_bag),inner_bag))
    return rules

def get_all_containers(inverted_index,bag_name):
    containers = []
    for bag in inverted_index[bag_name]:
        containers.append(bag)
        containers += get_all_containers(inverted_index,bag.name)
    return containers

def get_all_inner_bags(index,outer_bagname):
    bags = []
    for bag in index[outer_bagname]:
        bags.append(bag)
        for i in range(bag.nb):
            bags += get_all_inner_bags(index,bag.name)
    return bags 

def first_star():
    rules = get_puzzle_input('../data/inputday7_test.txt')
    inverted_index = defaultdict(list)
    OuterBag = namedtuple('OuterBag','name nb')
    [inverted_index[rule[2]].append(OuterBag(rule[0],rule[1])) for rule in rules]
    
    containers = get_all_containers(inverted_index,'shiny gold')
    unique_containers = set([bag.name for bag in containers])
    #print(unique_containers)
    print("[*] Number of bags : %s"%len(set(unique_containers)))

def second_star():
    rules = get_puzzle_input('../data/inputday7.txt')
    index = defaultdict(list)
    InnerBag = namedtuple('InnerBag','name nb')
    [index[rule[0]].append(InnerBag(rule[2],rule[1])) for rule in rules]
    bags = get_all_inner_bags(index,'shiny gold')
    nb_bags = 0
    for bag in bags:
        nb_bags += bag.nb
    print("[**] Number of bags : %s"%nb_bags)

    






if __name__ == "__main__":
    first_star()
    second_star()
