
def main():
    nums = int(input("Enter the number of files: "))
    file_dict = dict()
    index_dict = dict()
    
    for i in range(nums):
        name = input("Enter the name of the file: ")
        block_list = list(map(int, input("Enter the blocks for the file: ").split()))
        index_block = int(input("Enter the index block from the given blocks: ")) #Should be unique for each file
        index_dict.update({str(index_block):block_list})
        file_dict.update({name: [len(block_list), index_block]})
    
    print("Choose a file whose information is required")
    name = input("Enter the name of the file: ")
    try:
        print("Length of File: {}".format(file_dict[name][0]))
        print("Index block of File: {}".format(file_dict[name][1]))
        print("Blocks occupied by File: {}".format(index_dict[str(file_dict[name][1])]))
    except KeyError as err:
        print("{} is not a valid Index block".format(err))
        
if __name__ == "__main__":
    main()
        
        