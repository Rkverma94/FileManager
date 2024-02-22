from cmd import FileCommandPrompt


class Remove(FileCommandPrompt):
    def __init__(self, sourcepath):
        super().__init__('del', sourcepath)
        ...

    def removefile(self, file):
        self.run(file)

    def removefiles(self, files):
        self.run(files)


def main():
    ...


if __name__ == '__main__':
    main()