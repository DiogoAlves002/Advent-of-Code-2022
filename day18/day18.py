class cube():
    def __init__(self, x, y, z, unattached_faces):
        self.x = x
        self.y = y
        self.z = z
        self.unattached_faces = unattached_faces


    def is_attached(self, other_cube):
        if self.x == other_cube.x and self.y == other_cube.y and (self.z == other_cube.z + 1 or self.z == other_cube.z - 1):
            return True

        if self.x == other_cube.x and self.z == other_cube.z and (self.y == other_cube.y + 1 or self.y == other_cube.y - 1):
            return True

        if self.z == other_cube.z and self.y == other_cube.y and (self.x == other_cube.x + 1 or self.x == other_cube.x - 1):
            return True

        return False


def main():

    #test_input= True
    test_input= False

    filename= "test_input.txt" if test_input else "input.txt"
    lines= open(filename, "r").read().splitlines()

    cubes = []

    for line in lines:
        x, y, z = line.split(",")
        c = cube(int(x), int(y), int(z), 6)
        for other_c in cubes:
            if c.is_attached(other_c):
                c.unattached_faces -= 1
                other_c.unattached_faces -= 1

            if c.unattached_faces == 0:
                break
        cubes.append(c)


    part_1 = 0
    for c in cubes:
        part_1 += c.unattached_faces        
        

    print("Challenge 1: ", part_1)
    #print("Challenge 2: ", part_2)





if __name__ == "__main__":
    main()