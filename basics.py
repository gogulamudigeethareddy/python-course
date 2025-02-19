# first_name = "Geetha"
# last_name = "Reddy"
# full_name = f"{first_name} {last_name}"
# print(full_name) 

# print(f"Hello,{full_name.title()}")

# message = f"Hello, {full_name.title()}!"
# print(message)

# #cases
# name = "geetha"
# print(name.upper())
# print(name.lower())
# print(name.title())

# #Adding whitespace
# print("\tPython")
 
# print("Languages:\nPython\nC\nJava")

# print("Languages:\n\tPython\n\tC\n\tJava")

# #stripping whitespace
# language = ' python '
# language.lstrip()
# language.rstrip()
# language.strip()
# print(language)
# language = language.strip()
# print(language)

# frnd = "Eric"
# print(f"Hello {frnd}, would you like to learn some python today")
# print(frnd.upper())
# print(frnd.lower())

# universe_age = 14_000_000_000
# print(universe_age)

# print(4+4)
# print(20-12)
# print(2*4)
# print(16/2)

# a = 5
# hint = "When the first two digit number is divided by the smallest even number, a will be obtained" 
# print(hint)

# names = [ "cyan", "alice", "dora", "ben"]
# print(names)
# print(names[0])
# print(names[2].title())
# print(names[-1])
# print(f"{names[0].title()} is a beautiful girl.")

# names[1] = "Max"
# print(names)

# names.append("harry")
# print(names)

# names.append(["harry"])
# print(names)

# names.insert(2,"leo")
# print(names)

# del names[1]
# print(names)

# names.pop()
# print(names)

# popped_name = names.pop()
# print(names)
# print(popped_name)

# popped_name2 = names.pop(1)
# print(names)
# print(popped_name2)

# names.remove("dora")
# print(names)

# removed_name = names.remove("cyan")
# print(names)
# print(removed_name)

# names.sort()
# print(names)
# names.sort(reverse=True)
# print(names)

# print(sorted(names))
# print(names)

# names.reverse()
# print(names)

# print(len(names))


# #for loop
# for name in names:
#     print(name)
# for name in names:
#     print(f"{name.title()},have a good day")

# for value in range(1,6):
#     print(value)

# for value in range(6):
#     print(value)


# #numeric values
# numbers = list(range(6))
# print(numbers)

# #step
# numbers = list(range(1,11,2))
# print(numbers)

# squares = []
# for value in range(1,11):
#     squared_value = value**2
#     squares.append(squared_value)
# print(squares) 

# squares = [value**2 for value in range(1,11)]
# print(squares)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# #slicing
# print(names[0:2])
# print(names[:3])
# print(names[1:])
# print(names[-2:])
# print(names[0:3:2])

# for name in names[:3]:
#     print(name.title())

# food1 = ["pizza","coke","fries"]
# food2 = food1[:]
# print(food1)
# print(food2)
# food1.append("nuggets")
# food2.append("wings")
# print(food1)
# print(food2)

# food2 = food1    ##this will not work
# print(food2)   

# values = (10,15,20)
# print(values[0])
# print(values[1])
# print(values[2])

# values[0] = 5 ##causes error(tuples are immutable)

# value = (5,) ##single element tuple
# print(value)

# for value in values:
#     print(value)

# values = (30,40,50) ##Tuple can be changed like this(re-assigning all values)
# print(values)


# #If statement
# cars_list = ["audi","honda","bmw","hyuandi","benz"]
# for car in cars_list:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# pizza_topping = 'mushrooms'
# if pizza_topping != 'jalapeno' :
#     print("Hold the jalapeno topping!")

# a = 5
# if a == 5:
#     print(a)

# age = 20
# print(age >= 21 and age <= 21)

# age = 20
# print(age <= 21 and age <= 21)

# age = 20
# print(age >= 21 or age <= 21)

# age = 20
# print(age >= 21 or age >= 21)

# print("benz" in cars_list)

# print("acura" in cars_list)

# new_car = "lexus"
# if new_car not in cars_list:
#     print(f"Not in the list, new car - {new_car.title()}")

# age = 15
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Sorry,you are too young to vote")

# age = 20
# if age < 4:
#     print("Your admission fee cost is $0")
# elif age < 18:
#     print("Your admission fee cost is $20")
# else:
#     print("Your admission fee cost is $40")

# age = 10
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 20
# elif age <65:
#     price = 40
# else:
#     price = 20
# print(f"Your addmission fee is ${price}")

# age = 10
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 20
# elif age < 65:
#     price = 40
# elif age > 65:
#     price = 20
# print(f"Your addmission fee is ${price}")

# req_toppings = ["mushrooms","extra cheese"]
# if "mushrooms" in req_toppings:
#     print("Adding mushrooms")
# if "pineapple" in req_toppings:
#     print("Adding mushrooms")  
# if "extra cheese" in req_toppings:
#     print("Adding mushrooms")  
# print("\nFinished making pizza")

