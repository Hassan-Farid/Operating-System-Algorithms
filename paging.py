def main():
    phy_mem = int(input("Enter the size of the physical memory: "))
    log_mem = int(input("Enter the size of the logical memory: "))
    
    part_size = int(input("Enter the partition size: "))
    
    frames = phy_mem // part_size
    pages = log_mem // part_size
    
    page_frames = dict()
    for i in range(pages):
        page_frame = int(input("Enter the frame number to store page " + str(i) + ": "))
        page_frames.update({i:page_frame})
        
    print("Page Table")
    print("Page No \t Frame No")
    for pg,fr in page_frames.items():
        print("{}\t\t{}".format(pg, fr))
        
    print("Frame Table")
    print("Frame Address \t Page No")
    pg_counter = 0
    for i in range(frames):
            if i in list(page_frames.values()):
                print("{}\t\t{}".format(i, list(page_frames)[pg_counter]))
                pg_counter += 1
            else:
                print("{}\t\t{}".format(i, 3456)) #Assuming default page number for unallocated pages is 3456

    print("Computing Physical Address")
    base_addr = int(input("Enter the base address of the memory: "))
    log_addr = int(input("Enter the logical address whose physical address is required: "))
    phy_addr = base_addr + (page_frames[log_addr//part_size] * part_size) + (log_addr % part_size)
    print("Physical Address of the Instruction is: {}".format(phy_addr))
    
if __name__ == "__main__":
    main()