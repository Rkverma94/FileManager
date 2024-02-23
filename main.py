import os
from copy import Copy
from rm import Remove
import sys


class Driver:
    def __init__(self):
        pass


def main():
    if sys.argv[1:]:

        pass
    else:
        print("A simple command line tool for copy and removing files....")
        print("These are the supported commands: ")
        print('''
        1. Command - copy 
            supports single file and group of files.
        2. Command - del
            supports single/multiple file deletion
            
        ''')
    ...


if __name__ == "__main__":
    main()
