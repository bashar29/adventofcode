import re

MANDATORY_INFO = ['hcl','iyr','eyr','ecl','pid','byr','hgt']
OPTIONAL_INFO = ['cid']

def get_puzzle_input():
    with open('../data/inputday4.txt','r') as file:
        passports = []
        brut_data = {}
        for line in file:
            if line.strip() == '':
                passports.append(brut_data.copy())
                brut_data.clear()
            else:
                for info in line.strip().split(' '):
                    brut_data[info.split(':')[0]] = info.split(':')[1]
        passports.append(brut_data.copy())
    return passports

def check_validity_of_passport(passport:dict):
    for info in MANDATORY_INFO:
        if info not in passport.keys():
            return False
    return True

def check_advanced_validity_of_passport(passport:dict):
    for info in MANDATORY_INFO:
        if info not in passport.keys():
            return False
        else:
            val_to_check = passport[info]
            if info == 'byr':
                if len(val_to_check) != 4 or int(val_to_check) < 1920 or int(val_to_check) > 2002:
                    return False
            elif info == 'iyr':
                if len(val_to_check) != 4 or int(val_to_check) < 2010 or int(val_to_check) > 2020:
                    return False
            elif info == 'eyr':
                if len(val_to_check) != 4 or int(val_to_check) < 2020 or int(val_to_check) > 2030:
                    return False
            elif info == 'ecl':
                if val_to_check not in ['amb','blu','brn','gry','grn','hzl','oth']:
                    return False
            elif info == 'pid':
                if len(val_to_check) != 9 or re.fullmatch(r"[0-9]*",val_to_check) is None:
                    return False
            elif info == 'hcl':
                if val_to_check[0] != '#' or re.fullmatch(r"[0-9a-f]*",val_to_check[1:]) is None:
                    return False
            elif info == 'hgt':
                cond = False
                if re.fullmatch(r"[0-9]{3}cm",val_to_check) is not None and int(val_to_check[0:3]) <= 193 and int(val_to_check[0:3]) >= 150:
                    cond = True
                if re.fullmatch(r"[0-9]{2}in",val_to_check) is not None and int(val_to_check[0:2]) <= 76 and int(val_to_check[0:2]) >= 59:
                    cond = True
                if cond == False:
                    return False            
    return True

def first_star():
    passports = get_puzzle_input()
    nb_valid_passports = 0
    for passport in passports:
        if check_validity_of_passport(passport) == True:
            nb_valid_passports += 1

    print("* Number of valid passports : %s"%nb_valid_passports)

def second_star():
    passports = get_puzzle_input()
    nb_valid_passports = 0
    for passport in passports:
        if check_advanced_validity_of_passport(passport) == True:
            nb_valid_passports += 1

    print("**Number of valid passports : %s"%nb_valid_passports)
    

if __name__ == "__main__":
    first_star()
    second_star()
