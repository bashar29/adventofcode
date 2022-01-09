

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        soonest_timestamp = int(file.readline().strip())
        bus_id = [int(id) for id in file.readline().strip().split(',') if id != 'x']
        return soonest_timestamp,bus_id

def get_second_puzzle_input(filename):
    with open(filename,'r') as file:
        file.readline()
        bus_id = [id for id in file.readline().strip().split(',')]
        return bus_id    

def first_star():
    soonest_timestamp,bus_id = get_puzzle_input('../data/inputday13.txt')
    possible_departures = {}
    for id in bus_id:
        possible_departures[id] = ((soonest_timestamp//id)*id + id)
    best_departure = min(possible_departures,key=possible_departures.get)
    timestamp = possible_departures[best_departure] 
    print("[*] Best departure bus : %s timer : %s answer : %s"%(best_departure,timestamp,(timestamp-soonest_timestamp)*best_departure))

# https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
def inv(a, m) :  
    m0,x0,x1 = m,0,1
    
    if (m == 1) :
        return 0
 
    # Apply extended Euclid Algorithm
    while (a > 1) :
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
     
    # Make x1 positive
    if (x1 < 0) :
        x1 = x1 + m0
 
    return x1
 
# https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
def findMinX(num, rem, k) :   
    # Compute product of all numbers
    prod = 1
    for i in range(0, k) :
        prod = prod * num[i]
    # Initialize result
    result = 0
    # Apply above formula
    for i in range(0,k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp    
    return result % prod

def second_star():
    bus_id = get_second_puzzle_input('../data/inputday13.txt')
    print(bus_id)
    
    # CRT 
    num, rem = [],[]
    delta = 0
    for id in bus_id:
        if id != 'x':
            num.append(int(id))
            rem.append(delta)
        delta -= 1
    
    print("num : %s rem : %s"%(num,rem))
    print("[**] Departure bus : %s "%(findMinX(num,rem,len(num))))


if __name__ == '__main__':
    first_star()
    second_star()