from collections import defaultdict
from memory_profiler import profile


def turn(turn,last_number,numbers_spoken):
    if len(numbers_spoken[last_number]) == 1:
        number = 0
    else:
        # the turn number of the time it was most recently spoken before the last call
        last_time = numbers_spoken[last_number][-2]
        number = turn - 1 - last_time
    numbers_spoken[number].append(turn)
    return number

@profile
def first_star():
    start_numbers = [0,20,7,16,1,18,15]
    #start_numbers = [2,1,3]
    numbers_spoken = defaultdict(list)
    for i,n in enumerate(start_numbers):
        numbers_spoken[n].append(i)
    
    last_number = start_numbers[-1]
    for t in range(len(start_numbers),2020):
        last_number = turn(t,last_number,numbers_spoken)
    print("[*] number after 2020 turns : %s"%last_number)


def second_star():
    start_numbers = [0,20,7,16,1,18,15]
    #start_numbers = [2,1,3]
    numbers_spoken = defaultdict(list)
    for i,n in enumerate(start_numbers):
        numbers_spoken[n].append(i)
    
    last_number = start_numbers[-1]
    for t in range(len(start_numbers),30000000):
        last_number = turn(t,last_number,numbers_spoken)
    print("[**] number after 30M turns : %s"%last_number)

if __name__ == "__main__":
    first_star()
    second_star()