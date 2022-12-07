

def read_data():
    with open("day07/input.txt", "r") as f:
        data= f.read().splitlines()
    
    return data


def is_command(line):
    return line[0] == "$"


def fill_directory(data, directory):
    current_dir= {"/": {}} # current directory
    
    l= 0
    while l < len(data):
        line= data[l]

        if is_command: # command
            if line[2:4] == "cd": # change dir
                current_dir= line[5:]
                directory[current_dir]= {}
            elif line[2:4] == "ls": # list dir
                while not is_command(data[l+1]):
                    if data[l+1][0] == "d":
                        directory[current_dir][data[l+1]]= {}
                    else:
                        directory[current_dir]= {data[l+1]}
                    l+= 1
                
        else: # ls results
            pass


        l+= 1



def main():
    data= read_data()

    directory= {"/": {}}
    
    directory= fill_directory(data, directory)

    #index= get_marker(data, "default")
    #index_2= get_marker(data, "message")

    #print("challenge 1: ", index)
    #print("challenge 2: ", index_2)





if __name__ == "__main__":
    main()