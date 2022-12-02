
with open ("day02/input.txt", "r") as f:
    data = f.read().splitlines()

# A for Rock, B for Paper, and C for Scissors (opponent)
# X for Rock, Y for Paper, and Z for Scissors (player)


points= 0

for l in data:
    if l[2] == "X": # Rock
        points += 1
        if l[0] == "A":
            points += 3
        elif l[0] == "C":
            points += 6
    
    elif l[2] == "Y": # Paper
        points += 2
        if l[0] == "B":
            points += 3
        elif l[0] == "A":
            points += 6
    
    elif l[2] == "Z": # Scissors
        points += 3
        if l[0] == "C":
            points += 3
        elif l[0] == "B":
            points += 6

print("challenge 1: ", points)





# A for Rock, B for Paper, and C for Scissors (opponent)
# X for lose, Y for draw, and Z for win (player)

points2= 0

for l in data:
    if l[2] == "X": # lose
        if l[0] == "A": # Rock
            points2 += 3
        elif l[0] == "B": # Paper
            points2 += 1
        elif l[0] == "C": # Scissors
            points2 += 2

    elif l[2] == "Y": # draw
        points2 += 3
        if l[0] == "A": # Rock
            points2 += 1
        elif l[0] == "B": # Paper
            points2 += 2
        elif l[0] == "C": # Scissors
            points2 += 3

    elif l[2] == "Z": # win
        points2 += 6
        if l[0] == "A": # Rock
            points2 += 2
        elif l[0] == "B": # Paper
            points2 += 3
        elif l[0] == "C": # Scissors
            points2 += 1


print("challenge 2: ", points2)




