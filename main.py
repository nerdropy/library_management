class Library:
    def __init__(self):
        self.lib = open('books.txt', 'a+')
        print("Library created.")

    def __del__(self):
        self.lib.close()
        print("Destructor called, Library deleted.")

    def listBooks(self):
        txt = self.lib.read().splitlines()
        for i in txt:
            print(i)

    def addBook(self):
        # self.title = title
        # self.author = author
        # self.year = year
        # self.pages = pages

        metadata = [x for x in input('Add the book information (title, author, year, pages):').split(', ')]
        wcomma = ', '.join(metadata)
        self.lib.write(f"{wcomma}\n")
        print(self.lib)



obj1 = Library()
obj2 = Library()
obj1.addBook()
obj2.addBook()

print(obj1)
        




