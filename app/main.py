import sys
import os
import subprocess
from typing import Optional

def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path



def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    PATH = os.environ.get("PATH")

    # Wait for user input
    while(True):
        command, *args = input().split(" ")
        if(command != ""):
            if(command== "exit"):
                exit(0)

            elif(command== "echo"):
                for x in range(1,len(args)):
                    if(x == len(args)-1):
                        print(args[x])
                    else:
                        print(command,end=" ")
            
            elif(command=="type"):
                cmd = command
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if command in ["echo","exit","type"]:
                    print(command+" is a shell builtin")
                elif cmd_path:
                    print(cmd+" is "+cmd_path)
                else:
                    print(command+": not found")

            elif(executable := locate_executable(command)):
                #print(executable)
                subprocess.run(executable, *args)
            # elif(command[0].startswith("program")):
            #     print("Hello "+command[1+"!"],end = " ")
            #     execute_program(command[0])
            


           
            sys.stdout.write("$ ")

        
        else:
            
            break


if __name__ == "__main__":
    main()
