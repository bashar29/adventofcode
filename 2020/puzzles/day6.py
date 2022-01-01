
def get_puzzle_input():
    with open('../data/inputday6.txt','r') as file:
        groups = []
        group = []
        for line in file:
            if (line.strip() == ''):
                groups.append(group.copy())
                group.clear()
            else:
                group += [*line.strip()]
        groups.append(group)
    return groups

def get_puzzle_input_second_star():
    with open('../data/inputday6.txt','r') as file:
        groups = []
        group = []
        first_line_of_group = True
        for line in file:
            if (line.strip() == ''):
                groups.append(group.copy())
                group.clear()
                first_line_of_group = True
            else:
                if first_line_of_group:
                   group += [*line.strip()]
                   first_line_of_group = False
                else:
                    new_entries = [*line.strip()]
                    entries_to_delete = []
                    [entries_to_delete.append(entry) for entry in group if entry not in new_entries]
                    [group.remove(c) for c in entries_to_delete]
        groups.append(group)
    return groups            


def first_star():
    groups = get_puzzle_input()
    groups_unique_answers = []
    for g in groups:
        groups_unique_answers.append(set(g))
    nb_answers = 0
    for s in groups_unique_answers:
        nb_answers += len(s)
    print("[*] count : %s"%nb_answers)

def second_star():
    groups = get_puzzle_input_second_star()
    nb_answers = 0
    for g in groups:
        nb_answers += len(g)
    print("[**] count : %s"%nb_answers)
    

if __name__ == "__main__":
    first_star()
    second_star()
