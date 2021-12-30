

def get_puzzle_input():
    with open('../data/inputday1.txt') as file:
        entries = []
        for entry in file:
            entries.append(int(entry.strip()))
    return entries

def first_star():
    entries = get_puzzle_input()
    for i,entry in enumerate(entries):
        for second_entry in entries[i:]:
            if entry + second_entry == 2020:
                print("entries : %s %s multiplicaton : %s"\
                    %(entry,second_entry,entry*second_entry))
                return

def second_star():
    entries = get_puzzle_input()
    for entry in entries:
        for second_entry in entries:
            for third_entry in entries:
                if entry + second_entry + third_entry == 2020:
                    print("entries : %s %s %s multiplicaton : %s"\
                        %(entry,second_entry,third_entry, entry*second_entry*third_entry))
                    return


if __name__ == "__main__":
    first_star()
    second_star()
