import os


class FileCommandPrompt:
    folders = ['Docs', 'Videos', 'Music', 'Others', 'Applications']
    def __init__(self, command, sourcepath, targetpath=None):
        self.command = command
        self.sourcepath = sourcepath
        if targetpath:
            self.targetpath = targetpath

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        if not value:
            raise ValueError('Invalid Command')
        self._command = value

    @property
    def sourcepath(self):
        return self._sourcepath

    @sourcepath.setter
    def sourcepath(self, path):
        if not os.path.exists(path):
            raise ValueError('Path does not exists')
        self._sourcepath = path

    @property
    def targetpath(self):
        if self._targetpath:
            return self._targetpath

    @targetpath.setter
    def targetpath(self, path):
        if not os.path.exists(path):
            raise ValueError('Path does not exists')
        self._targetpath = path

    def run(self, files):
        invalid_files = []
        if isinstance(files, str):
            if not self.checkfile(files):
                raise ValueError('File does not exists')
            else:
                command = self.command+' '+'\"'+self.sourcepath+files+'\"'
                if self.targetpath:
                    command += ' '+'\"'+self.targetpath+'\"'
                os.system(command)
        #need to implement targetpath condition
        elif isinstance(files, list):
            for file in files:
                if not self.checkfile(file):
                    invalid_files.append(file)
                else:
                    command = self.command+' '+'\"'+self.sourcepath+file+'\"'
                    if self.targetpath:
                        command += ' '+'\"'+self.targetpath+'\"'
                    os.system(command)
            if invalid_files.length > 0:
                raise ValueError('Few file does not exists')

    def checkfile(self, file):
        filepath = self.sourcepath+file
        print(f'filepath---{filepath}')
        if not os.path.exists(filepath):
            return False
        else:
            return True

def main():
    try:
        filecmd = FileCommandPrompt('C:\\')
        print(filecmd.sourcepath)
    except ValueError:
        print("Path is incorrect")


if __name__ == '__main__':
    main()
