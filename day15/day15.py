import numpy as np


def read_data(test= False):
    filename= "test_input.txt" if test else "input.txt"

    with open("day15/" + filename, "r") as f:
        lines= f.read().splitlines()
            
    
    sensors= {}

    for line in lines:
        sensor, beacon= line.split(":")

        sen_X, sen_Y= sensor.split(",")
        sen_X= int(sen_X.split("=")[1])
        sen_Y= int(sen_Y.split("=")[1])

        be_X, be_Y= beacon.split(",")
        be_X= int(be_X.split("=")[1])
        be_Y= int(be_Y.split("=")[1])

        sensors[(sen_X, sen_Y)]= (be_X, be_Y)

    return sensors


def print_grid(grid):
    grid_s= ""

    # replace "0" with ".", "1" with "S" and "2" with "B"
    grid= np.where(grid==0, ".", grid)
    grid= np.where(grid=="1", "S", grid)
    grid= np.where(grid=="2", "B", grid)
    grid= np.where(grid=="3", "#", grid)

    for row in grid:
        grid_s+= "".join(row)+"\n"
    print(grid_s)


def get_distance(sensor, beacon):
    return abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])


def get_neighbours(sensor, grid):
    neighbours= set()

    if sensor[0] > 0:
        neighbours.add((sensor[0]-1, sensor[1])) # left

    if sensor[0] < grid.shape[1]-1:
        neighbours.add((sensor[0]+1, sensor[1])) # right

    if sensor[1] > 0:
        neighbours.add((sensor[0], sensor[1]-1)) # up

    if sensor[1] < grid.shape[0]-1:
        neighbours.add((sensor[0], sensor[1]+1)) # down

    return neighbours



def challenge(sensors):
    grid_height_max= max([max(sensor[1], beacon[1]) for sensor, beacon in sensors.items()]) + 1
    grid_height_offset= min([min(sensor[1], beacon[1]) for sensor, beacon in sensors.items()])

    grid_width_max= max([max(sensor[0], beacon[0]) for sensor, beacon in sensors.items()]) + 1
    grid_width_offset= min([min(sensor[0], beacon[0]) for sensor, beacon in sensors.items()])
    

    grid= np.zeros((grid_height_max-grid_height_offset, grid_width_max-grid_width_offset), dtype= int)

    for sensor, beacon in sensors.items():
        print("sensor: ", sensor, "beacon: ", beacon)
        grid[sensor[1]-grid_height_offset, sensor[0]-grid_width_offset]= 1
        grid[beacon[1]-grid_height_offset, beacon[0]-grid_width_offset]= 2

        distance_sensor_beacon= get_distance(sensor, beacon)

        cells= get_neighbours(sensor, grid)

        while cells:
            square= cells.pop()
            print("square: ", square)

            if grid[square[1]-grid_height_offset, square[0]-grid_width_offset] == 0:

                if get_distance(square, sensor) <= distance_sensor_beacon:
                    grid[square[1]-grid_height_offset, square[0]-grid_width_offset]= 3

                    cells.update(get_neighbours(square, grid))






        print_grid(grid)




    
    






def main():

    sensors= read_data(test=True)
    
    positions= challenge(sensors)

    print("Challenge 1: ", positions)





if __name__ == "__main__":
    main()