from guizero import *
library = []

def make_a_list(app:App, book_input: TextBox):
    library.append(book_list.value)

def add_book(App, book_input: TextBox):
    main.hide()
    # del_book.hide()
    # check_book.hide()
    add_book.show()

def del_book():
    main.hide()
    # add_book.hide()
    # check_book.hide()
    del_book.show()
    for a in library:
       if a == book_input1.value:
            library.remove(book_input1.value)

def check_book():
    main.hide()
    check_book.show(library)


def book_existence():
    for v in library:
        if v == book_input2.value:
            if book_input2 in library:
                command=change_message3
            else:
                command=change_message4
        

def change_message1():
    show.value="The book has been added into the library."

def change_message2():
    show.value="The book has been removed from the library."
    
def change_message3():
    show.value="The book is in the library."

def change_message4():
    show.value="The book is not in the library."

def return_to_main():
    main.show()
    add_book.hide()
    del_book.hide()
    check_book.hide()

app = App(title="Manage library", width=500, height=450)
main = Box(app, visible=True, layout="grid")
Text(main, text="WELCOME TO THE LIBRARY!", size= 12, color="black", grid=[1,0])
PushButton(main, text="Add books in the library", grid=[0,2], command=add_book(app, ), args=book_input.value)
PushButton(main, text="Remove books in the library", grid=[1,2], command=del_book)
PushButton(main, text="Find a book's existence", grid=[2,2], command=check_book)

add_book = Box(app, visible=False, layout="grid")
Text(add_book, text="Add books in the library", size= 10, color="black", grid=[1,0])
Text(add_book, text="Enter the name of the book you want to add: ", size=8, color="black", grid=[0,1])
book_input = TextBox(add_book, width= 15, grid=[1,1])
PushButton(add_book, text="Ok", grid=[2,1], command=change_message1)
show = Text(add_book,text="", grid=[1,2])
PushButton(add_book, text="X", grid=[4,5], command=return_to_main)

del_book = Box(app, visible=False, layout="grid")
Text(del_book, text="Remove books from the library", size=10, color="black", grid=[1,0])
Text(del_book, text="Enter the name of the book you want to remove: ", size=8, color="black", grid=[0,1])
book_input1 = TextBox(del_book, width= 15, grid=[1,1])
PushButton(del_book, text="Ok", grid=[2,1], command=change_message2)
show1 = Text(del_book,text="", grid=[1,2])
PushButton(del_book, text="X", grid=[4,5], command=return_to_main)

check_book = Box(app, visible=False, layout="grid")
Text(check_book, text="Check a book's existence the library", size=10, color="black", grid=[1,0])
Text(check_book, text="Enter the name of the book you want to find: ", size=8, color="black", grid=[0,1])
book_input2 = TextBox(del_book, width= 15, grid=[1,1],)
PushButton(del_book, text="Ok", grid=[2,1], command=book_existence)
PushButton(check_book, text="X", grid=[4,5], command=return_to_main)
show2 = Text(del_book,text="", grid=[1,2])

app.display()
