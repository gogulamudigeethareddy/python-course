# guests = ["mark", "robert", "john", "sam", "lina"]
# guests[1] = "lisa"
# print(guests)
# message = f"You are invited to the dinner today."
# print(f"Hello {guests[0]}, {message}")
#
##sort and reverse
# places = ["Huawei","Switzerland","Finland","Alaska","France"]
# print(places)
# print(sorted(places))
# print(places)
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)
#
# #for loop
# animals = ["dog","cat","rabbit"]
# for animal in animals:
# print(f"{animal.title()}")
# print(f"{animal.title()} can be a great pet. \n")
# print(f"All these animals are not wild")

# for value in range(1,21):
# print(value)
#
# numbers = list(range(1,1000000))
# for number in numbers:
# print(number)

##slicing
# print(f"First three members in the guests list are:\n{guests[:3]}")
#
# print(f"Middle three members in the guests list are:")
# for members in guests[1:4]:
# print(members)
#
# print(f"Last three members in the guests list are:")
# for members in guests[-3:]:
# print(members)

##if statement
# alien_color = "green"
# if alien_color == "green":
# print("Player in the game earned 5 points")

# alien_color = "green"
# if alien_color == "red":
# print("Player in the game earned 5 points")

# alien_color = "red"
# if alien_color == "green":
# print("Player in the game earned 5 points")
# else:
# print("Player in the game earned 10 points")
#
# alien_color = "red"
# if alien_color == "green":
#    print("Player in the game earned 5 points")
# if alien_color == "yellow":
#    print("Player in the game earned 5 points")
# else:
#    print("Player in the game earned 15 points")
#
# age = 10
# if age < 2:
# print("Person is a baby")
# elif age >= 2 and age < 4:
# print("Person is a toddler")
# elif age >= 4 and age < 13:
# print("Person is a kid")
# elif age >= 13 and age < 20:
# print("Person is a teenager")
# elif age >= 20 and age < 65:
# print("Person is an adult")
# else:
# print("Person is an elder")
#
# favorite_fruits = ["banana","apple","grapes","orange"]
# if "apple" in favorite_fruits:
# print("You really like apple")
# if "pinapple" in favorite_fruits:
# print("You really like pinapple")
# if "banana" in favorite_fruits:
# print("You really like banana")
# if "strawberry" in favorite_fruits:
# print("You really like straberry")
# if "orange" in favorite_fruits:
# print("You really like orange")
# if "grapes" in favorite_fruits:
# print("You really like grapes")
#
# usernames = ["ggr123","admin","john12","pepsi","max123"]
# for username in usernames:
# if username == "admin":
# print("Hello admin, would you like to see a status report?")
# else:
# print(f"Hello {username.title()}, thank you for logging in again.")
#
# usernames = []
# if usernames:
# for username in usernames:
# if username == "admin":
# print("Hello admin, would you like to see a status report?")
# else:
# print(f"Hello {username.title()}, thank you for logging in again.")
#
# else:
# print("We need to find some users!")

# current_users = ["ggr123","admin","John12","pepsi","max123","Hazel","alisa"]
# new_users = ["alice","Mark","pepsi","lisa123","tom98","john12"]
# currentusers_lower = []
# for users in current_users:
# users = users.lower()
# currentusers_lower.append(users)
# for new_user in new_users:
# if new_user in currentusers_lower:
# print("Enter new username")
# else:
# print("username is available")
# #ordinal numbers
# num_list = [1,2,3,4,5,6,7,8,9]
# for num in num_list:
# if num == 1:
# print("1st")
# elif num == 2:
# print("2nd")
# elif num == 3:
# print("3rd")
# else:
# print(f"{num}th")

##Dictionaries

# person = {
# 'first_name' : 'John',
# 'last_name' : 'mark',
# 'age' : 25,
# 'city' : 'sfo',
# }
# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

# favorite_numbers = {
# 'leo' : 1,
# 'max' : 5,
# 'alisa' : 8,
# 'ted' : 2,
# 'mark' : 3,
# }
# print(favorite_numbers)

# rivers_dict = {'ganga': 'india', 'nile' : 'egypt', 'mississippi': 'america'}
# for river, country in rivers_dict.items():
# print(f"The {river.title()} runs through {country.title()}")
# for river in rivers_dict.keys():
# print(river.title())
# for country in rivers_dict.values():
# print(country.title())

