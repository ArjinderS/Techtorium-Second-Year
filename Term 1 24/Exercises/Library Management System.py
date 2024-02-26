#Library Management System

decision = ["A", "D", "S", "Q"]
books = []

while True:
    library = input("Type A to add a book, D to display books, S to search books, or Q/Esc to quit: ")

    if library.lower() == "a":
        if len(books) >= 5:
            print("You have reached the maximum limit for adding books.")
        else:
            bookname = input("Enter book name: ")
            authorname = input("Enter author: ")
            genrename = input("Enter genre: ")
            books.append({"title": bookname, "author": authorname, "genre": genrename})
            print("The book {} by {} under the genre of {} has been added.".format(bookname, authorname, genrename))
    elif library.lower() == "d":
        if not books:
            print("No books have been added yet.")
        else:
            print("List of added books:")
            for index, book in enumerate(books, 1):
                print("{}: {} by {} ({})".format(index, book["title"], book["author"], book["genre"]))
    elif library.lower() == "s":
        search_query = input("Enter search query: ").lower()
        found_books = []
        for book in books:
            if search_query in book["title"].lower() or search_query in book["author"].lower() or search_query in book["genre"].lower():
                found_books.append(book)
        if found_books:
            print("Search results:")
            for index, book in enumerate(found_books, 1):
                print("{}: {} by {} ({})".format(index, book["title"], book["author"], book["genre"]))
    else:
        print("No matching books found.")
        exit()

    #Not sure about this
    next_action = input("Press any key to open library ")
    if next_action.upper() not in decision:
        #print(next_action + " is not a valid option.")
        continue
    else:
        library = next_action.upper()



'''
bookname1 = input("Enter book name: ")
authorname1 = input("Enter author: ")
genrename1 = input("Enter genre: ")
print("The book you selected is " + bookname1 + " by " + authorname1 + " under the genre of " + genrename1)

bookname2 = input("Enter book name: ")
authorname2 = input("Enter author: ")
genrename2 = input("Enter genre: ")
print("The book you selected is " + bookname2 + " by " + authorname2 + " under the genre of " + genrename2)

bookname3 = input("Enter book name: ")
authorname3 = input("Enter author: ")
genrename3 = input("Enter genre: ")
print("The book you selected is " + bookname3 + " by " + authorname3 + " under the genre of " + genrename3)

bookname4 = input("Enter book name: ")
authorname4 = input("Enter author: ")
genrename4 = input("Enter genre: ")
print("The book you selected is " + bookname4 + " by " + authorname4 + " under the genre of " + genrename4)

bookname5 = input("Enter book name: ")
authorname5 = input("Enter author: ")
genrename5 = input("Enter genre: ")
print("The book you selected is " + bookname5 + " by " + authorname5 + " under the genre of " + genrename5)


# Default function to run if else condition  
def NumberCheck(a):   
    # Checking if the number is positive  
    if a > 0:   
        print("The number you gave is positive")   
    # Checking if the number is negative   
    elif a < 0:   
        print("The number you gave is negative")   
    # Else the number is zero  
    else:   
        print("The number you gave is Zero")  
# Taking number from user  
a = float(input("Enter a number as input value: "))  
# Printing result  
NumberCheck(a) 



import uuid

# Generate a random UUID (UUID4) unique identifier/ID/Primary key
unique_id = uuid.uuid4()

print(unique_id)

# I think this is for a separate database, ours should only be in the program ???
class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
'''