import os
import sys

def main():
    print("@Copyright CT-18030 Hassan Farid Linux Shell")
    
    while True:
        query = input("\n" + str(os.getcwd()) + ": ")
    
        if query == 'exit':
            sys.exit()
            break
        
        query_comps = query.split(' ')
    
        #Parsing the provided query
        if len(query_comps) == 1:
            command = query_comps[0]
        
            if command == "ls":
                print(os.system('ls'))
            
            elif command == "fork":
                os.fork()
            
            elif command == "wait":
                os.wait()

        else:
            command = query_comps[0]
            args = query_comps[1:]
    
if __name__ == "__main__":
    main()
