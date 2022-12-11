

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


def touching(tail, head):
    spaces_around_head= [(head[0]-1, head[1]), (head[0]+1, head[1]), (head[0], head[1]-1), (head[0], head[1]+1)]
    corners_around_head= [(head[0]-1, head[1]-1), (head[0]+1, head[1]-1), (head[0]-1, head[1]+1), (head[0]+1, head[1]+1)]

    return tail in spaces_around_head or tail in corners_around_head

def overlapping(tail, head):
    return tail == head
    

def inline(tail, head):
    return tail[0] == head[0] or tail[1] == head[1]


def lineDirection(tail, head):
    if tail[0] == head[0]:
        if tail[1] > head[1]:
            return "up"
        else:
            return "down"
    else:
        if tail[0] > head[0]:
            return "left"
        else:
            return "right"

def getCorner(tail, head):
    """returns the corner where the head is in relation to the tail"""
    if head[0] > tail[0]: # if head is to the right of tail
        if head[1] < tail[1]: # if head is above tail
            return "top right"
        else: # if head is below tail
            return "bottom right"
    else: # if head is to the left of tail
        if head[1] < tail[1]: # if head is above tail
            return "top left"
        else: # if head is below tail
            return "bottom left"
            


def moveTail(tail, head):

    if overlapping(tail, head) or touching(tail, head):
        #print("not moved")
        return tail

    elif inline(tail, head): # if tail is inline with head
        #print("inline")
        if lineDirection(tail, head) == "up":
            return (tail[0], tail[1]-1)
        elif lineDirection(tail, head) == "down":
            return (tail[0], tail[1]+1)
        elif lineDirection(tail, head) == "left":
            return (tail[0]-1, tail[1])
        else: # if lineDirection(tail, head) == "right":
            return (tail[0]+1, tail[1])

    else: # if tail is not inline with head
        corner= getCorner(tail, head)
        #print("corner")
        if corner == "top right":
            return (tail[0]+1, tail[1]-1)

        elif corner == "bottom right":
            return (tail[0]+1, tail[1]+1)

        elif corner == "top left":
            return (tail[0]-1, tail[1]-1)

        else: # if corner == "bottom left":
            return (tail[0]-1, tail[1]+1)











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
            tail= moveTail(tail, head)
            
            #fancyGridPrint(head, tail, "small")
            tail_positions.add(tail) # add tail to set of positions if it is not already there
    #printTail(tail_positions)
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
            if direction == "U":
                head= (head[0], head[1]-1)

            elif direction == "D":
                head= (head[0], head[1]+1)

            elif direction == "L":
                head= (head[0]-1, head[1])

            elif direction == "R":
                head= (head[0]+1, head[1])

            cord[0]= head # store head 
            for tail_part in range(1, 10): # move all tails
                tail= cord[tail_part]
                previous_tail_after_moving= cord[tail_part-1]

                tail= moveTail(tail, previous_tail_after_moving)
                cord[tail_part]= tail # store tail part
                
            
            #fancyGridPrint(head, cord, "big")
            tail_positions.add(tail) # add last tail to set of positions if it is not already there
    #printTail(tail_positions)

    return len(tail_positions)











def main():
    """uncomment fancyGridPrint to see the path of the tail, and printTail to see the tail positions"""

    data= read_data()
    
    moves= sequenceOfMoves(data)

    tail_positions= followPath(moves)


    tail_positions_2= followPathBigCord(moves)



    print("challenge 1: ", tail_positions)
    print("challenge 2: ", tail_positions_2)





if __name__ == "__main__":
    main()