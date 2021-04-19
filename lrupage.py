def main():
    frames = int(input("Enter the number of frames: "))
    ref_string = list(map(int, input("Enter the reference string for the frames: ").split()))
    
    initial = [-1] * frames
    page_faults = 0
    
    for page in ref_string:
        if page not in initial:
            if len(initial) == frames:
                initial.remove(initial[0])
                initial.append(page)
            else:
                initial.append(page)
            
            page_faults += 1
            
        else:
            initial.remove(page)
            initial.append(page)
            
        print("Reference for new Page {}: {}".format(page, initial))
            
    print("Number of Page Faults: {}".format(page_faults))
            
if __name__ == "__main__":
    main()