# requested_toppings = ["mushrooms","green peppers","extra cheese"]
# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers":
#         print("Sorry,we are out of green peppers right now")
#     else:
#         print(f"Adding {requested_topping}")
# print("\nFinished making your pizza")

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         if requested_topping == "green peppers":
#             print("Sorry,we are out of green peppers right now")
#         else:
#             print(f"Adding {requested_topping}")
# else:
#     print("\nDo you really want plain pizza?")
  
# available_toppings = ["mushrooms","olives","pinapple","red peppers","green peppers","extra cheese"]
# requested_toppings = ["mushrooms","french fries","extra cheese"]
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}")
#     else:
#         print(f"Sorry, we don't have {requested_topping}")
# print("\nFinished making your pizza")


# #dictionaries

# flowers = {'color': 'red','count': 5}
# print(flowers['color'])

# #adding values
# flowers['type'] = 'rose'
# print(flowers)

# #modifiying values
# flowers['color'] = 'yellow'
# print(flowers)

# #deleting
# del flowers['count']
# print(flowers)

# #storing similar objects
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'max': 'python',
# }
# fav_language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {fav_language}")

# #get()
# print(flowers['count'])    #error because 'count' does not exists
# count_value = flowers.get('count')
# print(count_value)
# count_value = flowers.get('count','No count value')
# print(count_value)

# #looping
# person = {
    # 'user_name' : 'admin',
    # 'first_name' : 'john',
    # 'last_name' : 'mark',
# }
# for key,value in person.items():
    # print(f"\nKey: {key}")
    # print(f"Value: {value}")
# 
# favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'max': 'python',
# }
# for name,language in favorite_languages.items():
    # print(f"{name.title()}'s favorite language is {language.title()}")
# 
# for name in favorite_languages.keys():
    # print(name)
# 
# special_friends = ['sarah','max']
# for name in favorite_languages.keys():
    # print(f"Hi {name.title()}")
    # if name in special_friends:
        # language = favorite_languages[name].title()
        # print(f"{name.title()}, I see you like {language}")
# 
# if 'elsa' not in favorite_languages.keys():
    # print("Elsa, please take the poll!")

# for name, language in sorted(favorite_languages.items()):
    # print(f"{name.title()}'s favorite language is {language.title()}")

# for language in favorite_languages.values():
    # print(language.title())
# 
# for language in set(favorite_languages.values()):    ##non-repetative
    # print(language.title())

# # nesting, Dictionaries in a list
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_3 = {'color': 'red', 'points': 15}

#for creating more aliens
# aliens = []
# for alien in range(30):
    # new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    # aliens.append(new_alien)

# for alien in aliens[:5]:   ##printing first 5 aliens
    # print(alien)
# print(".....")
# print(len(aliens))

# for alien in aliens[:3]:   ##changing colors of aliens
    # if alien['color'] == 'green':
        # alien['color'] = 'yellow'
        # alien['points'] = 10
        # alien['speed'] = 'medium'
# for alien in aliens[:5]:
    # print(alien)

# for alien in aliens[:3]:   ##changing colors of aliens
    # if alien['color'] == 'green':
        # alien['color'] = 'yellow'
        # alien['points'] = 10
        # alien['speed'] = 'medium'
    # elif alien['color'] == 'yellow':
        # alien['color'] = 'red'
        # alien['points'] = 15
        # alien['speed'] = 'fast'
# for alien in aliens[:5]:
    # print(alien)

# #lists in dictionary
# pizza = {
    # 'crust' : 'thick',
    # 'toppings' : ['mushrooms', 'extra cheese']
# } 
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
    # print(f"\t {topping}")
# 
# favorite_languages = {
    # 'jen' : ['python','ruby'],
    # 'sarah' : ['c'],
    # 'edward' : ['ruby', 'go'],
    # 'phil' : ['python', 'haskell'],
# }
# for name, languages in favorite_languages.items():
    # if len(languages) == 1:
        # print(f"\n{name.title()}'s favorite language is {languages[0].title()}")
    # else:
        # print(f"\n{name.title()}'s favorite language is:")
        # for language in languages:
            # print(f"\t{language.title()}")
# 
# #Dictionary in a dictionary
# users = {
    # 'mviolet' : {
        # 'first_name' : 'mark',
        # 'last_name' : 'violet',
        # 'location' : 'princeton',
    # },
    # 'sblack' : {
        # 'first_name' : 'sean',
        # 'last_name' : 'black',
        # 'location' : 'newyork',
    # }
# }
# for user_name, user_info in users.items():
    # print(f"\nUsername : {user_name}")
    # full_name = f"{user_info['first_name']} {user_info['last_name']}"
    # print(f"\tFull name : {full_name.title()}")
    # print(f"\tLocation : {user_info['location'].title()}")
