import os


def main():
    os.chdir('C:\\Users\\Shree\\Downloads\\')
    files = os.listdir()
    pdfs = []
    for file in files:
        if ".pdf" in file:
            pdfs.append(file)
    print(pdfs)
    for pdf in pdfs:
        sourcepath = '"C:\\Users\\Shree\\Downloads\\'+pdf+'"'
        targetpath = '"C:\\Users\\Shree\\Documents\\Pdfs"'
        copycmd = 'copy '+sourcepath+' '+targetpath
        os.system(copycmd)

    pass


if __name__ == "__main__":
    main()
