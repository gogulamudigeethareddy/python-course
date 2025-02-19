from only_user_module import User

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