# 

# #input() function
# name = input("Please enter your name: ")
# print(f"Hello, {name}!")
# 
#if longer than one line while asking for input:
# message = "If you tell who you are, we can personalize the messages you see."
# message += "\n What is your first name? "
# name = input(message)
# print(f"Hello, {name}!")

# age = input("How old are you? ")
# print(age)
# print(type(age))
# 
# age = input("How old are you? ")
# age = int(age)
# print(age)
# print(type(age))
# 
# #modulo operator
# print(4%2)

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
    # print(f"The number {number} is even.")
# else:
    # print(f"The number {number} is odd.")
# 
# #while loop

# current_number = 1
# while current_number <= 5 :
    # print(current_number)
    # current_number += 1 
# 
# prompt = "\n Tell me something, and I will repeat it back to you;"
# prompt += "\n Enter 'quit' to end the program."
# message = ""
# while message != 'quit':
    # message = input(prompt)
    # print(message)

# prompt = "\n Tell me something, and I will repeat it back to you;"
# prompt += "\n Enter 'quit' to end the program."
# message = ""
# while message != 'quit':
    # message = input(prompt)
    # if message != 'quit':
        # print(message)

# using flag
# prompt = "\n Tell me something, and I will repeat it back to you;"
# prompt += "\n Enter 'quit' to end the program."
# active = True
# while active:
    # message = input(prompt)F
    # if message == 'quit':
        # active = False
    # else:
        # print(message)

#Break 
# prompt = "\nEnter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' to end.) "
# while True:
    # city = input(prompt)
    # if city == 'quit':
        # break
    # else:
        # print(f"I'd love to go to the {city.title()}")

#Continue 
# current_num = 0         #printing odd numbers below 10
# while current_num < 10:
    # current_num += 1
    # if current_num % 2 == 0:
        # continue
    # print(current_num)
# 
##using while loop with lists
# unconfirmed_users = ["bran","alice","jon"]
# confirmed_users = []
# while unconfirmed_users:
    # current_user = unconfirmed_users.pop()
    # print(f"Verifiying user: {current_user.title()}")
    # confirmed_users.append(current_user)
# print("\nThe following users have been confirmed: ")
# for users in confirmed_users:
    # print(users.title())
# 
# pets = ['dog','cat','rabbit','cat','fish','dog','cat']
# print(pets)
# while 'cat' in pets:
    # pets.remove('cat')
# print(pets)
# 
##using while loop with dictionaries
# respone = {}
# polling_active = True
# while polling_active:
    # name = input("\nEnter your name: ")
    # dish = input("Enter your favorite dish: ")
    # respone[name] = dish
    # message = input("\nWould you like to let another person for the response? (y/n) ")
    # message = message.lower()
    # if message == 'n':
        # polling_active = False
# print("\nPolling is complete.Results are: ")
# for name,dish in respone.items():
    # print(f"{name}'s favorite dish is {dish}.")

##Functions

# def greet_user():
    # """Display a simple greeting."""
    # print("Hello!")
# greet_user() 
# 
# def greet_user(username):
    # """Display a simple greeting."""
    # print(f"Hello, {username.title()}!")
# greet_user('jesse')
# 
##Positional arguments
# def describe_pet(animal_type, pet_name):
    # """Display information about a pet."""
    # print(f"I have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster','harry')

# def describe_pet(animal_type, pet_name):
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster','harry')
# describe_pet('dog','while')
# 
# def describe_pet(animal_type, pet_name):
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type = 'hamster', pet_name = 'harry')

#Default vaules
# def describe_pet(pet_name, animal_type = 'dog'):    #default value is dog
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name = 'willie')    
# 
# def describe_pet(pet_name, animal_type = 'dog'):    #default value is dog
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name = 'harry', animal_type='hamster')    

##Function calling types
# def describe_pet(pet_name, animal_type = 'dog'):    
    # print(f"\nI have a {animal_type}.")
    # print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('willie')    
# describe_pet(pet_name='willie')
# describe_pet('harry','hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry',animal_type='hamster')

##Return values
# def get_formatted_name(first_name,last_name):
    # """Return a full name, neatly formatted."""
    # full_name = f"{first_name} {last_name}"
    # return full_name.title()
# name = get_formatted_name('alice','cary')
# print(name)
# 
# def get_formatted_name(first_name, middle_name, last_name):
    # """Return a full name, neatly formatted."""
    # full_name = f"{first_name} {middle_name} {last_name}"
    # return full_name.title()
# name = get_formatted_name('alice','jon','cary')
# print(name)

# #Optional argument
# def get_formatted_name(first_name, last_name, middle_name=''):
    # """Return a full name, neatly formatted."""
    # if middle_name:
        # full_name = f"{first_name} {middle_name} {last_name}"
    # else:
        # full_name = f"{first_name} {last_name}"
    # return full_name.title()
