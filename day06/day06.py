import copy

def read_data():
    with open("day06/input.txt", "r") as f:
        data= f.read()
    
    return data




def get_marker(data, type):
    if type== "message":
        amount= 14
    else:
        amount= 4
    for idx in range(len(data) - amount):
        cut = data[idx:idx+amount]
        
        if any(cut.count(c) > 1 for c in cut):
            continue
        return idx + amount



def main():
    data= read_data()

    index= get_marker(data, "default")
    index_2= get_marker(data, "message")

    print("challenge 1: ", index)
    print("challenge 2: ", index_2)





if __name__ == "__main__":
    main()