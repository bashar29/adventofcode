from collections import defaultdict

def get_puzzle_input():
    with open('../data/inputday2.txt') as file:
        passwds=[]
        for line in file:
            cond = line.strip().split(' ')[0]
            car = line.strip().split(' ')[1][0]
            passwd = line.strip().split(' ')[2]
            passwds.append([cond,car,passwd])
    return passwds

def control_password_rule_one(control_and_pass):
    min = int(control_and_pass[0].split('-')[0])
    max = int(control_and_pass[0].split('-')[1])

    caracteres = defaultdict(int)
    for c in control_and_pass[2]:
        caracteres[c] += 1

    nb = caracteres[control_and_pass[1]]
    if nb >= min and nb <= max : return 1
    else : return 0

def control_password_rule_two(control_and_pass):
    index_one = int(control_and_pass[0].split('-')[0]) - 1
    index_two = int(control_and_pass[0].split('-')[1]) - 1
    controlA,controlB = 0,0
    if control_and_pass[2][index_one] == control_and_pass[1]:
        controlA = 1
    if control_and_pass[2][index_two] == control_and_pass[1]: 
        controlB = 1
    return (abs(controlB-controlA))

def first_star():
    passwords = get_puzzle_input()
    nb_passwords_ok = 0
    for p in passwords:
        nb_passwords_ok += control_password_rule_one(p)    
    print("nombre de mots de passe corrects : %s"%nb_passwords_ok)    

def second_star():
    passwords = get_puzzle_input()
    nb_passwords_ok = 0
    for p in passwords:
        nb_passwords_ok += control_password_rule_two(p)
    print("nombre de mots de passe corrects : %s"%nb_passwords_ok)    

if __name__ == "__main__":
    first_star()
    second_star()