# name = get_formatted_name('alice','jon','cary')
# print(name)
# name = get_formatted_name('alice','cary')
# print(name)
# 
# #returning the dictionary
# def get_name(first_name, last_name):
    # """Return a dictionary of information about a person."""
    # person = {'first':first_name, 'last':last_name}
    # return person
# name = get_name('alex','rojer')
# print(name)
# 
# def build_person(first_name, last_name, age='None'):
    # """Return a dictionary of information about a person."""
    # person = {'first': first_name, 'last': last_name}
    # if age:
        # person['age'] = age
    # return person
# person_details = build_person('alexa', 'henry',25)
# print(person_details)
# 
# #Using while loop in functions
# def get_formatted_name(first_name, last_name):
    # """Return a full name, neatly formatted."""
    # full_name = f"{first_name} {last_name}"
    # return full_name.title()
# while True:
    # print("\n Enter your full name.")
    # print("(enter 'q' at anytime to quit)")
    # f_name = input("First name: ")
    # if f_name == 'q':
        # break
    # l_name = input("Last name: ")
    # if l_name == 'q':
        # break
    # name = get_formatted_name(f_name, l_name)
    # print(f"Hello, {name}!")
# 
# #Passing a list
# def greet_users(names):
    # """Print a simple greeting message to each user in the list."""
    # for name in names:
        # print(f"Hello, {name.title()}!")
# usernames = ['alex','bella','jon']
# greet_users(usernames)
# 
##modifying a list in the function
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_designs = []
# while unprinted_designs:    #printing the each design and moving each design to completed designs after printing.
    # current_design = unprinted_designs.pop()
    # print(f"Printing model: {current_design}")
    # completed_designs.append(current_design)
# print("\nThe following models have been printed:")
# for completed_design in completed_designs:
    # print(completed_design)
# 
##By using functions
# def print_models(unprinted_designs,completed_designs):
    # """Simulate printing each design, until none are left.
    #    Move each design to completed_designs after printing."""
    # while unprinted_designs:
        # current_design = unprinted_designs.pop()
        # print(f"Printing model: {current_design}")
        # completed_designs.append(current_design)
# def show_completed_models(completed_designs):
    # """Show all the models that were printed."""
    # print(f"\nThe following models have been printed:")
    # for design in completed_designs:
        # print(design)
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_designs = []
# print_models(unprinted_designs,completed_designs)
# show_completed_models(completed_designs)
# 
##Passing arbitrary no.of arguments
# def make_pizza(*toppings):   #Makes an empty tuple and add the values received.
    # """Print the list of toppings that have been requested."""
    # print(toppings)
# make_pizza('mushroom')
# make_pizza('pineapple','green peppers','extra cheese')

# def make_pizza(*toppings):   
    # """Summarize the pizza."""
    # print("\nMaking a pizza with the following toppings.")
    # for topping in toppings:
        # print(f"- {topping}")
# 
# make_pizza('mushroom')
# make_pizza('pineapple','green peppers','extra cheese')
# 
##mixing positional and arbitary arguments
# def make_pizza(size, *toppings):   #(*args)
    # """Print the list of toppings that have been requested."""
    # print(f"\nMaking a {size} inch pizza with the following toppings:")
    # for topping in toppings:
        # print(f"- {topping}")
# make_pizza(12,'mushroom')
# make_pizza(16,'pineapple','green peppers','extra cheese')
# 
##Arbitary keyword arguments
# def build_profile(first, last, **user_info):    #(**kwargs)
    # """Build a dictonary containing everything about a user."""
    # user_info['first_name'] = first
    # user_info['last_name'] = last
    # return user_info
# user_profile = build_profile('tom','halen',location='newyork',country='america')
# print(user_profile)
# 
##storing functions in modules
# import pizza_module            #file(module is a file ending with .py) will be imported
# pizza_module.make_pizza(16,'chicken')
# pizza_module.make_pizza(12,'mushrooms','green peppers','extra cheese')

# from pizza_module import make_pizza  # from module_name import function_name(importing specific functions)
# make_pizza(16, 'chicken')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 
# from pizza_module import make_pizza as mp    #Alias
# mp(16, 'chicken')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# import pizza_module as p     #Alias(increases readability)
# p.make_pizza(16, 'chicken')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from pizza_module import *    #(importing all functions in a module(not recommended in larger programs as there will be same names for functions,
# make_pizza(16, 'chicken')     #can get unexpected results)
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


## CLASSES
# 
# class Dog:
    # """Simple attempt to model a dog."""
    # def __init__(self,name,age):
        # """Initialize name and age attributes."""
        # self.name = name
        # self.age = age
    # def sit(self):
        # """Simulate a dog sitting in response to a command."""
        # print(f"{self.name} is now sitting.")
    # def roll_over(self):
        # """Simulate rolling over in response to a command."""
        # print(f"{self.name} rolled over!")

