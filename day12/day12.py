
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


def canMove(grid, x1, y1, x2, y2):
    return grid[y1][x1] >= grid[y2][x2] + 1

def neighbours(grid, x, y):
    neighbours= []

    # check left
    if x > 0 and canMove(grid, x, y, x-1, y):
        neighbours.append((x-1, y))

    # check right
    if x < len(grid[0]) - 1 and canMove(grid, x, y, x+1, y):
        neighbours.append((x+1, y))

    # check up
    if y > 0 and canMove(grid, x, y, x, y-1):
        neighbours.append((x, y-1))

    # check down
    if y < len(grid) - 1 and canMove(grid, x, y, x, y+1):
        neighbours.append((x, y+1))

    return neighbours



def main():


    grid= read_data()

    start, goal= starting_Goal_Position(grid)


    #print("challenge 1: ", monkey_business)
    #print("challenge 2: ", monkey_business_2)




if __name__ == "__main__":
    main()