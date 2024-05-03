import os


def getDir():
    path = input("Copy and past the directory here: ")
    path = path.replace("\\", "/")
    return path

def getFile():
    file = input("Copy and past the name of file only: ")

os.chdir(f'{getDir()}')
print(os.getcwd())