##instance
# class Dog:
    # """Simple attempt to model a dog."""
    # def __init__(self,name,age):
        # """Initialize name and age attributes."""
        # self.name = name
        # self.age = age
    # def sit(self):
        # """Simulate a dog sitting in response to a command."""
        # print(f"{self.name} is now sitting.")
    # def roll_over(self):
        # """Simulate rolling over in response to a command."""
        # print(f"{self.name} rolled over!")
# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# 
##calling methods
# class Dog:
    # """Simple attempt to model a dog."""
    # def __init__(self,name,age):
        # """Initialize name and age attributes."""
        # self.name = name
        # self.age = age
    # def sit(self):
        # """Simulate a dog sitting in response to a command."""
        # print(f"{self.name} is now sitting.")
    # def roll_over(self):
        # """Simulate rolling over in response to a command."""
        # print(f"{self.name} rolled over!")
# my_dog = Dog('Willie', 6)
# my_dog.sit()
# my_dog.roll_over()

##creating multiple instances
# class Dog:
    # """Simple attempt to model a dog."""
    # def __init__(self,name,age):
        # """Initialize name and age attributes."""
        # self.name = name
        # self.age = age
    # def sit(self):
        # """Simulate a dog sitting in response to a command."""
        # print(f"{self.name} is now sitting.")
    # def roll_over(self):
        # """Simulate rolling over in response to a command."""
        # print(f"{self.name} rolled over!")
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 8)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

##CAR Class
# class Car:
    # """A simple attempt to represent a car."""
    # def __init__(self,make,model,year):
        # """Initialize attributes to describe a car."""
        # self.make = make
        # self.model = model
        # self.year = year
    # def get_descriptive_name(self):
        # """Return a neatly formatted descriptive name."""
        # long_name = f"{self.make} {self.model} {self.year}"
        # return long_name.title()
# my_new_car = Car(2023,'audi','a4')
# print(my_new_car.get_descriptive_name())

##Setting default value for atribute
# class Car:
    # def __init__(self,make,model,year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # full_name = f"{self.make} {self.model} {self.year}"
        # return full_name.title()
    # def read_odometer(self):
        # """Print a statement showing the car's mileage."""
        # print(f"This car has {self.odometer_reading} miles on it.")
# my_new_car = Car(2023,'audi','a4')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

##Modifying attribute values(3 ways)
# class Car:                              #1st model(modifying attribute's value directly)
    # def __init__(self,make,model,year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # full_name = f"{self.make} {self.model} {self.year}"
        # return full_name.title()
    # def read_odometer(self):
        # """Print a statement showing the car's mileage."""
        # print(f"This car has {self.odometer_reading} miles on it.")
# my_new_car = Car(2023,'audi','a4')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 25
# my_new_car.read_odometer()

# class Car:                              #2nd model(modifying attribute's value through method)
    # def __init__(self,make,model,year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # full_name = f"{self.make} {self.model} {self.year}"
        # return full_name.title()
    # def read_odometer(self):
        # """Print a statement showing the car's mileage."""
        # print(f"This car has {self.odometer_reading} miles on it.")
    # def update_odometer(self,mileage):
        # """Set odometer reading to the give value."""
        # self.odometer_reading = mileage
# my_new_car = Car(2023,'audi','a4')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()

# class Car:                              #miles cannot roll back
    # def __init__(self,make,model,year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # full_name = f"{self.make} {self.model} {self.year}"
        # return full_name.title()
    # def read_odometer(self):
        # """Print a statement showing the car's mileage."""
        # print(f"This car has {self.odometer_reading} miles on it.")
    # def update_odometer(self,mileage):
        # """Set odometer reading to the give value."""
        # if mileage >= self.odometer_reading:
            # self.odometer_reading = mileage
        # else:
            # print("You cannot roll back an odometer.")
# my_new_car = Car(2023,'audi','a4')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()
# my_new_car.update_odometer(10)
# my_new_car.read_odometer()
# 
# class Car:                              #3rd model(incrementing attibute's value through method)
    # def __init__(self,make,model,year):
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
    # def get_descriptive_name(self):
        # full_name = f"{self.make} {self.model} {self.year}"
        # return full_name.title()
    # def read_odometer(self):
        # """Print a statement showing the car's mileage."""
        # print(f"This car has {self.odometer_reading} miles on it.")
    # def update_odometer(self,mileage):
        # """Set odometer reading to the give value."""
        # if mileage >= self.odometer_reading:
            # self.odometer_reading = mileage
        # else:
            # print("You cannot roll back an odometer.")
    # def increment_odometer(self,miles):
        # """Add the given amount to the odometer reading."""
        # self.odometer_reading += miles
