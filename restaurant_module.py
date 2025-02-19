class Restaurant:
    """Simple restaurant class"""
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.name.title()} is the name of the restaurant.")
        print(f"The cuisine served in the restaurant is {self.type.title()}.")
    def restaurant_open(self):
        print(f"The restaurant is open.")