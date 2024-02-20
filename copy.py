from cmd import FileCommandPrompt


class Copy(FileCommandPrompt):
    def __init__(self, sourcepath, targetpath):
        super().__init__('copy', sourcepath, targetpath)

    def copyfile(self, file):
        self.run(file)
        ...

    def copyfiles(self, files):
        for file in files:
            self.run(files)
        ...


def main():
    copy = Copy('C:\\Users\\Shree\\Documents\\', 'C:\\Users\\Shree\\Documents\\Pdfs')
    copy.copyfile('test.css')


if __name__ == '__main__':
    main()


