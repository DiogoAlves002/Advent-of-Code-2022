import numpy as np


def read_data(test_input= False):
    filename= "test_input.txt" if test_input else "input.txt"

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


def print_grid(grid, with_impossible_sensor_spaces= False):
    grid_s= ""

    # replace "0" with ".", "1" with "S" and "2" with "B"
    grid= np.where(grid==0, ".", grid)
    grid= np.where(grid=="1", "S", grid)
    grid= np.where(grid=="2", "B", grid)
    if with_impossible_sensor_spaces:
        grid= np.where(grid=="3", "#", grid)
    else:
        grid= np.where(grid=="3", ".", grid)

    for row in grid:
        grid_s+= "".join(row)+"\n"
    print(grid_s)


def get_distance(sensor, beacon):
    return abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])


def get_neighbours(sensor, grid, w_offset, h_offset):

    # sensor= (w, h) # (with offset)
    # grid= (h, w) # because fuck you numpy (without offset)

    neighbours= set()
    if sensor[0] > 0+ w_offset:
        neighbours.add((sensor[0]-1, sensor[1])) # left

    if sensor[0] < grid.shape[1]-1+ w_offset:
        neighbours.add((sensor[0]+1, sensor[1])) # right

    if sensor[1] > 0+ h_offset:
        neighbours.add((sensor[0], sensor[1]-1)) # up

    if sensor[1] < grid.shape[0]-1+ h_offset:
        neighbours.add((sensor[0], sensor[1]+1)) # down

    return neighbours

def add_sensors(grid, sensors, grid_width_offset, grid_height_offset):
    visited= set()
    for sensor, beacon in sensors.items():
        visited.clear()
        #print("sensor: ", sensor, "beacon: ", beacon)
        grid[sensor[1]-grid_height_offset, sensor[0]-grid_width_offset]= 1
        grid[beacon[1]-grid_height_offset, beacon[0]-grid_width_offset]= 2

        distance_sensor_beacon= get_distance(sensor, beacon)

        cells= get_neighbours(sensor, grid, grid_width_offset, grid_height_offset)

        while cells:
            square= cells.pop()
            #print("square: ", square)

            if square in visited:
                continue
            visited.add(square)

            if get_distance(square, sensor) > distance_sensor_beacon:
                continue
            cells.update(get_neighbours(square, grid, grid_width_offset, grid_height_offset))

            if grid[square[1]-grid_height_offset, square[0]-grid_width_offset] == 0:
                grid[square[1]-grid_height_offset, square[0]-grid_width_offset]= 3

    return grid


def count_impossible_sensor_spaces(grid, row, height_offset):
    row+= height_offset
    
    count= 0
    for square in grid[row]:
        if square == 3:
            count+= 1

    return count

    




def challenge_test(sensors):
    """ This version calculates the full grid, unfortunately the one given in the input is too big for this."""

    grid_height_max= max([max(sensor[1], beacon[1]) for sensor, beacon in sensors.items()]) + 1
    grid_height_offset= min([min(sensor[1], beacon[1]) for sensor, beacon in sensors.items()])

    grid_width_max= max([max(sensor[0], beacon[0]) for sensor, beacon in sensors.items()]) + 1
    grid_width_offset= min([min(sensor[0], beacon[0]) for sensor, beacon in sensors.items()])

    
    grid= np.zeros((grid_height_max-grid_height_offset, grid_width_max-grid_width_offset), dtype= int)

    grid= add_sensors(grid, sensors, grid_width_offset, grid_height_offset)


    print_grid(grid)
    print_grid(grid, with_impossible_sensor_spaces= True)

    row= 10
    num= count_impossible_sensor_spaces(grid, row, grid_height_offset)
    return num


def is_row_in_range(sensor, beacon, row):
    distance= get_distance(sensor, beacon)

    if row > sensor[1]: # row is below sensor
        return row <= sensor[1] + distance, distance

    else: # row is above or in sensors line
        return row >= sensor[1] - distance, distance



def challenge(sensors, row= 2000000):
    """ This version calculates the ranges of the sensors and only considers the ones that contain the desired row (cant print the grid :c)"""
    
    blocked_squares= set()
    for sensor, beacon in sensors.items():
        in_range, distance= is_row_in_range(sensor, beacon, row)
        if in_range:
            Vertical_distance_to_row= abs(sensor[1]-row)
            horizontal_remaining= distance - Vertical_distance_to_row # the remaining distance that can be covered horizontally both to the left and right
            
            blocked_squares.update([(sensor[0]+i, row) for i in range(-horizontal_remaining, horizontal_remaining+1)])


            blocked_squares.remove(sensor) if sensor in blocked_squares else None
            blocked_squares.remove(beacon) if beacon in blocked_squares else None
           
            

    
     
    return len(blocked_squares)






def main():

    test_input= False

    num= 0
    if test_input:
        sensors= read_data(test_input)
        num= challenge_test(sensors)
    else:
        sensors= read_data()
        num= challenge(sensors)

    print("Challenge 1: ", num)





if __name__ == "__main__":
    main()