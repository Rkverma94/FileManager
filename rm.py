from cmd import FileCommandPrompt


class Remove(FileCommandPrompt):
    def __init__(self, sourcepath):
        super().__init__('del', sourcepath)
        ...

    def removefile(self, file):
        self.run(file)


def main():
    remove = Remove('C:\\Users\\Shree\\Documents\\Pdfs\\')
    remove.removefile('testtodel.txt')

if __name__ == '__main__':
    main()