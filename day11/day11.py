def read_data():
    with open("day11/input.txt", "r") as f:
        data= f.read().splitlines()

    monkeys= {}


    for l in data:
        if l.startswith("Monkey"):
            position= l.index(" ") + 1
            monkey= int(l[position: position+1])

            monkeys[monkey]= []
        
        elif l.startswith("  Starting"):
            position= l[l.index(": ") + 1: ]
            values= position.replace(" ", "").split(",")

            starting = [eval(i) for i in values] # convert to int

            monkeys[monkey].append(starting)

        elif l.startswith("  Operation"):
            operation= l[l.index("old ") + 4: ]
            operator, value= operation.split(" ")
            
            if value.isdigit():
                value= int(value)

            operation= (operator, value)

            monkeys[monkey].append(operation)

        elif l.startswith("  Test"):
            test= l[l.index(":") + 1: ]
            
            digits= [a for a in test if a.isdigit()]
            value= (int("".join(digits)), )
            
            monkeys[monkey].append(value)

        elif l.startswith("    If"):
            monkey_to_throw= (int(l[-1]), )
            
            monkeys[monkey].append(monkey_to_throw)

    return monkeys


def testThrow(test, item):
    return item % test[0] == 0

    

def reliefItem(item):
    item= item//3
    return item



def throwStuff(monkeys, monkey, relief):
    count_inspect= 0

    starting= monkeys[monkey][0]
    if len(starting) == 0:
        return monkeys, count_inspect
    operation= monkeys[monkey][1]
    test= monkeys[monkey][2]
    monkey_to_throw_if_true= monkeys[monkey][3]
    monkey_to_throw_if_false= monkeys[monkey][4]

    while starting:
        item= starting.pop(0)
        count_inspect+= 1
        if operation[0] == "+":
            if type(operation[1]) == int:
                item+= operation[1]
            else:
                item+= item
        elif operation[0] == "*":
            if type(operation[1]) == int:
                item*= operation[1]
            else:
                item*= item
        
        if relief:
            item= reliefItem(item)            

        if (testThrow(test, item)):
            monkey_receiving= monkey_to_throw_if_true[0]
        else:
            monkey_receiving= monkey_to_throw_if_false[0]
        
        monkey_receiving_stuff= monkeys[monkey_receiving].pop(0)

        monkey_receiving_stuff.append(item)

        monkeys[monkey_receiving]= [monkey_receiving_stuff] + monkeys[monkey_receiving]

    return monkeys, count_inspect



def monkeysRound(monkeys, monkeys_count_inspect, relief):
    for monkey in monkeys:
        throw= throwStuff(monkeys, monkey, relief)
        monkeys, count_inspect= throw
        #monkeys, count_inspect= throwStuff(monkeys, monkey)

        if not monkey in monkeys_count_inspect:
            monkeys_count_inspect[monkey]= count_inspect
        else:
            monkeys_count_inspect[monkey] += count_inspect

    return monkeys, monkeys_count_inspect

def monkeyBusiness(monkeys_count_inspect):
    values= monkeys_count_inspect.values()
    values= sorted(values, reverse= True)
    return values[0] * values[1]



def main():

    """ monkeys= read_data()
    print(monkeys)

    monkeys_count_inspect= {}
    for i in range(1, 21):
        monkeys, monkeys_count_inspect= monkeysRound(monkeys, monkeys_count_inspect, True)
    
    monkey_business= monkeyBusiness(monkeys_count_inspect) """



    monkeys_2= read_data()
    print(monkeys_2)

    monkeys_count_inspect_2= {}
    for i in range(1, 10_001):
        monkeys_2, monkeys_count_inspect_2= monkeysRound(monkeys_2, monkeys_count_inspect_2, False)
        print("round ", i, ": ", monkeys_count_inspect_2)
        #print(monkeys_2)
    
    monkey_business_2= monkeyBusiness(monkeys_count_inspect_2)


    #print("challenge 1: ", monkey_business)
    print("challenge 2: ", monkey_business_2)




if __name__ == "__main__":
    main()