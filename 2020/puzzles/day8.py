import collections


from collections import namedtuple

Cmd = namedtuple("Cmd","cmd param")

def get_puzzle_input(filename):
    with open(filename,'r') as file:
        instructions = []
        for line in file:
            instructions.append(Cmd(line.strip().split(' ')[0], int(line.strip().split(' ')[1])))
    return instructions            

def run_algo(instructions):
    accu = 0
    execution_pointer = 0
    fix = False
    memory_of_execution = []
    while True:
        if execution_pointer not in memory_of_execution:
            memory_of_execution.append(execution_pointer)
        else:
            break
        instruction = instructions[execution_pointer]
        if instruction.cmd == 'nop':
            execution_pointer += 1
        elif instruction.cmd == 'acc':
            accu += instruction.param
            execution_pointer += 1
        else: #jmp
            execution_pointer += instruction.param
        if execution_pointer == len(instructions):
            fix = True
            break
    return fix,accu

def first_star():
    instructions = get_puzzle_input('../data/inputday8.txt')
    _,accu = run_algo(instructions)
    print("[*] accumulator value : %s"%accu)

def second_star():
    instructions = get_puzzle_input('../data/inputday8.txt')
    
    for i,instr in enumerate(instructions):
        if instr.cmd == 'jmp':
            input = instructions.copy()
            cmd = input.pop(i)
            new_cmd = Cmd('nop',cmd.param)
            input.insert(i,new_cmd)
            fix,accu = run_algo(input)
            if fix:
                print("[**] Change jmp to nop : final accumulator value : %s"%accu)
                break
    
    for i,instr in enumerate(instructions):
        if instr.cmd == 'nop':
            input = instructions.copy()
            cmd = input.pop(i)
            new_cmd = Cmd('jmp',cmd.param)
            input.insert(i,new_cmd)
            fix,accu = run_algo(input)
            if fix:
                print("[**] Change nop to jmp : final accumulator value : %s"%accu)
                break

if __name__ == "__main__":
    first_star()
    second_star()
