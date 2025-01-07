from guizero import App, Box, Text, TextBox, PushButton

library = []

def make_a_list():
    library.append(book_input.value)

def add_book():
    main.hide()
    add_book_box.show()

def del_book():
    main.hide()
    del_book_box.show()

def remove_book():
    book_name = book_input1.value
    if book_name in library:
        library.remove(book_name)
    return_to_main()

def check_book():
    main.hide()
    check_book_box.show()

def book_existence():
    book_name = book_input2.value
    if book_name in library:
        status.value = f"'{book_name}' is in the list."
    else:
        status.value = f"'{book_name}' is not in the list."

def return_to_main():
    main.show()
    add_book_box.hide()
    del_book_box.hide()
    check_book_box.hide()

app = App(title="Manage library", width=500, height=450)
main = Box(app, visible=True, layout="grid")
Text(main, text="WELCOME TO THE LIBRARY!", size=12, color="black", grid=[1,0])
PushButton(main, text="Add books in the library", grid=[0,2], command=add_book)
PushButton(main, text="Remove books in the library", grid=[1,2], command=del_book)
PushButton(main, text="Find a book's existence", grid=[2,2], command=check_book)

add_book_box = Box(app, visible=False, layout="grid")
Text(add_book_box, text="Add books in the library", size=10, color="black", grid=[1,0])
Text(add_book_box, text="Enter the name of the book you want to add: ", size=8, color="black", grid=[0,1])
book_input = TextBox(add_book_box, width=15, grid=[1,1])
PushButton(add_book_box, text="Ok", grid=[2,1], command=make_a_list)
status = Text(add_book_box, text="", grid=[1,2])
PushButton(add_book_box, text="X", grid=[4,5], command=return_to_main)

del_book_box = Box(app, visible=False, layout="grid")
Text(del_book_box, text="Remove books from the library", size=10, color="black", grid=[1,0])
Text(del_book_box, text="Enter the name of the book you want to remove: ", size=8, color="black", grid=[0,1])
book_input1 = TextBox(del_book_box, width=15, grid=[1,1])
PushButton(del_book_box, text="Ok", grid=[2,1], command=remove_book)
PushButton(del_book_box, text="X", grid=[4,5], command=return_to_main)

check_book_box = Box(app, visible=False, layout="grid")
Text(check_book_box, text="Check book's existence in the library", size=10, color="black", grid=[1,0])
Text(check_book_box, text="Enter the name of the book you want to check: ", size=8, color="black", grid=[0,1])
book_input2 = TextBox(check_book_box, width=15, grid=[1,1])
PushButton(check_book_box, text="Ok", grid=[2,1], command=book_existence)
status = Text(check_book_box, text="", grid=[1,2])
PushButton(check_book_box, text="X", grid=[4,5], command=return_to_main)

app.display()