# favorite_languages = {
#   'jen': 'python',
#   'sarah': 'c',
#   'edward': 'ruby',
#   'max': 'python',
# }
# list_of_people = ['cyan', 'glen', 'edward', 'violet', 'jen']
# for name in list_of_people:
# if name in favorite_languages.keys():
# print(f"Hi {name.title()}, thank you for participating in the poll.")
# if name not in favorite_languages.keys():
# print(f"Hi {name.title()}, please participate in the poll.")
#
#
# person_1 = {
# 'first_name' : 'John',
# 'last_name' : 'mark',
# 'age' : 25,
# 'city' : 'sfo',
# }
# person_2 = {
# 'first_name' : 'alice',
# 'last_name' : 'star',
# 'age' : 20,
# 'city' : 'nyc',
# }
# person_3 = {
# 'first_name' : 'leo',
# 'last_name' : 'max',
# 'age' : 30,
# 'city' : 'njc',
# }
# people = [person_1, person_2, person_3]
# for person in people:
# print(f"\nFirstname : {person['first_name'].title()}")
# print(f"Lastname : {person['last_name'].title()}")
# print(f"Age : {person['age']}")
# print(f"City : {person['city'].upper()}")
#
# pet_1 = {
# 'type' : 'dog',
# 'owner': 'lucy',
# }
# pet_2 = {
# 'type' : 'cat',
# 'owner': 'erin',
# }
# pet_3 = {
# 'type' : 'rabbit',
# 'owner': 'leo',
# }
# pet_4 = {
# 'type' : 'parrot',
# 'owner': 'ted',
# }
# pets = [pet_1, pet_2, pet_3, pet_4]
# for pet in pets:
# print(f"\nPet-type : {pet['type'].title()}")
# print(f"Pet-owner : {pet['owner'].title()}")

# favorite_places = {
# 'alice' : ['newyork', 'california', 'washington'],
# 'harry' : ['boston'],
# 'tim' : ['florida', 'hawaii'],
# }
# for name,places in favorite_places.items():
# if len(places) > 1:
# print(f"\n{name.title()}'s favorite places are:")
# for place in places:
# print(f"\t{place.title()}")
# else:
# print(f"\n{name.title()}'s favorite place is {place.title()}")
#
# favorite_numbers = {
# 'leo' : [1,3,7],
# 'max' : [5,2],
# 'alisa' : [4,8,6],
# 'ted' : [2,4,6,8],
# 'mark' : [1,3,9]
# }
# for name,fav_num in favorite_numbers.items():
# print(f"\n{name.title()}'s favorite numbers are:")
# for num in fav_num:
# print(f"\t{num}")
#
# cities = {
# 'newyork' : {
# 'country' : 'america',
# 'population' : 7888000,
# 'fact' : "The City's Original Name Was New Amsterdam."
# },
# 'delhi' : {
# 'country' : 'india',
# 'population' : 31488000,
# 'fact' : 'Delhi has the largest market of spices in Asia.'
# },
# 'mumbai' : {
# 'country' : 'india',
# 'population' : 21848000,
# 'fact' : 'Mumbai was originally made up of seven islands.'
# },
# }
# for city,details in cities.items():
#  print(f"{city.title()}")
#

# #input function

# required_car = input("Hello, what kind of rental car do you like? ")
# print(f"Let me see if I can find you a {required_car}.")
#
# number_of_people = input("How many people are there in the your dinner group? ")
# number_of_people = int(number_of_people)
# if number_of_people > 8:
# print(f"Please wait for a table.")
# else:
# print(f"Your table is ready")
#
# number = input("Tell me your favorite number: ")
# number = int(number)
# if number % 10 == 0:
# print(f"Number {number} is a multiple of 10.")
# else:
# print(f"Number {number} is not a multiple of 10")

# #while loop
#
# prompt = "\n Enter the topping you like: "
# prompt += "\n Enter 'quit' to exit."
# toppings = True
# while toppings:
# pizza_topping = input(prompt)
# if pizza_topping == 'quit':
# toppings = False
# else:
# print(f"\n Adding {pizza_topping} to your pizza.")
#
# age = input("Enter your age: ")
# active = True
# while active:
# age = int(age)
# if age < 3:
# print("Your ticket is free.")
# active = False
# elif age >= 3 and age < 12:
# print("Your ticket cost is $10.")
# active = False
# else:
# print("Your ticket cost is $15.")
# active = False

