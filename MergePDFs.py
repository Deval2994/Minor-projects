from PyPDF2 import PdfMerger
import os


def getDir(promt):
    path = input(promt)
    path = path.replace("\\", "/")  # Replace backslashes with forward slashes for consistency
    os.path.exists(path)
    return path



def getFiles():
    numberOfFiles = int(input("List total number of files to merge: "))
    i = 1
    while i <= numberOfFiles:
        file = input(f"Copy and paste path of file {i} (Do not include ' \" '): ")
        file.replace("\\", "/")  # Replace backslashes with forward slashes for consistency
        try:
            merger.append(file)
            i += 1
        except (FileNotFoundError, PermissionError, Exception) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    merger = PdfMerger()  # Initialize a PdfMerger object
    getFiles()  # Get the list of PDF files to merge from user input
    newPDF = input("Give a name to merged PDF: ")  # Prompt user to give a name to the merged PDF file
    while True:
        try:
            directory = getDir(
                "Copy and paste the directory where you want to store merged PDF (Do not include ' \" '): ")  # Get the directory path from user input
            newPDF = os.path.join(directory, newPDF)
            merger.write(newPDF)
            merger.close()
        except Exception:
            print("directory not found")