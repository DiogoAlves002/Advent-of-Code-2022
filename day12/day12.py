
def read_data():
    with open("day12/input.txt", "r") as f:
        grid= f.read().splitlines()

    return grid


def starting_goal_Position(grid):
    start= None
    goal= None
    for y in range(len(grid)):
        if start and goal:
            return start, goal
            
        if "S" in grid[y]:
            start= (grid[y].index("S"), y)

        if "E" in grid[y]:
            goal= (grid[y].index("E"), y)



def all_starting_goal_positions(grid):
    start= []
    goal= None
    for y in range(len(grid)):
        if not "a" in grid[y] and not "S" in grid[y] and not "E" in grid[y]: # may speed up a bit
            continue

        # get all x coordinate of occurences of "a" and "S"
        a_s= [x for x in range(len(grid[y])) if grid[y][x] == "a" or grid[y][x] == "S"] 

        # add starting positions if there are any
        start.extend([(x, y) for x in a_s if a_s])

        # get goal position if there is any
        goal= (grid[y].index("E"), y) if "E" in grid[y] else goal


    return start, goal


def printGrid(grid, current):
    print("------------------")
    for y in range(len(grid)):
        if y != current[1]:
            print(grid[y])
            continue

        x= current[0]
        print(grid[y][:x] + "☆" + grid[y][x+1:])
    print("------------------")


def getDirection(current, next):
    x1, y1= current
    x2, y2= next

    if x1 == x2:
        if y1 < y2:
            return "V"
        else:
            return "^"
    else:
        if x1 < x2:
            return ">"
        else:
            return "<"


def chooseChar(grid, x, y, path):
    if (x, y) not in path:
        return "."
    elif grid[y][x] == "E":
        return "E"
    else:
        index= path.index((x, y))
        return getDirection(path[index], path[index+1])


def printPath(grid, path):
    print("")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            direction= chooseChar(grid, x, y, path)
            print(direction, end="")
        print()
    print("")



def canMove(grid, x1, y1, x2, y2):
    """the elevation of the destination square can be at most one higher than the elevation of your current square"""

    if grid[y1][x1] == "S": # start has elevation "a"
        return ord("a") + 1 >= ord(grid[y2][x2])

    if grid[y2][x2] == "E": # end has elevation "z"
        return ord(grid[y1][x1]) + 1 >= ord("z")

    return ord(grid[y1][x1]) + 1 >= ord(grid[y2][x2])

def neighbours(grid, current_square):
    x, y= current_square
    neighbours= []

    # check up
    if y > 0 and canMove(grid, x, y, x, y-1):
        #print("can move up")
        neighbours.append((x, y-1))

    # check down
    if y < len(grid) - 1 and canMove(grid, x, y, x, y+1):
        #print("can move down")
        neighbours.append((x, y+1))

    # check left
    if x > 0 and canMove(grid, x, y, x-1, y):
        #print("can move left")
        neighbours.append((x-1, y))

    # check right
    if x < len(grid[0]) - 1 and canMove(grid, x, y, x+1, y):
        #print("can move right")
        neighbours.append((x+1, y))

    return neighbours


def findPath(grid, start, goal):
    queue= [start]
    previous= {start: None}

    while queue:
        current= queue.pop(0)
        #print("current: ", current)
        #printGrid(grid, current)

        if current == goal:
            break

        for neighbour in neighbours(grid, current):
            #print("neighbour: ", neighbour)
            if neighbour not in previous:
                queue.append(neighbour)
                previous[neighbour]= current

    path= []
    if current != goal:
        return None

    while current != start:
        path.append(current)
        current= previous[current]

    path.append(start)
    path.reverse()

    return path

def findQuickestPath(grid, start, goal):
    steps= None
    quickest_path= None

    for s in start:
        #print("steps: ", steps)
        path= findPath(grid, s, goal)
        if path is None:
            #print("no path found")
            continue
        if steps is None or len(path)-1 < steps:
            quickest_path= path
            steps= len(path) -1

    return quickest_path, steps




def challenge1(grid):
    start, goal= starting_goal_Position(grid)

    path= findPath(grid, start, goal)
    printPath(grid, path)

    steps= len(path) - 1
    print("challenge 1: ", steps)


def challenge2(grid):
    starts, goal= all_starting_goal_positions(grid)

    quickest_path, steps= findQuickestPath(grid, starts, goal)
    printPath(grid, quickest_path)

    print("challenge 2: ", steps)




def main():


    grid= read_data()

    challenge1(grid)
    challenge2(grid)




if __name__ == "__main__":
    main()