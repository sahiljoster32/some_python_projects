import PyPDF2
import sys

def from_pages():
    start = input("\nstart or means from which you to pick the pages\n")
    stop = input("\nstop or means at which page to stop\n")
    page_Set = (start, stop)
    return page_Set

def append_merger_fun(fileobj1, fileobj2):
    merger.append(fileobj1, None, None, True)
    specific_page = input("want to add only specific number of pages(Y/N) = ")
    if specific_page == "Y":
        page_SeT = from_pages()
    elif specific_page == "N":
        no_of_pages = fileobj2.getNumPages()
        page_SeT = (0, no_of_pages)
    merger.append(fileobj2, None, page_SeT, True)
    merger.write(rf"C:\Users\sahil jhangar\Desktop\pdf\Newly_appended_pdf.pdf")

def merge_pdf_position(fileobj1, fileobj2, page_no):
    specific_page = input("want to add only specific number of pages(Y/N) = ")
    merger.merge(0, fileobj1, None, None, True)
    if specific_page == "Y":
        page_SeT = from_pages()
    elif specific_page == "N":
        no_of_pages = fileobj2.getNumPages()
        page_SeT = (0, no_of_pages)
    merger.merge(page_no, fileobj2, None, page_SeT, True)
    merger.write(rf"C:\Users\sahil jhangar\Desktop\pdf\Newly_merged_pdf.pdf")

def ask_for_more():
    answer = int(input("do you want to continue (Y/N) = \n"))
    if answer == "Y":
        flag = 1
    elif answer == "N": 
        flag = 0
    return flag
    
def main(fileobj1, fileobj2):
    while True:
        print("what you want to do with these files\n")
        try:
            option = int(input("following are the option \n merge = 1 \n append = 2\n"))
        except ValueError:
            print("enter only integer value \nnow please try again !!!!!!!\n\n")
        if option == 1:
            extra_select = input("want to merge second pdf at specific page(Y/N) = ")
            if extra_select == "Y":
                page_no = int(input("\nat what you want to insert\n"))
            else:
                page_no = 0
            merge_pdf_position(fileobj1, fileobj2, page_no)
        elif option == 2:
            append_merger_fun(fileobj1, fileobj2)
        close = ask_for_more()
        if close == 0:
            break
        

merger = PyPDF2.PdfFileMerger()
inputs = sys.argv[1:]
path1 = rf"C:\Users\sahil jhangar\Desktop\pdf\{inputs[0]}"
path2 = rf"C:\Users\sahil jhangar\Desktop\pdf\{inputs[1]}"

if __name__ == "__main__":
    with open(path1, "rb") as fileobj11:
        with open(path2, "rb") as fileobj22:
            fileobj1 = PyPDF2.PdfFileReader(fileobj11)
            fileobj2 = PyPDF2.PdfFileReader(fileobj22)
            main(fileobj1, fileobj2)