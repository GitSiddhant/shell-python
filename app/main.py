import sys
import os





def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    PATH = os.environ.get("PATH")

    # Wait for user input
    while(True):
        command = input().split()
        if(command[0] != ""):
            if(command[0] == "exit"):
                exit(0)

            elif(command[0]== "echo"):
                for x in range(1,len(command)):
                    if(x == len(command)-1):
                        print(command[x])
                    else:
                        print(command[x],end=" ")
            
            elif(command[0]=="type"):
                cmd = command[1]
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if command[1] in ["echo","exit","type"]:
                    print(command[1]+" is a shell builtin")
                elif cmd_path:
                    print(cmd+" is "+cmd_path)
                else:
                    print(command[1]+": not found")

            else:

                print(command[0]+": command not found")
            sys.stdout.write("$ ")

        
        else:
            
            break


if __name__ == "__main__":
    main()
