import PyPDF2
import sys

merger = PyPDF2.PdfFileMerger()

path1 = rf"C:\Users\sahil jhangar\Desktop\pdf __ project\{inputs[0]}"
path2 = rf"C:\Users\sahil jhangar\Desktop\pdf __ project\{inputs[1]}"

def from_pages():
    start = input("start or means from which you to pick the pages\n")
    stop = input("stop or means at which page to stop\n")
    page_Set = (start, stop)
    return page_Set

def append_merger_fun(fileobj1, fileobj2, select):
    if select == 1:
        page_SeT = from_pages()
    for i in range(2):
        merger.append(fileobj1, None, page_SeT, True)

def merge_pdf_position(fileobj1, fileobj2, page_no):
    specific_page = input("want to only specific number of pages(Y/N) = ")
    merger.merge(0, fileobj1,None,None,True)
    if specific_page == "Y":
        page_SeT = from_pages()
    elif specific_page == "N":
        no_of_pages = fileobj2.getNumPages()
        page_SeT = (0,no_of_pages)
    merger.merge(page_no, fileobj2, None, page_SeT, True)

def main(fileobj1, fileobj2):
    while True:
        try:
            print("what you want to do with these files\n")
            option = int(input("following are the option \n merge \t = 1 \n append \t = 2\n"))
            if option == 1:
                extra_select = input("want to merge second pdf at specific page(Y/N) = ")
                if extra_select == "Y":
                    page_no = int(input("\nat what you want to insert\n"))
                else:
                    page_no = 0
                merge_pdf_position(fileobj1,fileobj2,page_no)   
            

if __name__ == "__main__"
with open(path1, "rb") as fileobj1:
    with open(path2, "rb") as fileobj2:
