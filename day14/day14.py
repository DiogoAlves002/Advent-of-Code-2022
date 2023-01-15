
import time


def store_rocks(lines):
    """return the grid height and a list of tuples, each tuple is a line of rocks, and contains tuples of (x, y) points that make that line"""
    rocks= []
    bottom= 0
    for line in lines:
        points= line.split(" -> ")
        t= tuple() # line of rocks
        for point in points:
            x, y= point.split(",")
            t= t + ((int(x), int(y)), ) # add point to line
            if int(y) > bottom:
                bottom= int(y)
        rocks.append(t)
    #print(rocks)
    return bottom, rocks


def read_data():
    with open("day14/test_input.txt", "r") as f:
    #with open("day14/input.txt", "r") as f:

        lines= f.read().splitlines()

    bottom, rocks= store_rocks(lines)

    return bottom, rocks


def match_horizontal_rock(sand_X, start, finish):
    """returns True if sand_X is between the start and finish of the rock X coordinates"""

    start_X, start_Y= start
    finish_X, finish_Y= finish

    if start < finish: # rock is going right
        if sand_X >= start_X and sand_X <= finish_X:
            return True
    elif start > finish : # rock is going left
        if sand_X >= finish_X and sand_X <= start_X:
            return True
    else: # rock is vertical
        if sand_X == start_X:
            return True
    return False

def match_vertical_rock(sand_Y, start, finish):
    """returns True if sand_Y is between the start and finish of the rock Y coordinates"""

    start_X, start_Y= start
    finish_X, finish_Y= finish

    if start < finish: # rock is going down
        if sand_Y >= start_Y and sand_Y <= finish_Y:
            return True
    elif start > finish : # rock is going up
        if sand_Y >= finish_Y and sand_Y <= start_Y:
            return True
    else: # rock is horizontal
        if sand_Y == start_Y:
            return True
    return False


def match_sand(sand_X, sitting_sand):
    top= None
    for sand in sitting_sand:
        if sand[0] == sand_X:
            if top is None or sand[1] < top:
                top= sand[1]
    return top


def get_rock_top(start, finish):
    """returns the Coordinate top of the rock"""
    start_Y= start[1]
    finish_Y= finish[1]

    if start_Y < finish_Y:
        return start_Y
    else:
        return finish_Y


def slide_sand(sand, bottom, rocks, sitting_sand, direcion):
    top = None
    if direcion == "left":
        sand_X, sand_Y= sand
        sand_X -= 1
        sand_Y += 1
        for rock in rocks:
            start= rock[0]
            for i in range(1, len(rock)):
                finish= rock[i]
                #print("start: ", start, "finish: ", finish)
                if match_horizontal_rock(sand_X, start, finish):
                    if top is None or (top > get_rock_top(start, finish)-1 and get_rock_top(start, finish)-1 > sand_Y):
                        top= get_rock_top(start, finish)-1
                start= finish

        sand_top= match_sand(sand_X, sitting_sand)
        if sand_top is not None:
            if top is None or top > sand_top- 1:
                top= sand_top- 1
        
        if top is None: # sand has fallen off to the void
            print("fallen off while sliding", sand_X, top)
            return None       


    else:
        sand_X, sand_Y= sand
        sand_X += 1
    
    return drop_sand((sand_X, sand_Y), bottom, rocks, sitting_sand)



def drop_sand(sand, bottom, rocks, sitting_sand):
    """returns the Coordinate of the sand that has fallen"""
    sand_X, sand_Y= sand
    top= None
    for rock in rocks:
        start= rock[0]
        for i in range(1, len(rock)):
            finish= rock[i]
            #print("start: ", start, "finish: ", finish)
            if match_horizontal_rock(sand_X, start, finish):
                if top is None or (top > get_rock_top(start, finish)-1 and get_rock_top(start, finish)-1 > sand_Y):
                    top= get_rock_top(start, finish)-1
            start= finish
    #print("top rock", top)
    sand_top= match_sand(sand_X, sitting_sand)
    if sand_top is not None:
        if top is None or top > sand_top- 1:
            top= sand_top- 1


    fallen_sand= (sand_X, top) # sand has fallen to the top of the rock or sand

    # now we need to check if the sand can slide to the left or right
    slide_left= slide_sand(fallen_sand, bottom, rocks, sitting_sand, "left")
    if slide_left:
        return slide_left
    
    #slide_right= slide_sand(fallen_sand, bottom, rocks, sitting_sand, "right")
    #if slide_right:
    #    return slide_right

    if top is None: # sand has fallen off to the void
        print("fallen off", sand_X, top)
        return None

    #print("fallen sand", sand_X, top)
    return fallen_sand


def print_rock(rocks, x, y):
    for rock in rocks:
        start= rock[0]
        for i in range(1, len(rock)):
            finish= rock[i]
            if match_horizontal_rock(x, start, finish) and match_vertical_rock(y, start, finish):
                print("#", end="")
                return False
            start= finish
    return True

def print_sand(sitting_sand, x, y):
    for sand in sitting_sand: # print sand
        if sand[0] == x and sand[1] == y:
            print("o", end="")
            return False
    return True

def draw_grid(rocks, sitting_sand, dimensions= ((494, 0), (503, 9)), drop= (500, 0)):

    print("")
    for i in range(3): # print grid labels
        s= str(dimensions[0][0])[i]
        f= str(dimensions[1][0])[i]
        d= str(drop[0])[i]
        if dimensions[1][1] + 1 > 9:
            print(" ", end="")
            if dimensions[1][1] + 1 > 99:
                print(" ", end="")
        print("  "+ s + " "*(drop[0] - dimensions[0][0] - 1) + d + " "* (dimensions[1][0] - drop[0] - 1) + f)

    for y in range(dimensions[0][1], dimensions[1][1] + 1):
        print(y, end=" ")
        if y < 10:
            print(" ", end="")
        if y < 100:
            print(" ", end="")
        for x in range(dimensions[0][0], dimensions[1][0] + 1):

            if (x, y) == drop: # print drop
                print("+", end="")
                continue

            no_rock= print_rock(rocks, x, y) # print rocks
            
            if no_rock: # print sand
                no_sand= print_sand(sitting_sand, x, y)

            if no_rock and no_sand:
                print(".", end="")
        print("")


def challenge_1(bottom, rocks, start= (500, 0)):
    units= 0
    sitting_sand= []

    dimensions= ((494, 0), (503, 9)) # for test input
    #dimensions=((400, 0), (600, 200)) # for final input
    while True:
        sand= drop_sand(start, bottom, rocks, sitting_sand)
        if sand is None: # fell to the void
            break
        sitting_sand.append(sand)
        
        draw_grid(rocks, sitting_sand, dimensions, drop= start)

        units+= 1
        time.sleep(1)



    return units
    


def challenge_2(all_packets): 
    pass




def main():

    bottom, rocks= read_data()

    units= challenge_1(bottom, rocks)

    print("Challenge 1: ", units)

    #draw_grid(rocks, [(500, 8), (500, 7), (499, 8)])



        



if __name__ == "__main__":
    main()