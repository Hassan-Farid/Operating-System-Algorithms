def main():
    processes = int(input("Enter the number of processes : "))
    resources = int(input("Enter the number of resources : "))
    max_resources = [int(i) for i in input("Enter the maximum instances for each resource : ").split()]

    print("\n-- Allocated Resources for each process --")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    print("\n-- Maximum Resources that can be allocated for each process --")
    max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

    allocated = [0] * resources
    for i in range(processes):
        for j in range(resources):
            allocated[j] += currently_allocated[i][j]
    print(f"\nTotal Allocated Resources : {allocated}")

    available = [max_resources[i] - allocated[i] for i in range(resources)]
    print(f"Total Available Resources : {available}\n")

    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i + 1} is executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("The given processes are in an unsafe state.")
            break

        print(f"The given processes are in a safe state.\navailable resources : {available}\n")


if __name__ == '__main__':
    main()
