
WINDOW = 25

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        numbers = [int(val.strip()) for val in file]
        return numbers

def find_false_number(numbers):
    for i,n in enumerate(numbers):
        conform = False
        if i < WINDOW:
            continue
        for n1 in numbers[i-WINDOW:i]:
            for n2 in numbers[i-WINDOW:i]:
                if n1 != n2:
                    if n1+n2 == n:
                        conform = True
        if conform == False:
            return n
    return None

def find_set_of_numbers_thats_equals_false_number(numbers,false_number):
    for i,number in enumerate(numbers):
        total = number
        j = i
        while total < false_number:
            j += 1
            try:
                total += numbers[j]
            except IndexError as e:
                break
        if total == false_number:
            data = numbers[i:j]
            print("%s %s"%(min(data),max(data)))
            return min(data),max(data)
    return None,None

def first_star():
    numbers = get_puzzle_input('../data/inputday9.txt')
    false_number = find_false_number(numbers)
    print("[*] false number is %s"%false_number)

def second_star():
    numbers = get_puzzle_input('../data/inputday9.txt')
    false_number = find_false_number(numbers)
    n1,n2 = find_set_of_numbers_thats_equals_false_number(numbers,false_number)
    if n1 is not None and n2 is not None: 
        print("[**] result number is %s"%(n1+n2))

if __name__ == "__main__":
    first_star()
    second_star()
