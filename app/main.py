import os
import subprocess
import sys
from typing import Optional
def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
# def handle_exit(args):
#     sys.exit(int(args[0]) if args else 0)
# def handle_echo(args):
#     print(" ".join(args))
# def handle_type(args):
#     if args[0] in builtins:
#         print(f"{args[0]} is a shell builtin")
#     elif executable := locate_executable(args[0]):
#         print(f"{args[0]} is {executable}")
#     else:
#         print(f"{args[0]}: not found")
# builtins = {
#     "exit": handle_exit,
#     "echo": handle_echo,
#     "type": handle_type,
# }
def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    PATH = os.environ.get("PATH")

    # Wait for user input
    while(True):
        command, *args= input().split(" ")
        if(command != ""):
            if(command == "exit"):
                exit(0)

            elif(command== "echo"):
                flag = False
                for x in range(0,len(args)):
                    
                    if(x==0 and args[x][0]=="'"):
                        flag=True
                        print(args[x][1:],end=" ")
                    elif(x==len(args)-1 and args[x][-1]=="'"):
                        print(args[x][0:-1])
                    elif(x == len(args)-1):
                        print(args[x])
                    elif flag:
                        print(args[x],end=" ")
                    elif flag is False:
                        if(args[x]==" "):
                            continue
                        else:
                            print(args[x],end=" ")


            
            elif(command=="type"):
                cmd = args[0]
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if cmd in ["echo","exit","type","pwd","cd","cat"]:
                    print(cmd+" is a shell builtin")
                elif cmd_path:
                    print(cmd+" is "+cmd_path)
                else:
                    print(cmd+": not found")

            elif(executable := locate_executable(command)):
                #print(executable)
                subprocess.run([executable,*args])
            
            elif(command=="pwd"):
                print(os.getcwd())
            
            elif(command=="cd"):
                if(args[0]=='~'):
                    os.chdir(os.environ.get("HOME"))

                else:
                    try:
                        os.chdir(args[0])
                    except FileNotFoundError:
                        print(f"cd: {args[0]}: No such file or directory")

            elif(command=="cat"):
                for path in args:
                    path=path[1:-1]
                    with open(path, 'r') as file:
                        content = file.read()
                    print(content,end=" ")
                print()



               

            else:
                print(f"{command}: command not found")
            # elif(command[0].startswith("program")):
            #     print("Hello "+command[1+"!"],end = " ")
            #     execute_program(command[0])
            


           
            sys.stdout.write("$ ")

        
        else:
            print(f"{command}: command not found")
        sys.stdout.flush()
if __name__ == "__main__":
    main()