# prompt = "\n Enter the topping you like: "
# prompt += "\n Enter 'quit' to exit."
# while True:
# pizza_topping = input(prompt)
# if pizza_topping == 'quit':
# break
# else:
# print(f"\n Adding {pizza_topping} to your pizza.")
#
# infinite loop
# x = 1
# while x <= 5:
# print(x)
#
##while loop with list and dictionary
# sandwich_orders = ['chicken sandwich','spicy sandwich','veg sandwich','tuna sandwich']
# finished_sandwiches = []
# while sandwich_orders:
# order = sandwich_orders.pop()
# print(f"I made your {order}.")
# finished_sandwiches.append(order)
# print("\nThe sandwiches made are: ")
# for sandwich in finished_sandwiches:
# print(sandwich.title())

# sandwich_orders = ['chicken sandwich','pastrami sandwich','veg sandwich','pastrami sandwich','tuna sandwich','pastrami sandwich']
# finished_sandwiches = []
# print("We have run out of pastrami")
# while sandwich_orders:
# if 'pastrami sandwich' in sandwich_orders:
# sandwich_orders.remove('pastrami sandwich')
# else:
# order = sandwich_orders.pop()
# print(f"\nI made your {order}.")
# finished_sandwiches.append(order)
# print("\nThe sandwiches made are: ")
# for sandwich in finished_sandwiches:
# print(sandwich.title())

# polling_results = {}
# polling_active = True
# while polling_active:
# name = input("\nEnter your name: ")
# place = input("\nEnter the place you want to visit: ")
# polling_results[name] = place
# prompt = input("\nWould you like to let another person to add details?(yes/no) ")
# if prompt == 'no':
# break
# print("\nPolling results are: ")
# for name,place in polling_results.items():
# print(f"{name.title()} likes to visit {place.title()}.")

##Functions

# def display_message():
# """Display the message."""
# print("Hello everyone! Iam Learning Python.")
# display_message()
#
# def favorite_book(title):
# print(f"One of my favorite books is {title}.")
# favorite_book('Alice in Wonderland')

# def make_shirt(size,message):
# print(f"Shirt size is {size} with {message.upper()} as text on it.")
# make_shirt('medium','hello')
# make_shirt(size='medium', message='star')
#
# def make_shirt(size='large',message='I love Python'):
# print(f"\nShirt is {size} in size with a text of {message} on it.")
# make_shirt()
# make_shirt(size='medium')
# make_shirt(size='small',message='Rockstar')
#
# def describe_city(city, country='america'):
# print(f"\n{city.title()} is in {country.title()}.")
# describe_city('newyork')
# describe_city('mumbai',country='india')
# describe_city(city='delhi',country='india')
#

# #returning functions,dictionaries
# def city_country(city, country):
# """Return city and the country in a string."""
# details = f"{city}, {country}"
# return details.title()
# name = city_country('santiago', 'chile')
# print(name)
# name = city_country('newyork', 'america')
# print(name)
# name = city_country('delhi', 'india')
# print(name)
#
# def make_album(artist_name,album_title,):
# """Return a dictionary with album and artist names."""
# artist = {'Name': artist_name, 'Title': album_title}
# return artist
# music_album = make_album('Michael Jackson','Off the Wall')
# print(music_album)
# music_album = make_album('Taylor Swift','Red ink')
# print(music_album)
# music_album = make_album('Beyoncé','Renaissance')
# print(music_album)

