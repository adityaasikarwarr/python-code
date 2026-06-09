class Library :
    def book_details(self):
        self.book_name = ""
        self.author_name = ""
        self.price = 0
        
    def add_book_details(self) :
        self.book_name = input("Enter the book name : ")
        self.author_name = input("Enter the author name : ")
        self.price = input("Enter the price of the book : ")
        
    def show_book_details(self) :
        print("LIBRARY BOOK DETAILS : ")
        print(self.book_name)
        print(self.author_name)
        print(self.price)
        
book1 = Library()
book2 = Library()

print("ADD BOOK DETAIL : ")
book1.add_book_details()

print("ADD BOOK DETAIL : ")
book2.add_book_details()

print("SHOW BOOK DETAILS : ")
book1.show_book_details()

print("SHOW BOOK DETAILS : ")
book2.show_book_details()