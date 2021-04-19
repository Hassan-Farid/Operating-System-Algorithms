def main():
    size = int(input("Enter the size of the available memory: "))
    os_mem = int(input("Enter the memory space occupied by the OS: "))
    part_no = int(input("Enter the number of fixed partitions: "))
    page_size = list(map(int, input("Enter the memory size for pages to be allocated: ").split()))
    
    page_mem = size - os_mem
    rem_size = page_mem % part_no
    
    rem_part = []
    
    part_counter = 0
    for i in range(len(page_size)):
        part_counter += 1
        
        if part_counter > 6:
            break
        
        part_size = page_mem // part_no
        if page_size[i] <= rem_size:
            rem_size -= page_size[i]
            print("Allocated Page {}".format(i + 1))
        elif page_size[i] <= part_size:
            part_size -= page_size[i]
            rem_part.append(part_size)
            print("Allocated Page {}".format(i + 1))
        else:
            part_counter -= 1
            print("Blocked process {} due to unavailable capacity".format(i + 1))
            
    print("Internal Fragmentation for Memory is: {}".format(sum(rem_part) + rem_size))
    
if __name__ == "__main__":
    main()
