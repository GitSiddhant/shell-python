import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    while(True):
        command = input().split()
        if(command[0] != ""):
            if(command[0] == exit):
                exit(0)

            else:

                print(command[0]+": command not found")
                sys.stdout.write("$ ")

        
        else:
            
            break


if __name__ == "__main__":
    main()
