class Book_managment :
    def __init__(self , book_name , author_name):
        self.book_name = book_name
        self.author_name = author_name
        
class book_details(Book_managment) :
    def __init__(self,book_name , author_name ,  genre , price , ):
        super().__init__(book_name , author_name)
        self.book_genre = genre
        self.book_price = price
        
    def show_details(self):
        print("BOOK DETAILS")
        print("Book name = " , self.book_name)
        print("Author name = ", self.author_name)
        print("Book genre = " , self.book_genre)
        print("Book price = " , self.book_price)
        
books = book_details("CHanakya niti" , "Chanakya" , "political" , 900)
books.show_details()