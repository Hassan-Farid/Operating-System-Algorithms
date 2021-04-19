def main():
    size = int(input("Enter the memory size available: "))
    os_mem = int(input("Enter the memory size occupied by OS: "))
    pageno = list(map(int, input("Enter the sizes for the pages to be allocated: ").split()))
    page_mem = size - os_mem
    for i in range(len(pageno)):
        if page_mem > pageno[i]:
            page_mem -= pageno[i]
            print("Allocated Page {}".format(i + 1))
        else:
            print("Blocked process {} due to unavailable capacity".format(i + 1))
    
    print("External Fragmentation for Memory is: {}".format(page_mem))
    
if __name__ == "__main__":
    main()
        
        