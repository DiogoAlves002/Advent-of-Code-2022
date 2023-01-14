
def read_data():
    with open("day13/input.txt", "r") as f:

        lines= f.read().splitlines()

    pairs= []
    next_pair= None
    for line in lines:
        if line:
            if next_pair is None:
                next_pair= eval(line)
                continue
            pairs.append((next_pair, eval(line)))
            next_pair= None

    return pairs
            

def compare_int(left, right):
    if left == right:
        #print("equal int", left, right)
        return -1
    #print("not equal int", left, right)
    if left < right:
        return 1
    return 0


def compare_packets(left, right):
    if type(left) == int and type(right) == int:
        return compare_int(left, right)
        
    left= [left] if type(left) == int else left
    right= [right] if type(right) == int else right

    #print("##compare", left, right)
    for l, r in zip(left, right):
        result= compare_packets(l, r)
        if result == 1:
            #print("smaller", left, right)
            return 1
        elif result == 0:
            #print("greater", left, right)
            return 0
    return compare_int(len(left), len(right))





def main():


    pairs= read_data()

    sum_right_order= 0

    i= 1
    for pair in pairs:
        left, right= pair
        #print('\n', i)
        if compare_packets(left, right):
            #print("--RIGHT--", i)
            sum_right_order += i
        i += 1


    print("challenge 1:", sum_right_order)

        





if __name__ == "__main__":
    main()