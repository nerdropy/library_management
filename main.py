class Library:
    def __init__(self):
        self.lib = open('books.txt', 'a+')
        print("Library created.")

    def __del__(self):
        self.lib.close()
        print("Destructor called, Library deleted.")

    def listBooks(self):
        pass



