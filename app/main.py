import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    while(True):
        command = input()
        if(command != ""):

            print(command+": command not found")
        
        else:
            break


if __name__ == "__main__":
    main()
