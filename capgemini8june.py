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
        print("Book name = " , self.book_name)
        print("Author name = " , self.author_name)
        print("Book Price = " , self.price)
        
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

class FoodItems :
    def item_details(self):
        self.item_name = ""
        self.item_price = 0
        self.item_quantity = 0
        
    def add_food_item(self):
        self.item_name = input("Enter your food item : ")
        self.item_price = int(input("Enter the price : "))
        self.item_quantity = int(input("Enter the quantity "))
        
    def show_item(self):
        print("FOOF ITEM DETAIL")
        print("Item name = " , self.item_name)
        print("Item price = " , self.item_price)
        print("Item quantity = " , self.item_quantity)
        
    def total_bill(self):
        self.item_price = self.item_price * self.item_quantity
        print("Total bill = ", self.item_price)
        
food_item1 = FoodItems()
food_item2 = FoodItems()

print("ENTER FOOD ITEM DETAILS :")
food_item1.add_food_item()
print("ENTER FOOD ITEM DETAILS :")
food_item2.add_food_item()

print("SHOW ITEM DETAILS :")
food_item1.show_item()

print("SHOW ITEM DETAILS :")
food_item2.show_item()

print("TOTAL BILL ITEM 1")
food_item1.total_bill()
print("TOTAL BILL ITEM 2")
food_item2.total_bill()