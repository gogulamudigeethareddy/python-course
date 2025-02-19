class User:
   def __init__(self,first_name,last_name,age):
       self.first = first_name
       self.last = last_name
       self.age = age
   def describe_user(self):
       """Summary of user information."""
       print(f"User information:")
       print(f"Full name: {self.first} {self.last}")
       print(f"Age: {self.age}")
   def greet_user(self):
       """Greeting the user."""
       print(f"Hello, {self.first} {self.last}")


       