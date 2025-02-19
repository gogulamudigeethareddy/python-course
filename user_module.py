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
class Admin(User):
   def __init__(self, first_name, last_name, age):
       """
       Initialize attributes of parent class.
       Then initialize attributes specific to an admin.
       """
       super().__init__(first_name, last_name, age)
       self.privileges = Privileges()
class Privileges:
   def __init__(self):
       self.privileges = ['can add post','can delete post','can ban user']
   def show_privileges(self):
       """Print a privileges of the admin."""
       print(f"The following are the list of privileges the admin has:")
       for privilege in self.privileges:
           print(f"-{privilege}")

