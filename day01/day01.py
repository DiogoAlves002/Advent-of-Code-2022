
with open ("input.txt", "r") as f:
    data = f.read().splitlines()

elfs= {}
elf= 0
cal= 0
for line in data:
    if line == "":
        elfs[elf] = cal
        elf += 1
        cal = 0
        continue
    cal += int(line)

# print the biggest value
print("challenge 1: ", max(elfs.values()))




# print the sum of the top three values
print("challenge 2: ", sum(sorted(elfs.values(), reverse=True)[:3]))