# def make_album(artist_name,album_title,no_of_songs=None):
# """Return a dictionary with album and artist names."""
# artist = {'Name': artist_name, 'Title': album_title}
# if no_of_songs:
# artist = {'Name': artist_name, 'Title': album_title, 'No.of.songs':no_of_songs}
# return artist
# music_album = make_album('Taylor Swift','Red ink')
# print(music_album)
# music_album = make_album('Beyoncé','Renaissance',6)
# print(music_album)
#
# def make_album(artist_name,album_title):
# """Return a dictionary with album and artist names."""
# artist = {'Name': artist_name, 'Title': album_title}
# return artist
# while True:
# print("\nEnter artist name and title")
# print("\n(enter 'q' at anytime to quit.)")
# a_name = input('Artist name: ')
# if a_name == 'q':
# break
# t_name = input('Album title: ')
# if t_name == 'q':
# break
# music_album = make_album(a_name, t_name)
# print(music_album)
#
##lists in functions
# def show_messages(text_message):
# for message in text_message:
# print(message.title())
# messages = ['hello!', 'hi', 'good morning', 'good to see you.']
# show_messages(messages)
#
# def send_messages(messages,sent_messages):
#    """Print text message and moves eacmessage to sent_messages list."""
#    for message in range(len(messages)):
#  current_message = messages.pop()
#  print(f"Printing {current_message}")
#  sent_messages.append(current_message)
# def show_messages(messages,sent_messages):
#   """Print the lists."""
#   print(messages)
#   print(sent_messages)
# messages = ['hello!', 'hi', 'good morning', 'good to see you.']
# sent_messages = []
# send_messages(messages,sent_messages)
# show_messages(messages,sent_messages)
#
# def send_messages(messages,sent_messages):
#    """Print text message and moves eacmessage to sent_messages list."""
#    for message in range(len(messages)):
#  current_message = messages.pop()
#  print(f"Printing {current_message}")
#  sent_messages.append(current_message)
# def show_messages(messages,sent_messages):
#   """Print the lists."""
#   print(messages)
#   print(sent_messages)
# messages = ['hello!', 'hi', 'good morning', 'good to see you.']
# sent_messages = []
# send_messages(messages[:],sent_messages)    #copy of messages list is passed as argument so that it donot modify the original messages list
# show_messages(messages,sent_messages)
#
##arbitary number of arguments
# def sandwich(*items):
# """Print the sandwich order details with the items in the list."""
# print("\nYour sandwich is ready with the following items:")
# for item in items:
# print(item)
# sandwich('chicken','lettuce')
# sandwich('chicken','lettuce','cheese')
# sandwich('tomato')

# def build_profile(first, last, **user_info):    #(**kwargs)
# """Build a dictonary containing everything about a user."""
# user_info['first_name'] = first
# user_info['last_name'] = last
# return user_info
# user_profile = build_profile('alexa','henry',field='technology',location='california',country='america')
# print(user_profile)uu
#
# def make_car(manufacturer,model,**car_details):
# """Print a dictionary with the given info of the car."""
# car_details['Manufacturer'] = manufacturer
# car_details['Model'] = model
# return car_details
# car = make_car('toyota','camry',color='white',automatic=True)
# print(car)


##Classes

# class Restaurant:
# def __init__(self,restaurant_name,cuisine_type):
# self.name = restaurant_name
# self.type = cuisine_type
# def describe_restaurant(self):
# print(f"{self.name} is the name of the restaurant.")
# print(f"The cuisine served in the restaurant is {self.type}")
# def restaurant_open(self):
# print(f"The restaurant is open.")
# restaurant = Restaurant('hello','indian')
# print(restaurant.name)
# print(restaurant.type)
# restaurant.describe_restaurant()
# restaurant.restaurant_open()
#
# class Restaurant:
# def __init__(self,restaurant_name,cuisine_type):
# self.name = restaurant_name
# self.type = cuisine_type
# def describe_restaurant(self):
# print(f"{self.name} is the name of the restaurant.")
# print(f"The cuisine served in the restaurant is {self.type}.")
# def restaurant_open(self):
# print(f"The restaurant is open.")
# restaurant_1 = Restaurant('Taco de quella','Mexican')
# restaurant_2 = Restaurant('Paradise','Indian')
# restaurant_3 = Restaurant('Isbella','American Fusion')
# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()
#
# class User:
# def __init__(self,first_name,last_name,age):
# self.first = first_name
# self.last = last_name
# self.age = age
# def describe_user(self):
# """Summary of user information."""
# print(f"User information:")
# print(f"Full name: {self.first} {self.last}")
# print(f"Age: {self.age}")
# def greet_user(self):
# """Greeting the user."""
# print(f"Hello, {self.first} {self.last}")
# person = User('Henry','Clare',25)
# person.greet_user()
# person.describe_user()
# person2 = User('Lina','Daisy',22)
# person2.greet_user()
# person2.describe_user()

