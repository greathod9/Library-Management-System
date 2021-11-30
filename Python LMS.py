import datetime
import os

#os.getcwd()

class LMS:
    """
    This class is used to keep record of books library.
    It has 4 modules: "Display Books", "Issue Books", "Return Books", "Add Books"
    """
    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n", ""), 
            "lender_name": "", "Issue_date": "", "Status": "Available"}})
            id = id+1
    
    def display_books(self):
        print("-----------------------List of Books-------------------------------")
        print("Book ID", "\t", "Title")
        print("-------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"), "]")
    
    def issue_books(self):
        book_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['Issue_date']}")
                return self.issue_books()
            elif self.books_dict[book_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[book_id]['lender_name'] = your_name
                self.books_dict[book_id]['Issue_date'] = current_date
                self.books_dict[book_id]['Status'] = "Already Issued"
                print("Books Issued Successfully!!\n")
        else:
            print("Book ID not found !!!")
            return self.issue_books()

    def add_book(self):
        new_book = input("Enter books title: ")
        if new_book == "":
            return self.add_book()
        elif len(new_book) > 25:
            print("Books title length is too long! Length should be 20 characters")
            return self.add_book()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'book_title': new_book, 'lender_name': "", 'Issue_date': "", 'Status': "Available"}})
                print(f"This books '{new_book}' has been added successfully!!!")

    def return_book(self):
        book_id = input("Enter book ID: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['Status'] == "Available":
                print("This book is already available in library. Please check you book ID.")
                return return_book()
            elif not self.books_dict[book_id]['Status'] == "Available":
                self.books_dict[book_id]['lender_name'] == ""
                self.books_dict[book_id]['Issue_date'] == ""
                self.books_dict[book_id]['Status'] == "Available"
                print("Successfully Updated!!\n")
        else:
            print("Book ID is not found")

try:
    myLMS = LMS("List.txt", "Guy's Library")
    press_key_list = {"D":"Display Books", "I":"Issue Books", "A":"Add Books", "R":"Return Books", "Q":"Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n--------------- Welcome to {myLMS.library_name} Library Management System --------------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection: Issue Books\n")
            myLMS.issue_books()
        elif key_press == "a":
            print("\nCurrent Selection: Add Books\n")
            myLMS.add_book()
        elif key_press == "d":
            print("\nCurrent Selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Books\n")
            myLMS.return_book()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("\nSomething went wrong. Please check your input\n")