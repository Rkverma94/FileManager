import os.path

from cmd import FileCommandPrompt


class Manage(FileCommandPrompt):
    def __init__(self, command, sourcepath):
        super().__init__(command, sourcepath)
        self.initialise_folders()
        self.arrange_files()

        ...

    def initialise_folders(self):
        directories_in_path = [filename for filename in os.listdir(self.sourcepath) if os.path.isdir(os.path.join(self.sourcepath, filename))]
        for folder in self.folders:
            if folder not in directories_in_path:
                os.system('mkdir '+self.sourcepath+'\\'+folder)


    def arrange_files(self):
        docs = []
        imgs = []
        apps = []
        others = []
        # get list of files only from sourcepath
        list_files = [filename for filename in os.listdir(self.sourcepath) if
                      not os.path.isdir(os.path.join(self.sourcepath, filename))]
        # iterate on each file and put them in each containers
        for file in list_files:
            print(file)
            try:
                if file.split('.')[1] in ['doc', 'word', 'pdf', 'txt', 'xls', 'xlsx', 'csv', 'docx']:
                    docs.append(file)
                if file.split('.')[1] in ['jpg', 'JPG', 'JPEG', 'jpeg', 'png', 'PNG', 'bmp', 'gif']:
                    imgs.append(file)
                if file.split('.')[1] in ['exe', 'iso', 'bat', 'bin', 'dll', 'jar', 'msi', 'rar']:
                    apps.append(file)
            except IndexError:
                others.append(file)

            ...
        self.arrange_docs(docs)
        self.arrange_imgs(imgs)
        self.arrange_apps(apps)

    def arrange_imgs(self, imgs):
        self.command = 'move'
        self.targetpath = self.sourcepath + '\\Videos'
        for img in imgs:
            self.run(img)

    def arrange_apps(self, apps):
        self.command = 'move'
        self.targetpath = self.sourcepath + '\\Applications'
        for app in apps:
            self.run(app)

    def arrange_docs(self, docs):
        self.command = 'move'
        self.targetpath = self.sourcepath + '\\Docs'
        for doc in docs:
            self.run(doc)
        #
        ...

def main():
    manage = Manage('arrange', 'C:\\Users\\Shree\\Downloads\\')
    pass

if __name__ == '__main__':
    main()