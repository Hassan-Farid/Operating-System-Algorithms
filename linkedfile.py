def main():
    nums = int(input("Enter the number of files: "))
    file_dict = dict()
    
    for i in range(nums):
        name = input("Enter the file name: ")
        block_list = list(map(int, input("Enter the blocks for the file in a linked order: ").split())) #-1 to terminate sequence
        file_dict.update({name: [len(block_list), block_list]})
        
    print("Choose a file whose information is required")
    name = input("Enter the name of the file: ")
    try:
        print("Length of the File: {}".format(len(block_list)))
        print("Starting block of the File: {}".format(block_list[0]))
        print("Blocks occupied by the file in Linked format: ", end='')
        print("{} ".format(block_list[0]), end='')
        for i in block_list[1:]:
            if i == -1:
                break
            print("--> {} ".format(i), end='')
    except KeyError as err:
        print("{} is an Invalid file name".format(err))
        
if __name__ == "__main__":
    main()
        