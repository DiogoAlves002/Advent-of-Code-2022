with open('input.txt') as f:
    data = f.read().splitlines()


count = 0
count2= 0


for l in data:
    first, second = l.split(',')


    begin_f, last_f= first.split('-')

    begin_s, last_s = second.split('-')

    begin_f = int(begin_f)
    last_f = int(last_f)

    begin_s = int(begin_s)
    last_s = int(last_s)


    if (begin_f <= begin_s and last_f >= last_s) or (begin_f >= begin_s and last_f <= last_s): # challenge 1
        count += 1

    # check if one of them starts or ends in the middle of the other
    if  (begin_f <= begin_s <= last_f or begin_f <= last_s <= last_f) or (begin_s <= begin_f <= last_s or begin_s <= last_f <= last_s): # challenge 2
        count2 += 1


print("challenge 1: ", count)

print("challenge 2: ", count2)



