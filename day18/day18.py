from collections import deque 


def get_neighbours(cube):
    neighbours = set()
    for coord in range(3): # check each coord + 1 and -1 while the others remain equal
        side = [0, 0, 0]
        side[coord] = 1

        neigbour_before, neigbour_after = (), ()
        for i in range(3):
            neigbour_before += (cube[i] - side[i],)
            neigbour_after += (cube[i] + side[i],)

        neighbours.add(neigbour_before)
        neighbours.add(neigbour_after)

    return neighbours


def num_of_faces_unattached(cube, cubes_set):
    unnatached = 6
    
    neigbours = get_neighbours(cube)

    for n in neigbours:
        if n in cubes_set:
            unnatached -= 1
        
    return unnatached


def is_out_of_boundaries(cube, min_boudary, max_boundary):
    for coord in cube:
        if coord <= min_boudary or coord >= max_boundary:
            return True

    return False



def is_exterior(side, cubes_set, min_boundary, max_boundary):
    stack = deque()
    stack.append(side)

    visited = set()

    while(stack):
        candidate = stack.pop()

        if candidate in visited:
            continue

        visited.add(candidate)

        if candidate in cubes_set:
            continue

        if is_out_of_boundaries(candidate, min_boundary, max_boundary):
            return True

        neighbours = get_neighbours(candidate)
        for n in neighbours:
            stack.appendleft(n)

    return False


def num_of_exterior_faces(cube, cubes_set, min_boundary, max_boundary):
    exterior = 0
    
    neighbours = get_neighbours(cube)

    for side in neighbours:
        if is_exterior(side, cubes_set, min_boundary, max_boundary):
            exterior += 1

    return exterior



def main():

    #test_input= True
    test_input= False

    filename= "test_input.txt" if test_input else "input.txt"
    lines= open(filename, "r").read().splitlines()

    cubes_set = set()
    min_boundary = float("inf")
    max_boundary = float("-inf")

    

    for line in lines:
        x, y, z = line.split(",")
        x, y, z = int(x), int(y), int(z)

        cube = (x, y, z)
        cubes_set.add(cube)

        max_boundary = max(max_boundary, x, y, z)
        min_boundary = min(min_boundary, x, y, z)
        
    

    part_1 = 0
    part_2 = 0
    for cube in cubes_set:
        part_1 += num_of_faces_unattached(cube, cubes_set)
        part_2 += num_of_exterior_faces(cube, cubes_set, min_boundary, max_boundary)

        
    
    print("Challenge 1: ", part_1)
    print("Challenge 2: ", part_2)
    



if __name__ == "__main__":
    main()