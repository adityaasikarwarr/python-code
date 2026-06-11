# class Book_managment :
#     def __init__(self , book_name , author_name):
#         self.book_name = book_name
#         self.author_name = author_name
        
# class book_details(Book_managment) :
#     def __init__(self,book_name , author_name ,  genre , price , ):
#         super().__init__(book_name , author_name)
#         self.book_genre = genre
#         self.book_price = price
        
#     def show_details(self):
#         print("BOOK DETAILS")
#         print("Book name = " , self.book_name)
#         print("Author name = ", self.author_name)
#         print("Book genre = " , self.book_genre)
#         print("Book price = " , self.book_price)
        
# books = book_details("CHanakya niti" , "Chanakya" , "political" , 900)
# books.show_details()



# class productionHouse :
#     def __init__(self , house_name):
#         self.production_house_name = house_name 
        
# class movie(productionHouse) :
#     def __init__(self, house_name , movie_name):
#         super().__init__(house_name)
#         self.movie_name = movie_name
        
# class actor(movie):
#     def __init__(self, house_name, movie_name , actor_name , actor_age):
#         super().__init__(house_name, movie_name)
#         self.actor_name = actor_name
#         self.actor_age = actor_age
        
#     def show_details(self):
#         print("MOVIE DETAILS")
#         print("House name = " , self.production_house_name)
#         print("Movie name = ", self.movie_name)
#         print("Actor name = ", self.actor_name)
#         print("Actor age = ", self.actor_age)
        
        
# actor_details = actor("T-series " , "Dhurandhar" , "Ranveer sigh", 34)
# actor_details.show_details()
    


class vehicle_managment :
    def __init__(self , vehicle_number , vehicle_brand):
        self.vehicle_number = vehicle_number
        self.vehicle_brand = vehicle_brand
        
class bus(vehicle_managment):
    def __init__(self, vehicle_number, vehicle_brand , load_capacity):
        super().__init__(vehicle_number, vehicle_brand)
        self.load_capacity = load_capacity
        
    def show_bus(self):
        print("BUS DETAILS")
        print("Bus number = " ,self.vehicle_number)
        print("Bus brand = ", self.vehicle_brand)
        print("Load capacity = ",  self.load_capacity)
        
class truck(vehicle_managment):
    def __init__(self, vehicle_number, vehicle_brand , load_capacity):
        super().__init__(vehicle_number, vehicle_brand)
        self.load_capacity = load_capacity
        
    def show_truck(self):
        print("Truck DETAILS")
        print("Truck number = " ,self.vehicle_number)
        print("Truck brand = ", self.vehicle_brand)
        print("Load capacity = ",  self.load_capacity)
        
bus_details = bus(1234 , "TATA" , "100 KG")
bus_details.show_bus()

truck_details = truck(6565 , "TATA" , "1000 KG")
truck_details.show_truck()