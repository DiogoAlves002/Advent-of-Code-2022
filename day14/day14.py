

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
    bottom += 2
    return bottom, rocks


def read_data():
    #with open("day14/test_input.txt", "r") as f:
    with open("day14/input.txt", "r") as f:

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


def match_sand(sand_X, sand_Y, sitting_sand):
    top= None
    for sand in sitting_sand:
        if sand[0] == sand_X and sand[1] >= sand_Y: # ignore sand above the current drop point
            if top is None or sand[1] < top: # top of the pile
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


def blocked_by_rock(sand, rocks):
    sand_X, sand_Y= sand
    for rock in rocks:
        start= rock[0]
        for i in range(1, len(rock)):
            finish= rock[i]
            if match_horizontal_rock(sand_X, start, finish) and match_vertical_rock(sand_Y, start, finish):
                return True # blocked by a rock
            start= finish
    return False

def slide_sand(sand, bottom, rocks, sitting_sand, direcion):
    sand_X, sand_Y= sand
    sand_Y += 1
    sand_X += 1 if direcion == "right" else -1
    
    if blocked_by_rock((sand_X, sand_Y), rocks):
        return -1

    sand_top= match_sand(sand_X, sand_Y, sitting_sand)
    if sand_top is not None and sand_top == sand_Y:
        return -1 # blocked by sand

    return drop_sand((sand_X, sand_Y), bottom, rocks, sitting_sand)


def update_bottom(rocks, sand_X, bottom):
    rock_bottom= rocks[-1]

    current_bottom= 0
    for point in rock_bottom:
        if point[1] > current_bottom:
            current_bottom= point[1]

    if current_bottom != bottom: # bottom has not been added yet
        rocks.append(((sand_X-2, bottom), (sand_X+2, bottom)))
        return rocks
        
    rock_bottom_start, rock_bottom_finish= rock_bottom
    if rock_bottom_start[0] >= sand_X:
        rock_bottom_start= (sand_X-2, bottom)
    else:
        rock_bottom_finish= (sand_X+2, bottom)
    
    rocks[-1]= (rock_bottom_start, rock_bottom_finish)
    return rocks

    


def drop_sand(sand, bottom, rocks, sitting_sand):
    """returns the Coordinate of the sand that has fallen"""
    sand_X, sand_Y= sand
    top= None
    for rock in rocks:
        start= rock[0]
        for i in range(1, len(rock)):
            finish= rock[i]
            if match_horizontal_rock(sand_X, start, finish):
                rock_top= get_rock_top(start, finish)
                if rock_top-1 >= sand_Y and(top is None or top > rock_top-1):
                    top= rock_top-1
            start= finish
            
    sand_top= match_sand(sand_X, sand_Y, sitting_sand)
    if sand_top is not None:
        if sand_top == 0: # blocked the entrance
            return None
        if top is None or top > sand_top- 1:
            top= sand_top- 1


    if top is None: # sand has fallen off to the void
        if bottom is None: # challenge 1
            return None

        rocks= update_bottom(rocks, sand_X, bottom)
        top = bottom-1

    
    fallen_sand= (sand_X, top) # sand has fallen to the top of a rock or sand
    
    # now we need to check if the sand can slide to the left or right
    slide_left= slide_sand(fallen_sand, bottom, rocks, sitting_sand, "left")
    if slide_left != -1:
        return slide_left
    
    if slide_left == -1: # sand is blocked by a rock or sand
        slide_right= slide_sand(fallen_sand, bottom, rocks, sitting_sand, "right")
        if slide_right != -1:
            return slide_right

    return fallen_sand


def print_rock(rocks, x, y):
    for rock in rocks:
        start= rock[0]
        for i in range(1, len(rock)):
            finish= rock[i]
            if match_horizontal_rock(x, start, finish) and match_vertical_rock(y, start, finish):
                return "#"
            start= finish
    return None

def print_sand(sitting_sand, x, y):
    for sand in sitting_sand: # print sand
        if sand[0] == x and sand[1] == y:
            return "o"
    return None

def draw_grid(rocks, sitting_sand, dimensions= ((494, 0), (503, 9)), drop= (500, 0)):

    grid= ['\n']
    for i in range(3): # print grid labels
        s= str(dimensions[0][0])[i]
        f= str(dimensions[1][0])[i]
        d= str(drop[0])[i]
        if dimensions[1][1] + 1 > 9:
            grid.append(" ")
            if dimensions[1][1] + 1 > 99:
                grid.append(" ")
        #grid.append(" ") # needed for test input but not for challenge input (dunno why but tbh dont really care)
        grid.append("  "+ s + " "*(drop[0] - dimensions[0][0] - 1) + d + " "* (dimensions[1][0] - drop[0] - 1) + f + "\n")

    for y in range(dimensions[0][1], dimensions[1][1] + 1):
        grid.append(str(y)+ " ")
        if y < 10:
            grid.append(" ")
        if y < 100:
            grid.append(" ")
        for x in range(dimensions[0][0], dimensions[1][0] + 1):

            if (x, y) == drop:
                grid.append("+")
                continue

            rock= print_rock(rocks, x, y)
            if rock:
                grid.append(rock)
                continue


            sand= print_sand(sitting_sand, x, y)
            if sand:
                grid.append(sand)
                continue

            grid.append(".")
        grid.append("\n")

    print("".join(grid))


def challenge(rocks, start, bottom= None):
    units= 0
    sitting_sand= set()

    #dimensions= ((488, 0), (508, 11)) # for test input
    dimensions=((300, 0), (700, 200)) # for final input
    while True:
        sand= drop_sand(start, bottom, rocks, sitting_sand)
        if sand is None: # fell to the void or blocked the entrance
            break
        sitting_sand.add(sand)
        
        units+= 1

        if units % 100 == 0:
            print(units)
    draw_grid(rocks, sitting_sand, dimensions, drop= start) # final grid
    return units
    





def main():

    bottom, rocks= read_data()
    start= (500, 0)

    units= challenge(rocks, start)
    units_2 = challenge(rocks, start, bottom)


    print("Challenge 1: ", units)
    print("Challenge 2: ", units_2)




        



if __name__ == "__main__":
    main()