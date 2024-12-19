import os
import subprocess
import sys
from typing import Optional
import re
import shlex
def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
    return None

def main():
    # Uncomment this block to pass the first stage
    
    PATH = os.environ.get("PATH")

    # Wait for user input
    while(True):
        sys.stdout.write("$ ")
        inp = input()
        command, *args= inp.split(" ")
        if(command == "exit"):
                exit(0)
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

        elif(command=="type"):
                cmd = args[0]
                cmd_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{cmd}"):
                        cmd_path = f"{path}/{cmd}"
                if cmd in ["echo","exit","type","pwd","cd"]:
                    print(cmd+" is a shell builtin")
                elif cmd_path:
                    print(cmd+" is "+cmd_path)
                else:
                    print(cmd+": not found")

        elif(command== "echo"):
            if inp.startswith("'") and inp.endswith("'"):
                 message = inp[6:-1]
                 print(message)
            else:
                 parts = shlex.split(inp[5:])
                 print(" ".join(parts))
        else:
             args = shlex.split(inp)
             executablePath = locate_executable(args[0])
             if executablePath:
                  result = subprocess.run(args,capture_output=True,text=True)
                  print(result.stdout, end="")
             else:
                  print(f"{command}: command not found")
                    

  
  
    

        
        
if __name__ == "__main__":
    main()