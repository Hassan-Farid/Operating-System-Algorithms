def main():
    frames = int(input("Enter the number of frames: "))

    ref_string = list(map(int,input("Enter the reference string for the frames: ").strip().split()))
    initial = [-1] * frames
    page_faults = 0

    occurance = [None for i in range(frames)]
    for i in range(len(ref_string)):
        if ref_string[i] not in initial:
            if len(initial) < frames:
                initial.append(ref_string[i])
            else:
                for x in range(len(initial)):
                    if initial[x] not in ref_string[i+1:]:
                        initial[x] = ref_string[i]
                        break
                    else:
                        occurance[x] = ref_string[i+1:].index(initial[x])
                else:
                    initial[occurance.index(max(occurance))] = ref_string[i]
            page_faults += 1
            
        print("Reference string for New Page {}: {}".format(ref_string[i], initial))
        
    print("Total Page Faults: {}".format(page_faults))
    
if __name__ == "__main__":
    main()