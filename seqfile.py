def get_blocks(start, length):
    block_list = []
    for i in range(start, length + start):
        block_list.append(i)
        
    return block_list

def main():
    num = int(input("Enter the number of files: "))
    file_dict = dict()
    for i in range(num):
        name = input("Enter the name of the file: ")
        start = int(input("Enter the starting block of the file: "))
        length = int(input("Enter the number of blocks in the file: "))
        file_dict.update({name:[length, get_blocks(start, length)]})
    
    print("Choose the file whose info you want to look at")
    name = input("Enter the name of the file: \n")
    try:
        print("Length of File: {}".format(file_dict[name][0]))
        print("Blocks occupied by File: {}".format(file_dict[name][1]))
    except KeyError as err:
        print("{} not a valid filename".format(err))
    
if __name__ == "__main__":
    main()        