# class Restaurant:
# def __init__(self,restaurant_name, cuisine_type):
# self.name = restaurant_name
# self.type = cuisine_type
# self.number_served = 0
# def describe_restaurant(self):
# print(f"{self.name.title()} is the restaurant's name.")
# print(f"The cuisine served here is {self.type}")
# def open_restaurant():
# print("The restaurant is open.")
# def customers_served(self):
# print(f"This restaurant has served {self.number_served} customers.")
# restaurant = Restaurant('taco de casa', 'mexican')
# restaurant.customers_served()

# class Restaurant:
# def __init__(self,restaurant_name, cuisine_type):
# self.name = restaurant_name
# self.type = cuisine_type
# self.number_served = 0
# def describe_restaurant(self):
# print(f"{self.name.title()} is the restaurant's name.")
# print(f"The cuisine served here is {self.type}")
# def open_restaurant():
# print("The restaurant is open.")
# def customers_served(self):
# print(f"This restaurant has served {self.number_served} customers.")
# def set_number_served(self,number):
# self.number_served = number
# restaurant = Restaurant('taco de casa', 'mexican')
# restaurant.set_number_served(20)
# restaurant.customers_served()

# class Restaurant:
# def __init__(self,restaurant_name, cuisine_type):
# self.name = restaurant_name
# self.type = cuisine_type
# self.number_served = 0
# def describe_restaurant(self):
# print(f"{self.name.title()} is the restaurant's name.")
# print(f"The cuisine served here is {self.type}")
# def open_restaurant():
# print("The restaurant is open.")
# def customers_served(self):
# print(f"This restaurant has served {self.number_served} customers.")
# def set_number_served(self,number):
# self.number_served = number
# def increment_number_served(self,served):
# self.number_served += served
# restaurant = Restaurant('taco de casa', 'mexican')
# restaurant.set_number_served(20)
# restaurant.customers_served()
# restaurant.increment_number_served(45)
# restaurant.customers_served()

# class User:
    # def __init__(self, first_name, last_name):
        # self.first_name = first_name
        # self.last_name = last_name
        # self.login_attempts = 0
    # def describe_user(self):
        # """Prints a summary of the user profile."""
        # print(f"User Information:")
        # print(f"First Name: {self.first_name}")
        # print(f"Last Name: {self.last_name}")
        # print(f"Login Attempts: {self.login_attempts}")
    # def increment_login_attempts(self):
        # """Increments the value of login_attempts by 1."""
        # self.login_attempts += 1
    # def reset_login_attempts(self):
        # """Resets the value of login_attempts to 0."""
        # self.login_attempts = 0
# user_instance = User("John", "Doe")           #Creating an instance of the User class
# user_instance.increment_login_attempts()      #Calling increment_login_attempts several times
# user_instance.increment_login_attempts()
# user_instance.increment_login_attempts()
# print(f"Login Attempts (Before Reset): {user_instance.login_attempts}")     #Printing the value of login attempts before reset
# user_instance.reset_login_attempts()              #Calling reset_login_attempts
# print(f"Login Attempts (After Reset): {user_instance.login_attempts}")      #Printing the value of login attempts after reset
# 
##inheritance
# class Restaurant:
    # def __init__(self,restaurant_name,cuisine_type):
        # self.name = restaurant_name
        # self.type = cuisine_type
    # def describe_restaurant(self):
        # print(f"{self.name.title()} is the name of the restaurant.")
        # print(f"The cuisine served in the restaurant is {self.type.title()}.")
    # def restaurant_open(self):
        # print(f"The restaurant is open.")
# class IceCreamStand(Restaurant):
    # def __init__(self,restaurant_name,cuisine_type):
        #"""
        #Initialize attributes of parent class.
        #Then initialize attributes specific to IceCreamStand.
        #"""
        # super().__init__(restaurant_name,cuisine_type)
        # self.flavors = ['straberry','vanila','butterscotch','blueberry']
    # def show_flavors(self):
        # print(f"The following are the flavors of ice cream:")
        # for flavor in self.flavors:
            # print(flavor)
# icecreamstand = IceCreamStand('paradise','indian')
# icecreamstand.describe_restaurant()
# icecreamstand.show_flavors()
# 
# class User:
    # def __init__(self,first_name,last_name,age):
        # self.first = first_name
        # self.last = last_name
        # self.age = age
    # def describe_user(self):
        # """Summary of user information."""
        # print(f"User information:")
        # print(f"Full name: {self.first} {self.last}")
        # print(f"Age: {self.age}")
    # def greet_user(self):
        # """Greeting the user."""
        # print(f"Hello, {self.first} {self.last}")
