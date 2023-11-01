
with open ("input.txt", "r") as f:
    data = f.read().splitlines()

# a through z have priorities 1 through 26
# A through Z have priorities 27 through 52

priority = 0

def get_priority(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96


for l in data:
    first_half = l[:len(l)//2]
    second_half = l[len(l)//2:]

    # intersection of the two halves
    intersection = set(first_half).intersection(set(second_half))
    letter= intersection.pop()

    letter_priority= get_priority(letter)

    priority += letter_priority


print("challenge 1: ", priority)






with open ("day03/input.txt", "r") as f:
    data = f.read().splitlines()

# divide data in groups of 3 lines
data = [data[i:i+3] for i in range(0, len(data), 3)]


priority_2 = 0

for group in data:
    intersection= set(group[0]).intersection(set(group[1])).intersection(set(group[2]))

    letter = intersection.pop()
    letter_priority = get_priority(letter)
    priority_2 += letter_priority
    
print("challenge 2: ", priority_2)
