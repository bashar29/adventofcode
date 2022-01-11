from collections import defaultdict
from functools import reduce
import functools

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        fields = defaultdict(list)
        my_ticket = []
        nearby_tickets = []
        while (line := file.readline().strip()) != '':
            field_name = line.strip().split(':')[0]
            first_interval = line.strip().split(':')[1].split("or")[0].strip()
            second_interval = line.strip().split(':')[1].split("or")[1].strip()
            fields[field_name].append(first_interval)
            fields[field_name].append(second_interval)
        file.readline() # your ticket
        my_ticket = file.readline().strip()
        file.readline() # separation
        file.readline() # nearby tickets
        for tickets in file:
            nearby_tickets.append(tickets.strip())
    return fields,my_ticket,nearby_tickets

          
def check_ticket(values, ticket):
    '''
    For each value of the ticket ('val1,val2,val3,...'), check if it's included in one of the field interval (tuples).
    Return the list of the value KO for the ticket
    '''  
    values_not_found = []
    for v in ticket.split(','):
        val_found = False
        for ctrl in values:
            if int(v) >= ctrl[0] and int(v) <= ctrl[1]:
                val_found = True
                break 
        if val_found == False:
            values_not_found.append(int(v))
    return values_not_found

def find_fields_possibles_positions(fields,values_in_field):
    fields_pos = defaultdict(list)
    for key,field in fields.items():
        for i,values in enumerate(values_in_field):
            ok_for_all = True
            for value in values:
                if (int(value) < int(field[0].split('-')[0]) or int(value) > int(field[0].split('-')[1])) and \
                   (int(value) < int(field[1].split('-')[0]) or int(value) > int(field[1].split('-')[1])) : 
                    ok_for_all = False
                    break
            if ok_for_all == True:
                fields_pos[key].append(i)
    return fields_pos

def first_star():
    fields,my_ticket,nearby_tickets = get_puzzle_input('../data/inputday16.txt')
    values_in_fields = []
    for values in fields.values():
        for inter in values:
            t = (int(inter.split('-')[0]),int(inter.split('-')[1]))
            values_in_fields.append(t)
    values_rejected = []
    for ticket in nearby_tickets:
        values_rejected += check_ticket(values_in_fields,ticket)    
    result = sum(values_rejected)
    print("[*] result : %s"%result)

def second_star():
    fields,my_ticket,nearby_tickets = get_puzzle_input('../data/inputday16.txt')
    values_in_fields = []
    for values in fields.values():
        for inter in values:
            t = (int(inter.split('-')[0]),int(inter.split('-')[1]))
            values_in_fields.append(t)
    valid_tickets = []
    for ticket in nearby_tickets:
        if len(check_ticket(values_in_fields,ticket)) == 0:
            valid_tickets.append(ticket)
    
    values_tickets_by_index = []
    for i in range(len(my_ticket.split(','))):
        values = []
        for ticket in valid_tickets:
           values.append(ticket.split(',')[i])
        values_tickets_by_index.append(values)

    field_possibilities = find_fields_possibles_positions(fields, values_tickets_by_index)
    
    field_pos = {}

    while True:
        for k,v in field_possibilities.items():
            if len(v) == 1:
                field_pos[k] = v[0]
                field_possibilities.pop(k)
                for values in field_possibilities.values():
                    values.pop(values.index(v[0]))
                break 
        if len(field_pos) == len(fields):
            break

    ticket = []
    for val in my_ticket.split(','):
        ticket.append(val)

    result = []
    result.append(int(ticket[field_pos['departure location']]))
    result.append(int(ticket[field_pos['departure station']]))
    result.append(int(ticket[field_pos['departure platform']]))
    result.append(int(ticket[field_pos['departure track']]))
    result.append(int(ticket[field_pos['departure date']]))
    result.append(int(ticket[field_pos['departure time']]))
    final = functools.reduce(lambda x,y:x*y,result,1)

    print("[**] result : %s"%final)

if __name__ == "__main__":
    first_star()
    second_star()