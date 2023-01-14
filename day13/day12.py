
def read_data():
    with open("day13/input.txt", "r") as f:
        lines= f.read().splitlines()

    pairs= []
    next_pair= None
    for line in lines:
        if line:
            if not next_pair:
                next_pair= eval(line)
                continue

            pairs.append((next_pair, eval(line)))
            next_pair= None

    return pairs
            
    


def compare_packets(left, right):
    if type(left) == int and type(right) == int:
            return left < right
    elif type(left) == list and type(right) == list:
        for l, r in zip(left, right):
            if compare_packets(l, r) == False:
                return False
        return True
    elif type(left) == int:
        return compare_packets([left], right)
    else:
        return compare_packets(left, [right])






def main():


    pairs= read_data()

    total_right_order= 0

    i= 1
    for pair in pairs:
        left, right= pair
        if compare_packets(left, right):
            total_right_order += i
        i += 1


    print("challenge 1:", total_right_order)

        





if __name__ == "__main__":
    main()