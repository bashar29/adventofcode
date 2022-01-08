import copy

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        seats = [[*line.strip()] for line in file.readlines()]
    return seats

def check_seat(seats,i,j):
    if i < 0 or j < 0 or i > len(seats)-1 or j > len(seats[0])-1:
        return 'W'
    else:
        return seats[i][j]

def occupied_seats_around(seats,seat_i,seat_j):
    nb_occupied_seats_around = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if check_seat(seats,seat_i+i,seat_j+j) == '#':
                nb_occupied_seats_around += 1
    if nb_occupied_seats_around >= 4:
        return True
    else:
        return False

   

def occupied_seats_around_second_star(seats,seat_i,seat_j):
    nb_occupied_seats_around = 0
    i,j = 0,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        j += 1
    i,j = 1,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        j += 1; i += 1
    i,j = 1,0
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        i += 1    
    i,j = -1,-1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        i -= 1 ; j -= 1
    i,j = 0,-1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        j -= 1
    i,j = -1,0
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        i -= 1
    i,j = -1,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        i -= 1 ; j += 1
    i,j = 1,-1    
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                nb_occupied_seats_around += 1
            break
        i += 1 ; j -= 1    
    if nb_occupied_seats_around >= 5:
        return True
    else:
        return False

def empty_seats_around_second_star(seats,seat_i,seat_j):
    around_clear = True
    i,j = 0,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        j += 1
    i,j = 1,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        j += 1; i += 1
    i,j = 1,0
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        i += 1    
    i,j = -1,-1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        i -= 1 ; j -= 1
    i,j = 0,-1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        j -= 1
    i,j = -1,0
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        i -= 1
    i,j = -1,1
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        i -= 1 ; j += 1
    i,j = 1,-1    
    while True:
        s = check_seat(seats,seat_i+i,seat_j+j)
        if s != '.' or s == 'W':
            if s == '#':
                around_clear = False
            break
        i += 1 ; j -= 1    
    return around_clear

def empty_around_seat(seats,seat_i,seat_j):
    empty_around = True
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if check_seat(seats,seat_i+i,seat_j+j) == '#':
                empty_around = False
                break
    return empty_around

def step(seats,algo_empty_seats,algo_occupied_seats):
    new_seats = copy.deepcopy(seats)
    for i,line_seats in enumerate(seats):
        for j,seat in enumerate(line_seats):
            if seat == '.':
                continue
            elif seat == 'L':
                if algo_empty_seats(seats,i,j) == True:
                    new_seats[i][j] = '#'
            elif seat == '#':
                if algo_occupied_seats(seats,i,j) == True:
                    new_seats[i][j] = 'L'

    return new_seats

def first_star():
    seats = get_puzzle_input('../data/inputday11.txt')
    
    while True:
        new_seats = step(seats,empty_around_seat,occupied_seats_around)
        if new_seats == seats:
            break
        else:
            seats = new_seats
    
    nb = 0
    for line_seats in seats:
        for s in line_seats:
            if s == '#':
                nb+=1
    print("[*] nb occupied seats : %s"%nb)


def second_star():
    seats = get_puzzle_input('../data/inputday11.txt')
    
    while True:
        new_seats = step(seats,empty_seats_around_second_star,occupied_seats_around_second_star)     
        #for l in new_seats:
        #    print(l)
        #print('__________________________________________________')

        if new_seats == seats:
            break
        else:
            seats = new_seats
    
    nb = 0
    for line_seats in seats:
        for s in line_seats:
            if s == '#':
                nb+=1
    print("[**] nb occupied seats : %s"%nb) 

if __name__ == "__main__":
    first_star()
    second_star()