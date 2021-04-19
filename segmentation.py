def main():
    table_size = int(input("Enter the number of segments in segment table: "))
    seg_table = []
    for i in range(table_size):
        print("For Segment {}".format(i + 1))
        base_addr = int(input("Enter base address for the segment: "))
        seg_len = int(input("Enter the length of the segment: "))
        seg_size = int(input("Enter the size of each process in the segment: "))
        phy_seg = int(input("Enter the physical address of first process in the segment: "))
        seg_dict = {}
        seg_no = base_addr
        for j in range(base_addr, seg_len + base_addr):
            seg_dict.update({seg_no: phy_seg + (seg_no - base_addr)*seg_size})
            seg_no += 1
        print(seg_dict)
        seg_table.append(seg_dict)
        
    print(seg_table)
    
    print("\nSegment Table")
    print("Seg No\tBase Address\tSegment Limit")
    for i in range(table_size):
        print("{}\t\t{}\t\t{}".format(i+1, list(seg_table[i])[0], len(list(seg_table[i]))))
        
    log_addr = int(input("Enter the logical address for the segment: "))
    phy_addr = -1
    for i in range(len(seg_table)):
        if log_addr in list(seg_table[i]):
            phy_addr = seg_table[i][log_addr]
            
    if phy_addr != -1:
        print("Physical Address of the required Segment Address: {}".format(phy_addr))
    else:
        print("Invalid Physical Address")
        
if __name__ == "__main__":
    main()
    

            