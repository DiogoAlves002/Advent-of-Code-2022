

def read_data():
    with open("day07/input.txt", "r") as f:
        data= f.read().splitlines()
    
    return data


def is_command(line):
    return line[0] == "$"


def fill_directory(data, directory):
    current_dir= {"/": []} # current directory
    
    l= 0
    while l < len(data):
        line= data[l]

        if is_command: # command
            if line[2:4] == "cd": # change dir
                if line[5:] == "..":
                    current_dir= {i for i in directory if directory[i]==current_dir} # return to parent's directory
                else:
                    current_dir= line[5:]
                    directory[current_dir]= []
            elif line[2:4] == "ls": # list dir
                while l+1< len(data) and not is_command(data[l+1]):
                    if data[l+1][0] == "d": # dir
                        new_dir= {data[l+1][4:]: []}
                        directory[current_dir].append(new_dir)
                    else: # file
                        size_file= data[l+1].split(" ")
                        size= int(size_file[0])
                        directory[current_dir].append(size)
                    l+= 1


        l+= 1
    return directory


def fix_empty_dir(directory, new_directory, current_dir):
    
    total= 0
    for dir in directory[current_dir]:
        if type(dir) == int:
            total += dir
        else:
            for d in dir.keys():
                new_directory, to_add_to_total = fix_empty_dir(directory, new_directory, d)
                total += to_add_to_total
    new_directory[current_dir]= total
    return new_directory, total



def sum_total(directory):
    total= 0

    for value in directory.values():
        if value <= 100000:
            total += value
    
    return total


def main():
    data= read_data()

    directory= {"/": {}}
    
    directory= fill_directory(data, directory)

    new_directory= {}
    final_directory, total= fix_empty_dir(directory, new_directory, '/')
    #print(final_directory)

    total_sum= sum_total(final_directory)

    print("challenge 1: ", total_sum)
    #print("challenge 2: ", index_2)





if __name__ == "__main__":
    main()