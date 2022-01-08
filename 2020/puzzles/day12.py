
def get_puzzle_input(filename):
    with open(filename,'r') as file:
        instructions = [line.strip() for line in file]
    return instructions

class Ferry:
    def __init__(self):
        self.leading = 0
        self.position = [0,0]

    def follow_instruction(self,instruction):
        match instruction[:1]:
            case 'N':
                self.position[1] += int(instruction[1:])
            case 'S':
                self.position[1] -= int(instruction[1:])
            case 'E':
                self.position[0] += int(instruction[1:])
            case 'W':
                self.position[0] -= int(instruction[1:])
            case 'L':
                self.leading += int(instruction[1:])
                self.leading = self.leading % 360
            case 'R':
                self.leading -= int(instruction[1:])
                self.leading = self.leading % 360
            case 'F':
                if self.leading == 0:
                    self.position[0] += int(instruction[1:])
                elif self.leading == 90:
                    self.position[1] += int(instruction[1:])
                elif self.leading == 180:
                    self.position[0] -= int(instruction[1:])
                elif self.leading == 270:
                    self.position[1] -= int(instruction[1:])

    def manahattan_distance(self):
        print(self.position)
        return (abs(self.position[0]) + abs(self.position[1]))

class TrueFerry(Ferry):

    def __init__(self):
        Ferry.__init__(self)
        self.waypoint = [10,1]

    def follow_instruction(self, instruction):
        match instruction[:1]:
            case 'N':
                self.waypoint[1] += int(instruction[1:])
            case 'S':
                self.waypoint[1] -= int(instruction[1:])
            case 'E':
                self.waypoint[0] += int(instruction[1:])
            case 'W':
                self.waypoint[0] -= int(instruction[1:])
            case 'L':
                self.rotation_around_ferry(int(instruction[1:]))
            case 'R':
                self.rotation_around_ferry(-int(instruction[1:]))
            case 'F':
                multiplicator = int(instruction[1:])
                self.position[0] += multiplicator*self.waypoint[0]
                self.position[1] += multiplicator*self.waypoint[1]

    def rotation_around_ferry(self,angle):
        if angle % 360 == 90:
            new_x = -self.waypoint[1]
            new_y = self.waypoint[0]
            self.waypoint = [new_x,new_y]
        elif angle % 360 == 180:
            new_x = -self.waypoint[0]
            new_y = -self.waypoint[1]
            self.waypoint = [new_x,new_y]
        elif angle % 360 == 270:
            new_x = self.waypoint[1]
            new_y = -self.waypoint[0]
            self.waypoint = [new_x,new_y]


def first_star():
    instructions = get_puzzle_input('../data/inputday12.txt')
    ferry = Ferry()
    for inst in instructions:
        ferry.follow_instruction(inst)
    print("[*] Manhattan distance : %s"%ferry.manahattan_distance())

def second_star():
    instructions = get_puzzle_input('../data/inputday12.txt')
    ferry = TrueFerry()
    for inst in instructions:
        ferry.follow_instruction(inst)
    print("[**] Manhattan distance : %s"%ferry.manahattan_distance())

if __name__ == '__main__':
    first_star()
    second_star()