# class Admin(User):
    # def __init__(self, first_name, last_name, age):
        # """
        # Initialize attributes of parent class.
        # Then initialize attributes specific to an admin.
        # """
        # super().__init__(first_name, last_name, age)
        # self.privileges = ['can add post','can delete post','can ban user']
    # def show_privileges(self):
        # """Print a privileges of the admin."""
        # print(f"The following are the list of privileges the admin has:")
        # for privilege in self.privileges:
            # print(f"-{privilege}")
# admin = Admin('alex','cary','35')
# admin.show_privileges()

# class User:
    # def __init__(self,first_name,last_name,age):
        # self.first = first_name
        # self.last = last_name
        # self.age = age
    # def describe_user(self):
        # """Summary of user information."""
        # print(f"User information:")
        # print(f"Full name: {self.first} {self.last}")
        # print(f"Age: {self.age}")
    # def greet_user(self):
        # """Greeting the user."""
        # print(f"Hello, {self.first} {self.last}")
# class Admin(User):
    # def __init__(self, first_name, last_name, age):
        # """
        # Initialize attributes of parent class.
        # Then initialize attributes specific to an admin.
        # """
        # super().__init__(first_name, last_name, age)
        # self.privileges = Privileges()
# class Privileges:
    # def __init__(self):
        # self.privileges = ['can add post','can delete post','can ban user']
    # def show_privileges(self):
        # """Print a privileges of the admin."""
        # print(f"The following are the list of privileges the admin has:")
        # for privilege in self.privileges:
            # print(f"-{privilege}")
# admin = Admin('alex','cary','35')
# admin.privileges.show_privileges()
# 
# class Car:                                      #parent class
    # """A simple attempt to represent a car."""
    # def __init__(self, make, model, year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # long_name = f"{self.year} {self.make} {self.model}"
        # return long_name.title()
    # def read_odometer(self):
        # print(f"This car has {self.odometer_reading} miles on it.")
    # def update_odometer(self, mileage):
        # if mileage >= self.odometer_reading:
            # self.odometer_reading = mileage
        # else:
            # print("You cannot roll back an odometer.")
    # def increment_odometer(self, miles):
        # self.odometer_reading += miles
# class Battery:
    # """A simple attempt to model a battery for an electic car."""
    # def __init__(self,battery_size=75):
        # """Initialize the battery's attributes."""
        # self.battery_size = battery_size
    # def describe_battery(self):
        # """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-kwh battery.")
    # def upgrade_battery(self):
        # if self.battery_size != 100:
            # self.battery_size = 100
    # def get_range(self):
        # """Print a range about the range this battery provides."""
        # if self.battery_size == 75:
            # range = 260
        # elif self.battery_size == 100:
            # range = 310
        # print(f"This car can go about {range} miles on a full charge.")
# class ElectricCar(Car):                         #child class
    # """Represent aspects of a car, specific to electric vehicles."""
    # def __init__(self,make,model,year):
        # """
        # Initialize attributes of parent class.
        # Then initialize attributes specific to an electric car.
        # """
        # super().__init__(make,model,year)
        # self.battery = Battery()
# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
 
##Importing modules
# import restaurant_module 
# new_restaurant = restaurant_module.Restaurant('bawarchi', 'indian')
# new_restaurant.describe_restaurant()

# from user_module import Admin, Privileges
# admin = Admin('Mary', 'Cooper', 30)
# admin.privileges.show_privileges()

# from only_user_module import User
# from admin_privileges_module import Admin, Privileges
# admin = Admin('harry', 'potter', 10)
# admin.privileges.show_privileges()
# 
##Python Standard Library
# from random import randint
# class Dice:
    # """Simple dice class"""
    # def __init__(self, sides):
        # self.sides = 6
    # def roll_dice(self):
        # random_number = randint(1,self.sides)
        # print(random_number)
# six_sided_dice = Dice(6)
# six_sided_dice.roll_dice()        
# six_sided_dice.roll_dice()
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# six_sided_dice.roll_dice()   
# 
# from random import randint
# class Dice:
    # """Simple dice class"""
    # def __init__(self, sides):
        # self.sides = 10
    # def roll_dice(self):
        # random_number = randint(1,self.sides)
        # print(random_number)
