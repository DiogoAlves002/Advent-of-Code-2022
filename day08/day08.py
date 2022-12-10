

def read_data():
    with open("day08/input.txt", "r") as f:
        data= f.read().splitlines()
    
    return data


def countEdges(data):
    height= len(data)
    width= len(data[0])

    edges= 2*height + 2*width - 4
    return edges


def isVisible(data, tree_i, tree_j, tree):
    # up
    visibleUp= True
    visibleDown= True
    visibleLeft= True
    visibleRight= True

    for i in range(0, tree_i):
        if data[i][tree_j] >= tree: 
            visibleUp= False
            break
    
    # down
    for i in range(tree_i+1, len(data)):
        if data[i][tree_j] >= tree: 
            visibleDown= False
            break

    # left
    for j in range(0, tree_j):
        if data[tree_i][j] >= tree: 
            visibleLeft= False
            break
            
    # right
    for j in range(tree_j+1, len(data[0])):
        if data[tree_i][j] >= tree: 
            visibleRight= False
            break

    visible= visibleUp or visibleDown or visibleLeft or visibleRight
    return visible


def countMiddle(data):
    height= len(data)
    width= len(data[0])

    middle= 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            tree= data[i][j]
            if isVisible(data, i, j, tree):
                middle+= 1
    return middle


def main():
    data= read_data()
    
    edges= countEdges(data)

    total= edges + countMiddle(data)


    print("challenge 1: ", total)
    #print("challenge 2: ", index_2)





if __name__ == "__main__":
    main()