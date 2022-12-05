
def read_data():
    with open('day05/input.txt') as f:
        data = f.read().splitlines()
        
        setup= []
        moves= []
        type = "setup"
        for d in data:
            if d == "":
                type= "moves"
                continue
            setup, moves = store_data(type, setup, moves, d)
    return setup[::-1], moves

def store_data(type, setup, moves, data):
    if type == "setup":
        setup.append(data)
    elif type == "moves":
        moves.append(data)

    return setup, moves


def store_setup(setup):
    dic= {}

    index= setup[0].split(" ")
    index= list(filter(None, index)) # remove empty strings
    for i in index:
        dic[i]= []

    for row in setup[1:]:
        print(row)
        for i in index:
            box= row[1]
            row= row[3:]
            if i != index[-1]:
                row= row[1:]
            if box != " ":
                dic[i].append(box)
    return(dic)






def move(list_A, list_B, times):
    for i in range(times):
        list_B.append(list_A.pop())
    return list_A, list_B




def do_moves(setup_in_dic, moves):
    for m in moves:
        splited= m.split(" ", 5)
        times= int(splited[1])
        list_A= int(splited[3])
        list_B= int(splited[5])

        # TODO do moves







def main():
    setup, moves= read_data()

    print(setup)
    print(moves)


    setup_in_dic= store_setup(setup)

    do_moves(setup_in_dic, moves)







if __name__ == "__main__":
    main()