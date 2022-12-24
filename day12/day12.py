
def read_data():
    with open("day12/input.txt", "r") as f:
        grid= f.read().splitlines()

    return grid


def starting_Goal_Position(grid):
    start= None
    goal= None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if start and goal:
                return start, goal

            elif grid[y][x] == "S":
                start= (x, y)
            elif grid[y][x] == "E":
                goal= (x, y)


def printGrid(grid, current):
    print("------------------")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) == current:
                print("☆", end="")
            else:
                print(grid[y][x], end="")
        print()
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


def printPath(grid, path):
    print("##################")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in path:
                index= path.index((x, y))
                if index == len(path) - 1:
                    print("E", end="")
                else:
                    direction= getDirection(path[index], path[index+1])
                    print(direction, end="")
            else:
                print(".", end="")
        print()
    print("##################")



def canMove(grid, x1, y1, x2, y2):
    """the elevation of the destination square can be at most one higher than the elevation of your current square"""

    if grid[y1][x1] == "S": # start has elevation "a"
        if ord("a") + 1 >= ord(grid[y2][x2]):
            return True
        return False

    if grid[y2][x2] == "E": # end has elevation "z"
        if ord(grid[y1][x1]) + 1 >= ord("z"):
            return True
        return False

    if ord(grid[y1][x1]) + 1 >= ord(grid[y2][x2]):
        return True

    return False

def neighbours(grid, current_square):
    x, y= current_square
    neighbours= []

    # check left
    if x > 0 and canMove(grid, x, y, x-1, y):
        #print("can move left")
        neighbours.append((x-1, y))

    # check right
    if x < len(grid[0]) - 1 and canMove(grid, x, y, x+1, y):
        #print("can move right")
        neighbours.append((x+1, y))

    # check up
    if y > 0 and canMove(grid, x, y, x, y-1):
        #print("can move up")
        neighbours.append((x, y-1))

    # check down
    if y < len(grid) - 1 and canMove(grid, x, y, x, y+1):
        #print("can move down")
        neighbours.append((x, y+1))

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
    while current != start:
        path.append(current)
        current= previous[current]

    path.append(start)
    path.reverse()

    return path


def main():


    grid= read_data()

    start, goal= starting_Goal_Position(grid)

    path= findPath(grid, start, goal)
    
    printPath(grid, path)

    steps= len(path) - 1

    print("challenge 1: ", steps)


    #print("challenge 1: ", monkey_business)
    #print("challenge 2: ", monkey_business_2)




if __name__ == "__main__":
    main()