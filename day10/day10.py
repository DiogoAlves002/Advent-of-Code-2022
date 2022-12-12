def read_data():
    with open("day10/input.txt", "r") as f:
        data= f.read().splitlines()

    commands= []
    for l in data:
        
        line= l.split(" ")
        if len(line) == 2:
            command, value= line
            value= int(value)
        else:
            command= line[0]
            value= None
        commands.append((command, value))

    
    return commands


def interestingSignalStrengt(i, X):
    base= 20
    if i == base or ((i-base)%40 == 0 and i < 221):
        #print("interesting signal at i: ", i, " X: ", X)
        return i*X
    else:
        return 0


def incrementCycle(i, X):
    strenght = interestingSignalStrengt(i, X)
    i+=1
    return i, strenght


def executeProgram(commands):
    X=1
    i=1

    signal_strenght_sum= 0

    while commands:

        command= commands.pop(0)

        if command[0] == "addx":
            for e in range(2):
                i, strenght = incrementCycle(i, X)
                signal_strenght_sum += strenght
            X += command[1]
        elif command[0] == "noop":
            i, strenght = incrementCycle(i, X)
            signal_strenght_sum += strenght

        
    return signal_strenght_sum



def main():

    data= read_data()
    
    signal_strenght_sum= executeProgram(data)



    print("challenge 1: ", signal_strenght_sum)
    #print("challenge 2: ", tail_positions_2)





if __name__ == "__main__":
    main()