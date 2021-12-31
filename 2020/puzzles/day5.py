from collections import namedtuple

NB_DIGITS_FOR_ROWS = 7

def get_puzzle_input():
    with open('../data/inputday5.txt') as file:
        seats = []
        for line in file:
            seats.append([*line.strip()])
    return seats

def get_row_from_boarding_pass(boarding_pass):
    range_min,range_max = 0,127
    for code in boarding_pass[:NB_DIGITS_FOR_ROWS]:
        if code == 'F':
            range_max = range_min + ((range_max-range_min) // 2)
        else:
            range_min = range_min + (((range_max-range_min) // 2) + 1)
    return range_min
    
def get_column_from_boarding_pass(boarding_pass):
    column_min, column_max = 0,7
    for code in boarding_pass[NB_DIGITS_FOR_ROWS:]:
        if code == 'L':
            column_max = column_min + ((column_max-column_min) // 2)
        else:
            column_min = column_min + (((column_max-column_min) // 2) + 1)
    return column_min

def compute_seat_id(row,column):
    return 8*row+column

def first_star():
    seats = get_puzzle_input()
    max_seat_id = 0
    for seat in seats:
        row = get_row_from_boarding_pass(seat)
        column = get_column_from_boarding_pass(seat)
        seat_id = compute_seat_id(row,column)
        if seat_id > max_seat_id: max_seat_id = seat_id
        #print("seat %s row %s column %s seat_id %s"%(seat,row,column,seat_id))
    
    print("[*] max seat ID is %s"%max_seat_id)

def second_star():
    seats = get_puzzle_input()
    decoded_seats = []        
    for seat in seats:
        row = get_row_from_boarding_pass(seat)
        column = get_column_from_boarding_pass(seat)
        seat_id = compute_seat_id(row,column)
        decoded_seats.append(seat_id)
    decoded_seats.sort()
    
    for i,s in enumerate(decoded_seats):
        try:
            if decoded_seats[i+1] - s > 1:
                my_seat_id = s + 1
                break
        except IndexError as e:
            pass

    print("[**] my seat is %s"%my_seat_id)

if __name__ == "__main__":
    first_star()
    second_star()