import copy
import re

class Rule:
    def __init__(self,rule:str):
        self.id = rule.strip().split(':')[0]
        self.options = []
        self.options.append(rule.strip().split(':')[1].strip().split('|')[0].strip().split(' '))
        try:
            self.options.append(rule.strip().split(':')[1].strip().split('|')[1].strip().split(' '))
        except IndexError as e:
            pass #only one option
        
        for i,option in enumerate(self.options):
            if option[0] == '"a"':
                self.options[i][0] = 'a'
            if option[0] == '"b"':
                self.options[i][0] = 'b'
        
    def reduce(self,rule):
        options_to_append = []
        final_options = copy.copy(self.options)
        suppr = 0
        for index,option in enumerate(self.options):
            futures_options = self._reduce_option(option,rule)
            if len(futures_options) > 0:
                final_options.pop(index-suppr)
                suppr += 1
                for f_option in futures_options:
                    options_to_append.append(f_option)
        for o in options_to_append:
            final_options.append(o)
        self.options = copy.copy(final_options)
        if len(options_to_append) > 0:
            return True
        else:
            return False
    
    def _reduce_option(self,option,rule):
        futures_options = []
        for i,opt in enumerate(option):
            if opt == rule.id:
                for new_opts in rule.options:
                    future_option = copy.copy(option)
                    future_option.pop(i)
                    k = i
                    for o in new_opts:
                        future_option.insert(k,o)
                        k += 1
                    futures_options.append(future_option)
        return futures_options

    def __repr__(self):
        display = f"id : {self.id} options : {self.options}"
        return display

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        rules = []
        messages = []
        first_part = True
        for line in file:
            if first_part == True:
                if line == '\n':
                    first_part = False
                else:
                    rules.append(line.strip())
            else:
                messages.append(line.strip())
    return rules, messages

def get_a_b_rule(rules):
    rule_a,rule_b = None,None
    for rule in rules:
        if rule.split(':')[1].strip() == '"a"':
            rule_a = rule
        if rule.split(':')[1].strip() == '"b"':
            rule_b = rule
    rules.remove(rule_a)
    rules.remove(rule_b)
    a_b_rules = {}
    a_b_rules[rule_a.split(':')[0].strip()] = 'a'
    a_b_rules[rule_b.split(':')[0].strip()] = 'b'
    return a_b_rules

def first_star():
    rules, messages = get_puzzle_input('../data/inputday19.txt')
    a_b_rules = get_a_b_rule(rules)
    print(a_b_rules)

    rules_obj = []
    for rule in rules:
        r = Rule(rule)
        if r.id == '0':
            rule_zero = r
        #print(r)
        rules_obj.append(r)

    rules_obj.sort(key=lambda r:int(r.id))

    rules_obj_to_reduce = {}
    for rule in rules_obj:
        rules_obj_to_reduce[rule.id] = rule

    #for rule in rules_obj:
    #    rule_zero.reduce(rule)

    reduced = False
    while reduced == False:
        reduced = True
        print(f"length : {len(rule_zero.options)}")
        for option in rule_zero.options:
            for c in option:
                if c not in a_b_rules.keys() and c != '0':
                    if rule_zero.reduce(rules_obj_to_reduce[c]):
                        reduced = False
                        break
            if reduced == False:
                break


    # while len(rules_obj) > 1 :#only r.id == 0 subsist
    #     rules_used = []
    #     for r in rules_obj:
    #         if r.id != '0':
    #             if rule_zero.reduce(r):
    #                 rules_used.append(r)
    #     for rule in rules_used:
    #         rules_obj.remove(rule)

    # for option in rule_zero.options:
    #     for id in option:
    #         if id not in a_b_rules.keys():
    #             rule_zero.reduce(rules_obj_save[id])

    #print(rule_zero)

    patterns = []
    for option in rule_zero.options:
        pattern = []
        for c in option:
            pattern.append(a_b_rules[c])
        patterns.append(''.join(pattern))
    
    for pattern in patterns:
        print(pattern)

    nb_match = 0
    for message in messages:
        if message in patterns:
            nb_match += 1

    print("[*] nb matching messages : %s"%nb_match)

    # for r in rules_obj:
    #     print(r.id)
    #     for o in r.options:
    #         print(" - "+str(o))

def second_star():
    pass

if __name__ == '__main__':
    first_star()
    second_star()