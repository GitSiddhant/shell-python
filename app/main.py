import sys
import os
import subprocess

def execute_program(program_name, args=None):
    """
    Executes a program available in the PATH and prints its output.

    :param program_name: The name of the executable to run.
    :param args: A list of arguments to pass to the executable, if any.
    """
    # Build the command
    command = [program_name]
    if args:
        command.extend(args)

    try:
        # Execute the program
        result = subprocess.run(
            command,
            capture_output=True,  # Capture stdout and stderr
            text=True,            # Return output as a string
            check=True            # Raise exception if the command fails
        )

        # Print the output
        
        print( result.stdout)

        # Print errors, if any
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {program_name}: {e}")
        print("Error Output:")
        print(e.stderr)
    except FileNotFoundError:
        print(f"Error: {program_name} not found in PATH.")



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
            elif(command[0].startswith("program")):
                print("Hello "+command[1+"!"],end = " ")
                execute_program(command[0])
            


            else:

                print(command[0]+": command not found")
            sys.stdout.write("$ ")

        
        else:
            
            break


if __name__ == "__main__":
    main()
