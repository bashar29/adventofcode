import copy

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        slice = []
        for line in file:
            slice.append([*line.strip()])
    return slice

def print_pocket(pocket):
    print('Pocket :')
    for slice in pocket:
        for line in slice:
            print(line)
    print('/Pocket')

def print_hyper_pocket(pocket):
    print('Hyper Pocket :')
    for i,w in enumerate(pocket):
        print("w=%s"%i)
        print_pocket(w)    
    print('/Hyper Pocket')

def get_number_actif_cubes(pocket):
    nb = 0
    for slice in pocket:
        for line in slice:
            for c in line:
                if c == '#':
                    nb += 1
    return nb

def get_number_actif_hypercubes(hyper_pocket):
    nb = 0
    for pocket in hyper_pocket:
        for slice in pocket:
            for line in slice:
                for c in line:
                    if c == '#':
                        nb += 1
    return nb

def expand_dimension(pocket):
    for slice in pocket:
        for line in slice:
            line.insert(0,'.')
            line.append('.')
        length = len(line)
    for slice in pocket:
        slice.insert(0,length*['.'])
        slice.append(length*['.'])
    slice_len = len(slice)        
    upper_slice = []
    for i in range(slice_len):
        upper_slice.append(length*['.'])
    pocket.append(upper_slice)
    lower_slice = []
    for i in range(slice_len):
        lower_slice.append(length*['.'])
    pocket.insert(0,lower_slice)
    return pocket

def create_empty_pocket(size):
    pocket = []
    for k in range(size):
        slice = []
        for j in range(size):
            line = [] 
            for i in range(size):
                line.append('.')
            slice.append(line)
        pocket.append(slice)
    return pocket

def expand_hyper_dimension(hyper_pocket):
    new_hyper_pocket = copy.deepcopy(hyper_pocket)
    for index,pocket in enumerate(hyper_pocket):
        new_pocket = expand_dimension(pocket)
        new_hyper_pocket[index] = new_pocket
    new_hyper_pocket.insert(0,create_empty_pocket(len(new_pocket[0])))
    new_hyper_pocket.append(create_empty_pocket(len(new_pocket[0])))
    return new_hyper_pocket

def check_neighbours(pocket,i,j,k):
    nb_actives_neightbours = 0
    for kk in range(k-1,k+2):
        if kk >= 0 and kk < len(pocket):
            for jj in range (j-1,j+2):
                if jj >= 0 and jj < len(pocket[kk]):
                    if i > 0:
                        if pocket[kk][jj][i-1] == '#': 
                            nb_actives_neightbours += 1
                    if i < len(pocket[kk][jj]) - 1:
                        if pocket[kk][jj][i+1] == '#': 
                            nb_actives_neightbours += 1
                    if kk != k or jj != j:
                        if pocket[kk][jj][i] == '#':
                            nb_actives_neightbours += 1
    return nb_actives_neightbours

def check_hyper_neighbours(hyper_pocket,i,j,k,w):
    nb_actives_neightbours = 0
    try:
        for ww in range(w-1,w+2):
            if ww >= 0 and ww < len(hyper_pocket):
                for kk in range(k-1,k+2):
                    if kk >= 0 and kk < len(hyper_pocket[ww]):
                        for jj in range (j-1,j+2):
                            if jj >= 0 and jj < len(hyper_pocket[ww][kk]):
                                if i > 0:
                                    if hyper_pocket[ww][kk][jj][i-1] == '#': 
                                        nb_actives_neightbours += 1
                                if i < len(hyper_pocket[ww][kk][jj]) - 1:
                                    if hyper_pocket[ww][kk][jj][i+1] == '#': 
                                        nb_actives_neightbours += 1
                                if ww != w or kk != k or jj != j:
                                    if hyper_pocket[ww][kk][jj][i] == '#':
                                        nb_actives_neightbours += 1
    except IndexError as e:
        print("i=%s j=%s k=%s w=%s jj=%s kk=%s ww=%s"%(i,j,k,w,jj,kk,ww))
        print_hyper_pocket(hyper_pocket)
        raise e
    return nb_actives_neightbours

def execute_cycle(pocket_dimension):
    expanded_pocket_dimension = expand_dimension(pocket_dimension)
    new_pocket_dimension = copy.deepcopy(expanded_pocket_dimension)
    for k,slice in enumerate(expanded_pocket_dimension):
        for j,line in enumerate(slice):
            for i,cube in enumerate(line):
                nb_actives_neighbours = check_neighbours(expanded_pocket_dimension,i,j,k)
                if nb_actives_neighbours == 3 and cube == '.':
                    new_pocket_dimension[k][j][i] = '#'
                elif (nb_actives_neighbours == 3 or nb_actives_neighbours == 2) and cube == '#':
                    new_pocket_dimension[k][j][i] = '#'
                else:
                    new_pocket_dimension[k][j][i] = '.'
    return new_pocket_dimension

def execute_hyper_cycle(hyper_pocket_dimension):
    expanded_hyper_pocket_dimension = expand_hyper_dimension(hyper_pocket_dimension)
    new_hyper_pocket_dimension = copy.deepcopy(expanded_hyper_pocket_dimension)
    for w,pocket in enumerate(expanded_hyper_pocket_dimension):
        for k,slice in enumerate(pocket):
            for j,line in enumerate(slice):
                for i,cube in enumerate(line):
                    nb_actives_neighbours = check_hyper_neighbours(expanded_hyper_pocket_dimension,i,j,k,w)
                    if nb_actives_neighbours == 3 and cube == '.':
                        new_hyper_pocket_dimension[w][k][j][i] = '#'
                    elif (nb_actives_neighbours == 3 or nb_actives_neighbours == 2) and cube == '#':
                        new_hyper_pocket_dimension[w][k][j][i] = '#'
                    else:
                        new_hyper_pocket_dimension[w][k][j][i] = '.'
    return new_hyper_pocket_dimension

#K[J[I['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
def first_star():
    slice = get_puzzle_input('../data/inputday17.txt')
    pocket_dimension = [slice]
    for i in range(6):
        #print_pocket(pocket_dimension)
        pocket_dimension = execute_cycle(pocket_dimension)
    #print_pocket(pocket_dimension)
    print("[*] number of active cube : %s"%get_number_actif_cubes(pocket_dimension))

def second_star():
    slice = get_puzzle_input('../data/inputday17.txt')
    hyper_pocket_dimension = [[slice]]
    print_hyper_pocket(hyper_pocket_dimension)
    for i in range(6):
        #print_hyper_pocket(hyper_pocket_dimension)
        hyper_pocket_dimension = execute_hyper_cycle(hyper_pocket_dimension)
    #print_hyper_pocket(hyper_pocket_dimension)
    print("[**] number of active cube : %s"%get_number_actif_hypercubes(hyper_pocket_dimension))

if __name__ == "__main__":
    first_star()
    second_star()