# ten_sided_dice = Dice(10)
# ten_sided_dice.roll_dice()        
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# ten_sided_dice.roll_dice()  
# 
# from random import randint
# class Dice:
    # """Simple dice class"""
    # def __init__(self, sides):
        # self.sides = 20
    # def roll_dice(self):
        # random_number = randint(1,self.sides)
        # print(random_number)
# twenty_sided_dice = Dice(20)
# twenty_sided_dice.roll_dice()        
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  
# twenty_sided_dice.roll_dice()  

# import random
# my_list = (4, 1, 'a', 5, 8, 'd', 'x', 10, 't', 2, 6, 'c', 3, 7, 9)
# random_select = []
# for select in range(4): 
    # random_select.append(random.choice(my_list))
# print("The ticket maching the below four numbers/letters wins the prize")
# print(random_select)

# from random import choice
# my_ticket = [5435, 678960, 766, 73897, 8475, 948574, 47520, 78436, 4785, 84732, 4875, 2831, 4910, 2038]
# winning_ticket = 8475
# loop_period = 0
# for ticket in my_ticket:
    # current_ticket = choice(my_ticket)
    # loop_period += 1
    # if current_ticket == winning_ticket:
        # print(f"{loop_period} times the loop had to run to give you the winning ticket.")
        # break


##FILES AND EXCEPTIONS


# with open('In_python.txt') as file_object:
    # contents = file_object.read()
    # print(contents)

# with open('In_python.txt') as file_object:
    # for line in file_object:
        # print(line.strip())
# 
# with open('In_python.txt') as file_object:
    # lines = file_object.readlines()
# for line in lines:
    # print(line.strip())
# 
# with open('In_python.txt') as file_object:
    # lines = file_object.readlines()
# line_string = ''
# for line in lines:
    # line_string += line.replace('Python', 'C')
# print(line_string)
# 
##Writing to the file
# filename = 'guest.txt'
# with open(filename, 'w') as file_object:
    # name = input("Enter your name: ")
    # file_object.write(name.title())
# 
# filename = 'guest_book.txt'
# with open(filename, 'w') as file_object:
    # while True:
        # name = input("Enter your name: ")
        # print(f"Hello, {name.title()}.")
        # file_object.write(f"{name.title()} visited.\n")
        # prompt = input("Do you need to quit(y/n)? ")
        # if prompt == 'y':
            # break
    # 
# filename = 'guest_opinion.txt'
# with open(filename, 'w') as file_object:
    # while True:
        # name = input("Enter your name: ")
        # print(f"Hello, {name.title()}.")
        # reason = input("Why do you like programming? ")
        # file_object.write(f"{name.title()} visited.\n")
        # if reason:
            # file_object.write(f"{reason.title()}.\n")
        # prompt = input("Do you need to quit(y/n)? ")
        # if prompt == 'y':
            # break    

##Exceptions
# print("Enter two numbers to add: ")
# print("enter 'q' to quit.")
# first_number = input("\nFirst number: ")
# second_number = input("\nSecond number: ")
# try:
    # result = int(first_number) + int(second_number)
# except ValueError:
    # print("Invalid input, value should be numerical.")
# else:
    # print(result)

# print("Enter two numbers to add: ")
# print("enter 'q' to quit.")
# while True:
    # first_number = input("\nFirst number: ")
    # if first_number == 'q':
        # break
    # second_number = input("\nSecond number: ")
    # if second_number == 'q':
        # break
    # try:
        # result = int(first_number) + int(second_number)
    # except ValueError:
        # print("Invalid input, value should be numerical.")
    # else:
        # print(result)
    
# print("Enter two numbers to add: ")
# print("enter 'q' to quit.")
# while True:
    # first_number = input("\nFirst number: ")
    # if first_number == 'q':
        # break
    # second_number = input("\nSecond number: ")
    # if second_number == 'q':
        # break
    # try:
        # result = int(first_number) + int(second_number)
    # except ValueError:
        # pass
    # else:
        # print(result)
# 
# def files(filename):
    # try:
        # with open(filename, encoding='utf-8') as f:
            # contents = f.read()
    # except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
    # else:
        # print(contents.title())
