

def read_data():
    with open("day09/input.txt", "r") as f:
        data= f.read().splitlines()
    
    return data


def sequenceOfMoves(data):
    moves= []
    for line in data:
        direction, distance= line.split()
        distance= int(distance)
        moves.append((direction, distance))
    return moves


def distance(tail, head):
    return abs(tail[0] - head[0]) + abs(tail[1] - head[1])

def diagonal(tail, head):
    if tail[0] == head[0] or tail[1] == head[1] or distance(tail, head) > 2:
        return False
    else:
        return True

def adjacent(tail, head):
    if distance(tail, head) == 1:
        return True
    else:
        return False



def moveTail(tail, previous, head, head_direction):

    # not really happy with this code, but it works
    if tail == previous:
        return tail

    if tail[0] == previous[0] and tail[1] == previous[1]:
        return tail

    
    if diagonal(tail, head):
        return tail

    if not diagonal(tail, previous) and diagonal(tail, head):
        return tail

    if diagonal(tail, previous) and adjacent(tail, head):
        return tail



    if head_direction == "U":
        if tail[0] == previous[0]: # same column, head pulls it up
            if tail[1] == previous[1]-1: # tail is one above head, so the head will just cover it
                return tail
            return (tail[0], tail[1]-1)
        else: # different column, head pulls it diagonally to the same column and up
            return (previous[0], tail[1]-1)

    elif head_direction == "D":
        if tail[0] == previous[0]:
            if tail[1] == previous[1]+1:
                return tail
            return (tail[0], tail[1]+1)
        else:
            return (previous[0], tail[1]+1)

    elif head_direction == "L":
        if tail[1] == previous[1]:
            if tail[0] == previous[0]-1:
                return tail
            return (tail[0]-1, tail[1])
        else:
            return (tail[0]-1, previous[1])

    elif head_direction == "R":
        if tail[1] == previous[1]:
            if tail[0] == previous[0]+1:
                return tail
            return (tail[0]+1, tail[1])
        else:
            return (tail[0]+1, previous[1])

    else:
        print("ERROR: unknown direction: ", head_direction)
        exit(1)




def fancyGridPrint(head, tail, dimension):
    if dimension == "small":
        for alture in range (-4, 1):
            for largura in range(0,6):
                if (largura, alture) == head:
                    print("H", end="")
                elif (largura, alture) == tail:
                    print("T", end="")
                else:
                    print(".", end="")
            print()
        print()
        
    elif dimension == "big":
        for alture in range (-15, 6):
            for largura in range(-11, 15):
                if (largura, alture) == head:
                    print("H", end="")
                elif (largura, alture) in tail.values():
                    tail_part= list(tail.keys())[list(tail.values()).index((largura, alture))]
                    print(str(tail_part), end="")
                else:
                    print(".", end="")
            print()
        print()



def followPath(moves):
    head= (0,0)
    tail= (0,0)

    tail_positions= set()
    tail_positions.add(tail)

    for move in moves:
        direction, distance= move
        for i in range(distance):
            previous= tuple(head) # copy of head with another reference
            if direction == "U":
                head= (head[0], head[1]-1)

            elif direction == "D":
                head= (head[0], head[1]+1)

            elif direction == "L":
                head= (head[0]-1, head[1])

            elif direction == "R":
                head= (head[0]+1, head[1])
            tail= moveTail(tail, previous, head, direction)
            
            #fancyGridPrint(head, tail, "small  ")
            tail_positions.add(tail) # add tail to set of positions if it is not already there
    return len(tail_positions)


def fillCordDict():
    cord= {}

    for i in range(0, 10):
        cord[i]= (0,0)

    return cord


def printTail(tail):
    for altura in range (-15, 6):
        for largura in range(-11, 15):
            if (largura, altura) in tail:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def followPathBigCord(moves):
    head= (0,0)
    cord= fillCordDict()
    tail_positions= set()

    for move in moves:
        direction, distance= move
        for i in range(distance):
            previous= tuple(cord[0]) # copy of head with another reference
            if direction == "U":
                head= (head[0], head[1]-1)

            elif direction == "D":
                head= (head[0], head[1]+1)

            elif direction == "L":
                head= (head[0]-1, head[1])

            elif direction == "R":
                head= (head[0]+1, head[1])
            print("direction: ", direction)
            print("head: ", head)
            cord[0]= head
            for tail_part in range(1, 10): # move all tails
                print("tail_part: ", tail_part)
                tail= cord[tail_part]
                next_previous= cord[tail_part]
                print("tail: ", tail)
                print("next_previous: ", next_previous)

                previous_tail= cord[tail_part-1]
                print("previous_tail: ", previous_tail)
                print("previous: ", previous)
                tail= moveTail(tail, previous, previous_tail, direction)
                print("tail after moving: ", tail)
                cord[tail_part]= tail
                previous= tuple(next_previous)
                print("----")
            print("")
                
            
            fancyGridPrint(head, cord, "big")
            tail_positions.add(tail) # add last tail to set of positions if it is not already there
    printTail(tail_positions)

    return len(tail_positions)











def main():
    data= read_data()
    
    moves= sequenceOfMoves(data)

    tail_positions= followPath(moves)


    tail_positions_2= followPathBigCord(moves)



    print("challenge 1: ", tail_positions)
    print("challenge 2: ", tail_positions_2)





if __name__ == "__main__":
    main()