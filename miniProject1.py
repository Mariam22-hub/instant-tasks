
class Library():

    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
    
    def displayBooks(self):
        if (len(self.bookslist)):
            for i in range(len(self.bookslist)):
                print(self.bookslist[i])
        else:
            print("library is empty")

           
    def lend(self,book):
        if (book in self.bookslist):
            self.bookslist.remove(book)
            print("process successful!")
        else:
            print("Apologies..Book not found")
        
    def add(self,book):
        self.bookslist.append(book)
        print("book added sucessfully!")

    def return_book(self, book):
        self.bookslist.append(book)
        print("book returned sucessfully!")

listbooks = []
name = "Harry"
n = None
users = {}
HarryLibrary = Library(listbooks, name)

if __name__ == '__main__':

    print("1.add a book\n 2.Lend a book\n 3.return a book\n 4.display books\n 5.exit" )

    while(True):    
        n = int(input("Enter your choice: "))

        if (n == 1):
            book = input("Enter the name of the book you'd like to add: ")
            HarryLibrary.add(book)
        
        elif(n == 2):
            name = input("please enter your full name: ")
            book = input("Enter the name of the book you'd like to lend: ")
            users[book] = name

            HarryLibrary.lend(book)
        
        elif(n == 3):
            name = input("please enter your full name: ")
            book = input("Enter the name of the book you'd like to return: ")
            if (name in users.values()):
                HarryLibrary.return_book(book)
            else:
                print("It appears you didn't lend any books in the first place")
            
        elif(n == 4):
            print("Displaying Books...")
            HarryLibrary.displayBooks()
        
        elif(n == 5):
            print("exited")
            break



