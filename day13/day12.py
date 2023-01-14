
def store_packets(lines):
    pairs= [] # challenge 1
    all_packets= [] # challenge 2

    next_pair= None
    for line in lines:
        all_packets.append(eval(line))

        if next_pair is None:
            next_pair= eval(line)
            continue
        pairs.append((next_pair, eval(line)))
        next_pair= None


    all_packets.append([[2]])
    all_packets.append([[6]])

    return pairs, all_packets


def read_data():
    #with open("day13/test_input.txt", "r") as f:
    with open("day13/input.txt", "r") as f:

        lines= f.read().splitlines()
        lines= filter(None, lines) # remove empty lines

    pairs, all_packets= store_packets(lines)

    return pairs, all_packets

            

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



def challenge_1(pairs):
    sum_right_order= 0

    i= 1
    for pair in pairs:
        left, right= pair
        #print('\n', i)
        if compare_packets(left, right):
            #print("--RIGHT--", i)
            sum_right_order += i
        i += 1

    return sum_right_order


def quick_sort(packets):
    if len(packets) <= 1:
        return packets

    pivot= packets[0]
    left= []
    right= []
    for packet in packets[1:]:
        if compare_packets(packet, pivot):
            left.append(packet)
        else:
            right.append(packet)

    return quick_sort(left) + [pivot] + quick_sort(right)


def get_index(sorted_packets):
    idx_1= 0
    idx_2= 0

    i= 1
    for packet in sorted_packets:
        if packet == [[2]]:
            idx_1= i
        if packet == [[6]]:
            idx_2= i
        i += 1

    return idx_1, idx_2



def challenge_2(all_packets): 

    sorted_packets=  quick_sort(all_packets)

    idx_1, idx_2 = get_index(sorted_packets)

    return idx_1 * idx_2




def main():

    pairs, all_packets= read_data()

    sum_right_order= challenge_1(pairs)
    all_packets_right_order= challenge_2(all_packets)

    print("challenge 1:", sum_right_order)
    print("challenge 2:", all_packets_right_order)

        



if __name__ == "__main__":
    main()