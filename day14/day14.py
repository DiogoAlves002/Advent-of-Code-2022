
def store_rocks(lines):
    rocks= []
    for line in lines:
        points= line.split(" -> ")
        t= tuple()
        for point in points:
            point= float(point.replace(',', '.'))
            t= t + (point,)
        rocks.append(t)
    print(rocks)
    return rocks


def read_data():
    with open("day14/test_input.txt", "r") as f:
    #with open("day14/input.txt", "r") as f:

        lines= f.read().splitlines()

    rocks= store_rocks(lines)

    return rocks

            


def challenge_1(pairs):
    pass


def challenge_2(all_packets): 
    pass




def main():

    rocks= read_data()



        



if __name__ == "__main__":
    main()