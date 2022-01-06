from functools import reduce
from collections import defaultdict,deque


def get_puzzle_input(filename):
    with open(filename,'r') as file:
        adapters = [int(a.strip()) for a in file]
    return adapters


def first_star():
    adapters = get_puzzle_input("../data/inputday10.txt")
    sorted_adapters = sorted(adapters)
    controle_delta = reduce(lambda x,y:x+(y-x),sorted_adapters,0)
    print(controle_delta+3)
    un_j,trois_j = 0,0
    for i,n in enumerate(sorted_adapters):
        if i == 0:
            if n == 1:
                un_j += 1
            else:
                trois_j += 1
        else:
            if n-sorted_adapters[i-1] == 1:
                un_j += 1
            else:
                trois_j +=1
    trois_j += 1
    print("[*] result : %s"%(trois_j*un_j))

def compute_neighborhood(sorted_adapters):
    neighborhood = defaultdict(list)
    for i,adapter in enumerate(sorted_adapters):
        try:
            j = i+1
            while (sorted_adapters[j] - adapter <= 3):
                #neighborhood[adapter].append(sorted_adapters[j])
                neighborhood[i].append(j)
                j += 1
        except IndexError as e:
            pass
    return neighborhood

# source : https://marcarea.com/weblog/2019/02/17/parcours-de-graphes-en-python
# BFS - parcours en largeur
# fonctionne sur l'input de test mais trop long sur l'input 
def find_paths(graph,start,end):
    queue = deque()
    queue.append((start, [start]))

    while queue:
        node, path = queue.popleft()
        adjacent_nodes = [n for n in graph[node] if n not in path]
        for adjacent_node in adjacent_nodes:
            if adjacent_node == end:
                yield path + [adjacent_node]
            else:
                queue.append((adjacent_node, path + [adjacent_node]))

#
# https://www.geeksforgeeks.org/number-of-paths-from-source-to-destination-in-a-directed-acyclic-graph/
def add_edge(a, b, fre):
   
    # there is path from a to b.
    v[a].append(b)
    fre[b] += 1

def topological_sorting(fre, n):
    q = deque()
 
    # insert all vertices which
    # don't have any parent.
    for i in range(n):
        if (not fre[i]):
            q.append(i)
 
    l = []
 
    # using kahn's algorithm
    # for topological sorting
    while (len(q) > 0):
        u = q.popleft()
        #q.pop()
 
        # insert front element of queue to vector
        l.append(u)
 
        # go through all it's childs
        for i in range(len(v[u])):
            fre[v[u][i]] -= 1
 
            # whenever the frequency is zero then add
            # this vertex to queue.
            if (not fre[v[u][i]]):
                q.append(v[u][i])
    return l
 
# Function that returns the number of paths
def numberofPaths(source, destination, n, fre):
 
# make topological sorting
    s = topological_sorting(fre, n)
 
    # to store required answer.
    dp = [0]*n
 
    # answer from destination
    # to destination is 1.
    dp[destination] = 1
 
    # traverse in reverse order
    for i in range(len(s) - 1,-1,-1):
        for j in range(len(v[s[i]])):
            dp[s[i]] += dp[v[s[i]][j]]
    return dp

v = [[] for i in range(100)]
def second_star():
    adapters = get_puzzle_input('../data/inputday10_test.txt')
    adapters.append(0)
    adapters.append(max(adapters)+3)
    sorted_adapters = sorted(adapters)
    print(sorted_adapters)
    neighborhood = compute_neighborhood(sorted_adapters)
    print(neighborhood)
    # Execution too long ...
    # paths = find_paths(neighborhood,0,sorted_adapters[len(sorted_adapters)-1])
    # nb_paths = 0
    # for p in paths:
    #     nb_paths += 1
    # print(nb_paths)

    # here vertices are numbered from 0 to n-1.
    n = len(sorted_adapters)
    source, destination = 0, n-1
 
    # to count number of vertex which don't
    # have any parents.
    fre = [0]*n
 
    # to add all edges of graph
    for node,edge in neighborhood.items():
        for e in edge:
            add_edge(node,e,fre)
 
    # Function that returns the number of paths
    print(numberofPaths(source, destination, n, fre))

if __name__ == "__main__":
    first_star()
    second_star()
