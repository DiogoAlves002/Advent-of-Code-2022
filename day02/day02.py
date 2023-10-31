
with open ("input.txt", "r") as f:
    data = f.read().splitlines()


# part 1
player = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

opponent = {
    "A" : 3,
    "B" : 2,
    "C" : 1,
}

points = 0

# part 2
opponent_2 = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
}
points_2 = 0

for l in data:
    
    op, pl = l.split(" ")

    points += ( player[pl] * 3 + opponent[op] * 3)%9 + player[pl]

    points_2 += (player[pl] - 1 ) * 3 + (player[pl] + opponent_2[op]) % 3 + 1 ; 

print("challenge 1: ", points)
print("challenge 2: ", points_2)


