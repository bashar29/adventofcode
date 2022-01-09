import re,copy
from collections import deque

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        instructions = [[cmd.strip() for cmd in line.strip().split('=')] for line in file]
    return instructions

class Chip:
    
    MASK_LENGTH = 36
    
    def __init__(self,initial_mask):
        self.memory = {}
        self.mask = initial_mask
    
    def set_memory(self,adress,value):
        # conversion d'une string en list pour traiter les assignations, 
        # puis reconversion en string en fin de fonction
        binary_value = bin(int(value))[2:].rjust(Chip.MASK_LENGTH,'0')
        l_binary_value = [*binary_value]
        
        for i,b in enumerate(self.mask):
            if b == '0':
                l_binary_value[i] = '0'
            elif b == '1':
                l_binary_value[i] = '1'

        self.memory[adress] = int(''.join(l_binary_value),2)
    
    def compute_sum_values_inmemory(self):
        result = 0
        for v in self.memory.values():
            result += v
        return result

    def manage_instruction(self,instruction):
        if instruction[0] == 'mask':
            self.mask = instruction[1]
        else:
            match_object = re.search(r'[0-9]+',instruction[0])
            try:
                self.set_memory(match_object.group(0),instruction[1])
            except IndexError as e:
                print("Unexpected error processing instruction %s : %s"%(instruction,e))
                raise e

class ChipV2(Chip):

    def __init__(self):
        Chip.__init__(self,'')

    def set_memory(self,adress,value):
        binary_adress = bin(int(adress))[2:].rjust(Chip.MASK_LENGTH,'0')
        l_binary_adress = [*binary_adress]

        # if 1 in mask, the corresponding bit of the adress is set to 1 
        for i,b in enumerate(self.mask):
            if b == '1':
                l_binary_adress[i] = '1'
        
        adresses = []
        adresses.append(l_binary_adress)
        for i,b in enumerate(self.mask):
            if b == 'X':
                # duplication of adresses: one to keep same, the other to change the bit due to the mask 
                new_adresses = []
                for adr in adresses:
                    new_adresses.append(copy.deepcopy(adr))
                adresses = adresses + new_adresses
                s = int(len(adresses)/2)
                # first paquet of adresses don't change, in the second one we modify the bit corresponding to the mask
                for adr in adresses[s:]:
                    if adr[i] == '1':
                        adr[i] = '0'
                    else:
                        adr[i] = '1'

        for adr in adresses:
            self.memory[int(''.join(adr),2)] = int(value)

def first_star():
    instructions = get_puzzle_input('../data/inputday14.txt')
    state_machine = Chip('')
    
    for instruction in instructions:
        state_machine.manage_instruction(instruction)
    
    print("[*] memory sum : %s"%state_machine.compute_sum_values_inmemory())
    

def second_star():
    instructions = get_puzzle_input('../data/inputday14.txt')
    state_machine = ChipV2()
    
    for instruction in instructions:
        state_machine.manage_instruction(instruction)
    
    print("[**] memory sum : %s"%state_machine.compute_sum_values_inmemory())


if __name__ == '__main__':
    first_star()
    second_star()