# filenames = ['dogs.txt', 'rabbits.txt', 'cats.txt']
# for filename in filenames:
    # files(filename)
# 
# def files(filename):
    # try:
        # with open(filename, encoding='utf-8') as f:
            # contents = f.read()
    # except FileNotFoundError:
        # pass
    # else:
        # print(contents.title())
# filenames = ['dogs.txt', 'cats.txt','rabbits.txt']
# for filename in filenames:
    # files(filename)
# 
# line = "Row, row, row your boat"
# print(line.count('row'))
# print(line.lower().count('row'))

# with open('buster_bear_book.txt') as f:
    # contents = f.read()
# words = contents.split()
# print(len(words))
# bear_num = contents.count('bear')
# print(bear_num)
# bear_num_total = contents.lower().count('bear')
# print(f"About {bear_num_total} times the word 'bear' appears in the file.")
# the_num = contents.lower().count('the') 
# print(f"About {the_num} times the word 'the' appears in the file.")
# the_total = contents.lower().count('the ')      ##since, there can be 'then' and 'there'... words
# print(f"About {the_total} times the word 'the ' appears in the file.")  

##JSON
# import json
# favorite_num = input("Enter your favorite number: ")
# filename = 'fav_number.json'
# with open(filename, 'w') as f:
    # json.dump(favorite_num, f)
# 
# import json
# filename = 'fav_number.json'
# with open(filename) as f:
    # favorite_num = json.load(f)
    # print(f"I know your favorite number! It's {favorite_num}.")

# import json
# try:
    # filename = 'fav_number.json'
    # with open(filename) as f:
        # favorite_num = json.load(f)
        # print(f"I know your favorite number! It's {favorite_num}.")
# except FileNotFoundError:
    # favorite_num = input("Enter your favorite number: ")
    # filename = 'fav_number.json'
    # with open(filename, 'w') as f:
        # json.dump(favorite_num, f)
# 
# import json 
# def get_stored_username():
    # """Get stored username if available."""
    # filename = "username.json"
    # try:
        # with open(filename) as f:
            # username = json.load(f)
    # except FileNotFoundError:
        # return None
    # else:
        # return username
# def get_new_username():
    # """Prompt for a new username."""
    # username = input("What is your name? ")
    # filename = "username.json"
    # with open(filename, 'w') as f:
        # json.dump(username, f)
    # return username
# def greet_user():     
    # """Greet the user by name."""
    # username = get_stored_username()
    # prompt = input(f"Are you a user with '{username}' as the username(y/n)? ")
    # if prompt == 'y':
        # print(f"Welcome back, {username}!")
    # else:
        # username = get_new_username()
        # print(f"We'll remember you when you come back, {username}!")
# greet_user()
# 

##Testing

# import unittest
# from city_functions import names # type: ignore
# class NamesTestCase(unittest.TestCase):
    # def test_city_country(self):
        # city_country = names('santiago', 'chile')
        # self.assertEqual(city_country, 'Santiago, Chile')
# if __name__ == '__main__':
#   unittest.main()
# 
# import unittest
# from city_functions import names # type: ignore
# class NamesTestCase(unittest.TestCase):
    # """Tests for city_functions.py"""
    # def test_city_country(self):
        # details = names('santiago', 'chile')
        # self.assertEqual(details, 'Santiago, Chile')
    # def city_country_population(self):
        # details = names('santiago', 'chile', 5000000)
        # self.assertEqual(details, 'Santiago, Chile - 5000000')
# if __name__ == '__main__':
#   unittest.main()
# 
import unittest
from employee_details import Employee
class EmployeeDetailsTestCase(unittest.TestCase):
    """Tests for employee details."""
    def setUp(self):
        self.details = Employee('tom', 'gret', 8000)
    def test_give_default_raise(self):
        initial_salary = self.details.annual_salary
        self.details.give_raise(5000)
        new_salary = self.details.annual_salary
        self.assertEqual(new_salary, initial_salary+5000)
    def test_give_custom_raise(self):
        initial_salary = self.details.annual_salary
        custom_raise = 2000
        self.details.give_raise(custom_raise)
        new_salary = self.details.annual_salary
        self.assertEqual(new_salary, initial_salary+custom_raise)
if __name__ == '__main__':
    unittest.main()
