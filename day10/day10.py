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


def sprite(X):
    return (X-1, X, X+1)

def pixel(X, i):
    if (i-1)%40 in sprite(X):
        return ("#", )
    else:
        return (".", )

def updateCycle(current_cycle, cycles, X, i):
    current_cycle += pixel(X, i)
    if i % 40 == 0:
        cycles.append(current_cycle)
        current_cycle= []
    return current_cycle, cycles



def executeProgram(commands):
    X=1
    i=1

    signal_strenght_sum= 0
    cycles= []
    current_cycle= ()

    while commands:

        command= commands.pop(0)

        if command[0] == "addx":
            for e in range(2):
                current_cycle, cycles = updateCycle(current_cycle, cycles, X, i)

                i, strenght = incrementCycle(i, X)
                signal_strenght_sum += strenght
            X += command[1]
        elif command[0] == "noop":
            current_cycle, cycles = updateCycle(current_cycle, cycles, X, i)


            i, strenght = incrementCycle(i, X)
            signal_strenght_sum += strenght

        
    return signal_strenght_sum, cycles


def printCycles(cycles):
    for cycle in cycles:
        print("".join(cycle))


def main():

    data= read_data()
    
    signal_strenght_sum, cycles= executeProgram(data)




    print("challenge 1: ", signal_strenght_sum)
    print("challenge 2: ")
    printCycles(cycles)





if __name__ == "__main__":
    main()