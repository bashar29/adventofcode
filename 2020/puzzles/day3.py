from functools import reduce

def get_puzzle_input():
    with open('../data/inputday3.txt') as file:
        map_of_trees = []
        for line in file:
            locations = [*line.strip()]
            map_of_trees.append(locations)
    return map_of_trees

def expande_map_of_trees(map_of_trees,right_slope):
    final_width = right_slope*len(map_of_trees) + 1
    current_width = len(map_of_trees[0])
    nb_expansion = final_width//current_width + 1
    for positions in map_of_trees:
        positions += nb_expansion * positions

def first_star():
    map_of_trees = get_puzzle_input()
    expande_map_of_trees(map_of_trees,3)
    nb_tree_collisions,i,j = 0,0,0
    
    while i < len(map_of_trees) - 1:
        i+=1;j+=3
        if map_of_trees[i][j] == '#':
            nb_tree_collisions += 1
    
    print("Number of tree collisions : %s"%nb_tree_collisions)

def second_star():
    map_of_trees = get_puzzle_input()
    expande_map_of_trees(map_of_trees,7)
    
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    
    for s in slopes:
        nb_collisions,i,j = 0,0,0
        while i < len(map_of_trees) - 1:
            i+=s[1];j+=s[0]
            if map_of_trees[i][j] == '#':
                nb_collisions += 1
        s.append(nb_collisions)
    
    result = reduce(lambda x,y:x*y[2],slopes,1)

    print("Product of tree collisions for all slopes : %s"%result)


if __name__ == "__main__":
    first_star()
    second_star()