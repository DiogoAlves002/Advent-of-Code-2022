import copy

def read_data():
    with open("day06/input.txt", "r") as f:
        data= f.read()
    
    return data


def get_marker(data):
    for idx in range(len(data) - 4):
        cut = data[idx:idx+4]
        
        
        if any(cut.count(c) > 1 for c in cut):
            continue
        return idx + 4





def main():
    data= read_data()

    index= get_marker(data)

    print("challenge 1: ", index)
    #print("challenge 2: ", top_2)





if __name__ == "__main__":
    main()