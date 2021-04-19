def main():
    frames = int(input("Enter the number of frames: "))
    ref_string = list(map(int, input("Enter the reference string for the frames: ").split()))
    
    initial = [-1] * frames
    page_faults = 0
    for i in range(len(ref_string)):
        if ref_string[i] not in initial:
            page_faults += 1
        
        initial[i % frames] = ref_string[i]
        print("Reference for New Page {}: {}".format(ref_string[i], initial))
        
    print("Total number of page faults: {}".format(page_faults))
    
if __name__ == "__main__":
    main()
        
        