import PyPDF2
import sys
import time

#just for decoration in loading time---------------------------------
def loading_decor():
    for i in range(10):
        print("-",end="")
        time.sleep(0.02)
    print(":")
    for i in range(10):
        print("\\\b",end="")
        time.sleep(0.2)
        print("|\b",end="")
        time.sleep(0.2)
        print("-\b",end="")
        time.sleep(0.2)
        print("/\b",end="")


# to merge only a selected part of pdf -------------------------------------------
def from_pages():
    start = input("---------------start or means from which you to pick the pages\n")
    stop = input("---------------stop or means at which page to stop")
    page_Set = (start, stop)
    return page_Set

# it's a append function for pdf which append one pdf into another-------with some options like specific pages.-----------
def append_merger_fun(fileobj1, fileobj2):
    merger.append(fileobj1, None, None, True)
    specific_page = input("---------------want to add only specific number of pages(Y/N) = ")
    if specific_page == "Y":
        page_SeT = from_pages()
    elif specific_page == "N":
        no_of_pages = fileobj2.getNumPages()
        page_SeT = (0, no_of_pages)
    merger.append(fileobj2, None, page_SeT, True)
    merger.write(rf"----------------path to save the file needs to be here----------------")
    loading_decor()
    return "done"

# a function that merger a given pdf into another pdf --------------with some options like-
# where to put second pdf, selective pdf's page insertions---------------------------------
def merge_pdf_position(fileobj1, fileobj2, page_no):
    specific_page = input("---------------want to add only specific number of pages(Y/N) = ")
    merger.merge(0, fileobj1, None, None, True)
    if specific_page == "Y":
        page_SeT = from_pages()
    elif specific_page == "N":
        no_of_pages = fileobj2.getNumPages()
        page_SeT = (0, no_of_pages)
    merger.merge(page_no, fileobj2, None, page_SeT, True)
    merger.write(rf"----------------path to save the file needs to be here----------------")
    loading_decor()
    return "done"

# this function only asks for more inputs and to continue the work------------------------------
def ask_for_more():
    answer = int(input("---------------do you want to continue (Y/N) = "))
    if answer == "Y":
        flag = 1
    elif answer == "N":
        flag = 0
    return flag

# it's a main merger function for basic pdf merging, this function runs all related merging or appending functions--------
# or we can say it runs andlink all pdf addition functions.
def main(fileobj1, fileobj2):
    while True:
        print("$---------------what you want to do with these files-----------------$")
        try:
            option = int(
                input("---------------following are the options:-\nmerge = 1\nappend = 2\n"))
        except ValueError:
            print("enter only integer value\nnow please try again !!!!!!!")
        # more exceptions handling required for various errors.
        if option == 1:
            extra_select = input("---------------want to merge second pdf at specific page(Y/N) = ")
            if extra_select == "Y":
                page_no = int(input("---------------at what you want to insert "))
            else:
                page_no = 0
            merge_pdf_position(fileobj1, fileobj2, page_no)
        elif option == 2:
            append_merger_fun(fileobj1, fileobj2)
        close = ask_for_more()
        if close == 0:
            break


# initialization of merger object which come into play for merging pdfs-----------------------
merger = PyPDF2.PdfFileMerger()

# this will take arguments from command line ----------------------------
inputs = sys.argv[1:]

"""
NOTE:- always use the absolute path for the file if possible, 
however you can use relative path also.
"""

# paths with absolute path-------------------------------------------
path1 = rf"--------------path to the folder needs to be here------------- \{inputs[0]}"
path2 = rf"--------------path to the folder needs to be here------------- \{inputs[1]}"

# main driver code----------------------------
if __name__ == "__main__":
    with open(path1, "rb") as fileobj11:
        with open(path2, "rb") as fileobj22:
            fileobj1 = PyPDF2.PdfFileReader(fileobj11)
            fileobj2 = PyPDF2.PdfFileReader(fileobj22)
            sys.exit(main(fileobj1, fileobj2))