import os
from copy import Copy
from rm import Remove
from manage import Manage
import sys


class Driver:
    def __init__(self):
        pass


def main():
    if sys.argv[1:]:
        # arguments are passed
        # check for validity of commands
        list_of_args = sys.argv[1:]
        if list_of_args[0] == 'copy':
            if len(list_of_args) == 3:
                print(f"{list_of_args[1]}")
                filelist = list_of_args[1].split('\\')[-1]
                print(f"fileList---{list_of_args[1].split('\\')}")
                path = '\\'.join(list_of_args[1].split('\\')[:len(list_of_args[1].split('\\'))-1])
                if path[-1] == '\\':
                    path += '\\'
                print("path---",path)
                copy = Copy(path, list_of_args[2])
                copy.copyfile(filelist)
            else:
                raise ValueError('Proper arguments not passed')
        elif list_of_args[0] == 'del':
            if len(list_of_args) == 2:
                filelist = list_of_args[1].split('\\')[-1]
                path = '\\'.join(list_of_args[1].split('\\')[:len(list_of_args[1].split('\\'))-1])
                if path[-1] == '\\':
                    path += '\\'
                remove = Remove(path)
                remove.removefile(filelist)
            else:
                raise ValueError('Proper arguments are not passed')
        elif list_of_args[0] == 'arrange':
            if len(list_of_args) == 2:
                Manage(list_of_args[1])
            else:
                raise ValueError('Proper arguments are not passed')


    else:
        print("A simple command line tool for copy and removing files....")
        print("These are the supported commands: ")
        print('''
        1. Command - copy 
            supports single file and group of files.
        2. Command - del
            supports single/multiple file deletion
        3. Command - arrange
            supports moving files from source path to source path by creating different folders in it.        
        ''')
        command = input('type any command >')
        match command:
            case 'copy':
                sourcepath = input('what\'s? your source folder path >')
                filename = input('what\'s your file name to be copied (comma separated values if multiple files) >')
                filelist = [file for file in filename.split(',')]
                targetpath = input('Where it shoud be copied >')
                copy = Copy(sourcepath, targetpath)
                copy.copyfile(filelist)
            case 'del':
                sourcepath = input('what\'s? your source folder path >')
                filename = input('what\'s your file names to delete (comma separated values if multiple files) >')
                filelist = [file for file in filename.split(',')]
                rm = Remove(sourcepath)
                rm.removefile(filelist)
            case 'arrange':
                sourcepath = input('what\'s? your source folder path >')
                print(f'I am arranging your folder')
                Manage( sourcepath)
            case _:
                sys.exit(f'Either {command} is invalid or it is not implemented.')


if __name__ == "__main__":
    main()
