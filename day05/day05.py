import copy

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


def move_multiple(list_A, list_B, quantity):
    crates= list_A[-quantity:]
    list_A= list_A[:-quantity]
    list_B= list_B + crates
    return list_A, list_B




def do_moves(setup_in_dic, moves):
    setup_in_dic_copy= copy.deepcopy(setup_in_dic)

    for m in moves:
        splited= m.split(" ", 5)
        times= int(splited[1])
        list_A= splited[3]
        list_B= splited[5]
        
        setup_in_dic[list_A], setup_in_dic[list_B]= move(setup_in_dic[list_A], setup_in_dic[list_B], times) # challenge 1
        
        setup_in_dic_copy[list_A], setup_in_dic_copy[list_B]= move_multiple(setup_in_dic_copy[list_A], setup_in_dic_copy[list_B], times) # challenge 2

    return setup_in_dic, setup_in_dic_copy



def get_top(setup):
    result= ""
    for i in setup.values():
        result+= i.pop()

    return result






def main():
    setup, moves= read_data()


    setup_in_dic= store_setup(setup)

    final_setup, final_setup_2= do_moves(setup_in_dic, moves)

    top= get_top(final_setup)
    top_2= get_top(final_setup_2)

    print("challenge 1: ", top)
    print("challenge 2: ", top_2)





if __name__ == "__main__":
    main()