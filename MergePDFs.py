from PyPDF2 import PdfMerger
import os


def getDir(promt):
    path = input(promt)
    path = path.replace("\\", "/")  # Replace backslashes with forward slashes for consistency
    return path


def getFiles():
    numberOfFiles = int(input("List total number of files to merge: "))
    for i in range(1, numberOfFiles + 1):
        file = input(f"Copy and paste path of file {i} (Do not include ' \" '): ")
        file.replace("\\", "/") # Replace backslashes with forward slashes for consistency
        pdfs.append(file)


if __name__ == "__main__":
    directory = getDir(
        "Copy and paste the directory where you want to store merged PDF (Do not include ' \" '): ")  # Get the directory path from user input
    pdfs = []  # Initialize an empty list to store PDF files
    merger = PdfMerger()  # Initialize a PdfMerger object
    getFiles()  # Get the list of PDF files to merge from user input
    newPDF = input("Give a name to merged PDF: ")  # Prompt user to give a name to the merged PDF file
    for pdf in pdfs:
        merger.append(pdf)
    newPDF = os.path.join(directory, newPDF)
    merger.write(newPDF)
    merger.close()