# my_used_car = Car(2020,'toyota','camry')
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(25_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# 
##Inheritance
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
# class ElectricCar(Car):                         #child class
    # """Represent aspects of a car, specific to electric vehicles."""
    # def __init__(self,make,model,year):
        # """Initialize attributes of parent class."""
        # super().__init__(make,model,year)
# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# 
# #Defining attributes and methods of child class
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
# class ElectricCar(Car):                         #child class
    # """Represent aspects of a car, specific to electric vehicles."""
    # def __init__(self,make,model,year):
        # """
        # Initialize attributes of parent class.
        # Then initialize attributes specific to an electric car.
        # """
        # super().__init__(make,model,year)
        # self.battery_size = 75
    # def describe_battery(self):
        # """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-KWh battery.")
# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# 
##overiding methods from the parent class
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
# class ElectricCar(Car):                         #child class
    # """Represent aspects of a car, specific to electric vehicles."""
    # def __init__(self,make,model,year):
        # """
        # Initialize attributes of parent class.
        # Then initialize attributes specific to an electric car.
        # """
        # super().__init__(make,model,year)
        # self.battery_size = 75
    # def describe_battery(self):
        #  """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-KWh battery.")
    # def fill_gas_tank(self):                    #(overides the gas tank method from the parent class as the child class of electric car does not have gas tank.)
        # """Electric cars don't have gas tanks."""
        # print("This car doesn't need a gas tank.")
# my_tesla = ElectricCar('tesla', 'model s', 2022)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

##Instances as attributes(moving attributes and methods to a seperate class.)
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

##Importing classes
# from car_module import Car
# my_new_car = Car('audi', 'a5', '2022')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 25
# my_new_car.read_odometer() 

# from car_module import ElectricCar
# my_tesla = ElectricCar('tesla', 'model s', '2023')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# 
##Importing multiple classes
# from car_module import Car, ElectricCar
# my_bmw = Car('bmw', 'x3', 2022)
# print(my_bmw.get_descriptive_name())
# my_tesla = ElectricCar('tesla', 'roadster', 2023)
# print(my_tesla.get_descriptive_name())
# 
##Importing an entire module
# import car_module
# my_bmw = car_module.Car('bmw', 'x3', 2022)
# print(my_bmw.get_descriptive_name())
# my_tesla = car_module.ElectricCar('tesla', 'roadster', 2023)
# print(my_tesla.get_descriptive_name())
# 
##Importing all classes from the module
# from car_module import *        ##not recommended

##Aliasing
# from car_module import ElectricCar as EC

##Python standard library
# from random import randint
# print(randint(1,10))

# from random import choice
# players = ['alex', 'charles', 'michael', 'martina']     ##can be a list or a tuple 
# first_turn = choice(players)
# print(first_turn)
# 

##Files and Exceptions

##Reading from the file
# with open('pi.txt') as file_object:
    # contents = file_object.read()
# print(contents)
# 
# with open('pi.txt') as file_object:
    # contents = file_object.read()
# print(contents.rstrip())
# 
##If text file stored in another directory(Absolute file path)
# with open('folder_name/filename') as file_object    ##if text file is stored in a directory, the path can be mentioned like this.

##Reading line by line
# filename = 'pi.txt'
# with open(filename) as file_object:
    # for line in file_object:
        # print(line)

# filename = 'pi.txt'
# with open(filename) as file_object:
    # for line in file_object:
        # print(line.rstrip())      
# 
##Making a list of lines from a file
# filename = 'pi.txt'
# with open(filename) as file_object:
    # lines = file_object.readlines()
# for line in lines:
    # print(line.rstrip())

##Working with file contents
# filename = 'pi.txt'
# with open(filename) as file_object:
    # lines = file_object.readlines()
# pi_string = ''
# for line in lines:
    # pi_string += line.rstrip()
# print(pi_string)

# filename = 'pi.txt'
# with open(filename) as file_object:
    # lines = file_object.readlines()
# pi_string = ''
# for line in lines:
    # pi_string += line.strip()
# print(pi_string)
# 
##Large files
# filename = 'pi_million_digits.txt'
# with open(filename) as file_object:
    # lines = file_object.readlines()
# pi_string = ''
# for line in lines:
    # pi_string += line
# print(pi_string[:50])
# print(len(pi_string))
# 
# filename = 'pi_million_digits.txt'      ##Is birthday contained in pi value?
# with open(filename) as file_object:
    # lines = file_object.readlines()
# pi_string = ''
# for line in lines:
    # pi_string += line
# birthday = input("Enter your birthday in the form of mmddyy: ")
# if birthday in pi_string:
    # print("Your birthday appears in first million digits of pi.")
# else:
    # print("Your birthday doesnot appear in first million digits of pi.")

##Writing to the empty file
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
    # file_object.write("I love programming.")

##Writing multiple linws
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
    # file_object.write("I love programming.")
    # file_object.write("I love creating games.")
# 
# filename = 'programming.txt'
# with open(filename, 'w') as file_object:
    # file_object.write("I love programming.\n")
    # file_object.write("I love creating games.\n")
# 
# filename = 'programming.txt'
# with open(filename, 'a') as file_object:
    # file_object.write("I also love to work with large datasets.\n")
    # file_object.write("I love creating apps that can run in a browser.\n")
# 
# #Exceptions
##ZeroDivisionError
# print(5/0)    ##gets ZeroDivisionError

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
    # first_number = input("\nFirst number: ")
    # if first_number == 'q':
        # break
    # second_number = input("\nSecond number: ")
    # if second_number == 'q':
        # break
    # answer = int(first_number)/int(second_number)
    # print(answer)

##Try-Except blocks
# try:
    # print(5/0)
# except ZeroDivisionError:
    # print("You can't divide by zero!")
    
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
    # first_number = input("\nFirst number: ")
    # if first_number == 'q':
        # break
    # second_number = input("\nSecond number: ")
    # if second_number == 'q':
        # break
    # try:
        # answer = int(first_number)/int(second_number)
    # except ZeroDivisionError:
        # print("You can't divide by 0!")
    # else:
        # print(answer)
# 
##FileNotFoundError
# filename = 'alice.txt'
# with open(filename, encoding='utf-8') as f:
    # contents = f.read()

# filename = 'alice.txt'
# try:
    # with open(filename, encoding='utf-8') as f:
        # contents = f.read()
# except:
    # print(f"Sorry, the file {filename} does not exist.")
# 
# title = "Alice in wonderland"
# print(title.split())

# filename = 'resources/chapter_10/alice.txt'
# try:
#   with open(filename, encoding='utf-8') as f:
    #   contents = f.read()
# except:
#   print(f"Sorry, the file {filename} does not exist.")
# else:
#    words = contents.split()     #Counting the number of words in the file.
#    num_words = len(words)
#    print(f"The file {filename} has about {num_words} words.")
# 
##working with multiple files
# def count_words(filename):
    # try:
        # with open(filename, encoding='utf-8') as f:
            # contents = f.read()
    # except:
        # print(f"Sorry, the file {filename} does not exist.")
    # else:
        # words = contents.split()     #Counting the number of words in the file.
        # num_words = len(words)
        # print(f"The file {filename} has about {num_words} words.")
# filename = 'guest_opinion.txt'
# count_words(filename)    

# def count_words(filename):
    # try:
        # with open(filename, encoding='utf-8') as f:
            # contents = f.read()
    # except:
        # print(f"Sorry, the file {filename} does not exist.")
    # else:
        # words = contents.split()     #Counting the number of words in the fil
        # num_words = len(words)
        # print(f"The file {filename} has about {num_words} words.")
# filenames = ['guest_opinion.txt', 'guest_book.txt', 'programming.txt', 'In_python.txt']
# for filename in filenames:
    # count_words(filename)    

# def count_words(filename):
#    try:
    #    with open(filename, encoding='utf-8') as f:
        #    contents = f.read()
#    except:
    #    print(f"Sorry, the file {filename} does not exist.")
#    else:
    #    words = contents.split()     #Counting the number of words in the fil
    #    num_words = len(words)
    #    print(f"The file {filename} has about {num_words} words.")
# filenames = ['guest_opinion.txt', 'guest_book.txt', 'programming.txt', 'hello.txt','In_python.txt']
# for filename in filenames:
#    count_words(filename)    

##Failing silently(not showing exception-PASS statement)
# def count_words(filename):
#    try:
    #    with open(filename, encoding='utf-8') as f:
        #    contents = f.read()
#    except:
    #    pass
#    else:
    #    words = contents.split()     #Counting the number of words in the fil
    #    num_words = len(words)
    #    print(f"The file {filename} has about {num_words} words.")
# filenames = ['guest_opinion.txt', 'guest_book.txt', 'programming.txt', 'hello.txt', 'In_python.txt']
# for filename in filenames:
#    count_words(filename)    
# 
##Storing Data-JSON
# import json
# numbers = [2,5,11,8,14]
# filename = 'numbers.json'
# with open(filename, 'w') as f:
    # json.dump(numbers,f)
# 
# import json
# filename = 'numbers.json'
# with open(filename) as f:
    # numbers = json.load(f)
# print(numbers)
#    
# import json
# username = input("What is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f:
    # json.dump(username, f)
    # print(f"We'll remember you when you come back, {username}")
# 
# import json
# filename = 'username.json'
# with open(filename) as f:
    # username = json.load(f)
    # print(f"Welcome back, {username}!")
# 
##load the username, if it has been stored previously. Otherwise, prompt for username and store it.
# import json       
# filename = "username.json"
# try:
    # with open(filename) as f:
        # username = json.load(f)
# except FileNotFoundError:
    # username = input("What is your name? ")
    # with open(filename, 'w') as f:
        # json.dump(username, f)
        # print(f"We'll remember you when you come back, {username}!")
# else:
    # print(f"Welcome back, {username}!")
# 
##Refactoring-Making code easier to recognize by breaking it into small pieces/functions.
# import json 
# def greet_user():     
    # """Greet the user by name."""
    # filename = "username.json"
    # try:
        # with open(filename) as f:
            # username = json.load(f)
    # except FileNotFoundError:
        # username = input("What is your name? ")
        # with open(filename, 'w') as f:
            # json.dump(username, f)
            # print(f"We'll remember you when you come back, {username}!")
    # else:
        # print(f"Welcome back, {username}!")
# greet_user()
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
# def greet_user():     
    # """Greet the user by name."""
    # username = get_stored_username()
    # if username:
        # print(f"Welcome back, {username}!")
    # else:
        # username = input("What is your name? ")
        # filename = "username.json"
        # with open(filename, 'w') as f:
            # json.dump(username, f)
            # print(f"We'll remember you when you come back, {username}!")
# greet_user()

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
    # if username:
        # print(f"Welcome back, {username}!")
    # else:
        # username = get_new_username()
        # print(f"We'll remember you when you come back, {username}!")
# greet_user()

##Testing

# from name_function import get_formatted_name # type: ignore
# 
# print("Enter 'q' at anytime to quit.")
# while True:
    # first = input("\nPlease give me a first name: ")
    # if first == 'q':
        # break
    # last = input("Please give me a last name: ")
    # if last == 'q':
        # break
    # formatted_name = get_formatted_name(first, last)
    # print(f"\tNeatly formatted name: {formatted_name}.")
# 
# import unittest
# from name_function import get_formatted_name
# class NamesTestCase(unittest.TestCase):
    # """Tests for 'name_function.py'."""
    # def test_first_last_name(self):
        # """Do names like 'Janis Joplin' work?"""
        # formatted_name = get_formatted_name('janis', 'joplin')
        # self.assertEqual(formatted_name, 'Janis Joplin')
# if __name__ == '__main__':
    # unittest.main()

# import unittest
# from name_function import get_formatted_name
# class NamesTestCase(unittest.TestCase):
    # """Tests for 'name_function.py'."""
    # def test_first_last_name(self):
        # """Do names like 'Janis Joplin' work?"""
        # formatted_name = get_formatted_name('janis', 'joplin')
        # self.assertEqual(formatted_name, 'Janis Joplin')
    # def test_first_last_middle_name(self):
        # """Do names like 'Wolfgang Amadeus Mozart' work?"""
        # formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        # self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
# if __name__ == '__main__':
    # unittest.main()
# 
# from survey import AnonymousSurvey
# question = "What language did you first learn to speak?"    #Define a question
# my_survey = AnonymousSurvey(question)                       #Make a survey
# my_survey.show_question()                                   #Show the question
# print("Enter 'q' at anytime to quit.")
# while True:                                                 #Store responses
    # response = input("Language: ")
    # if response == 'q':
        # break
    # my_survey.store_response(response)
# print("\nThank you to everyone who participated in the survey!") #Show the results
# my_survey.show_results()
# 
# import unittest
# from survey import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
    # """Tests for class AnonymousSurvey"""
    # def test_store_single_response(self):
        # """Test that a single response is stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
# if __name__ == '__main__':
    # unittest.main()
# 
# import unittest
# from survey import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
    # """Tests for class AnonymousSurvey"""
    # def test_store_single_response(self):
        # """Test that a single response is stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
    # def test_store_three_responses(self):
        # """Test that three individual responses are stored properly"""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']
        # for response in responses:
            # my_survey.store_response(response)
        # for response in responses:
            # self.assertIn(response, my_survey.responses)
# if __name__ == '__main__':
    # unittest.main()
# 
# import unittest
# from survey import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
    # """Tests for the class AnonymousSurvey."""
    # def setUp(self):
        # """Create a survey and a set of responses for use in all test methods."""
        # question = "What language did you first learn to speak?"
        # self.my_survey = AnonymousSurvey(question) 
        # self.responses = ['English', 'Spanish', 'Mandarin']
    # def test_store_single_response(self):
        # """Test that a single response is stored properly."""
        # self.my_survey.store_response(self.responses[0])
        # self.assertIn(self.responses[0], self.my_survey.responses)
    # def test_store_three_responses(self):
        # """Test that three individual responses are stored properly."""
        # for response in self.responses:
            # self.my_survey.store_response(response)
        # for response in self.responses:
            # self.assertIn(response, self.my_survey.responses)
# if __name__ == '__main__':
    # unittest.main()






