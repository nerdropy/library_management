class Library:
    def __init__(self):
        self.lib = open('books.txt', 'a+')
        print("Library created.")

    def __del__(self):
        self.lib.close()
        print("Destructor called, Library deleted.")

    def listBooks(self):
        self.lib.seek(0) #move the pointer to the beginning
        txt = self.lib.read().splitlines()
        for book in txt:
            title, author, year, pages = book.strip().split(', ')
            print(title, author, year, pages)
        self.lib.seek(0) #reset the pointer
            

    def addBook(self):
        metadata = [x for x in input('Add the book information (title, author, year, pages):').strip().split(', ')]
        wcomma = ', '.join(metadata)
        self.lib.write(f"{wcomma}\n")
        print(self.lib)

    def removeBook(self):
        delBook = input("Type the title of the book you want to delete: ")

        listof = self.lib.read().splitlines()

        for line in listof:
            new_list = line.split(', ') #assign the current book content to a list
            print(new_list)
            if new_list[0] == delBook: #check if the book title matches with the input
                listof.remove(line) #remove the contents of the book from the list
                self.lib.truncate(0) #remove all the content in the .txt file starting from the first byte
                for i in listof: #iterate for every element in the listof
                    self.lib.write(i+'\n') #write each element and add new line
                break


obj1 = Library()
#obj1.addBook()
obj1.listBooks()
obj1.removeBook()


print(obj1)
        




