from scrobble import scrobble
from colorama import init, Fore
import os
import sys
init(autoreset = True)  

def main():
    scrobble()
    user_input = input(Fore.GREEN + "Restart (y/n): ")
    if user_input == 'y' or user_input == 'yes':
        os.system('cls')
        main()
    else:
        sys.exit()
        
if __name__ == '__main__':
    main()