"""A set of classes that can be used to represent gas and electric car."""

class Car:                                      #parent class
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery:
    """A simple attempt to model a battery for an electic car."""
    def __init__(self,battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        """Print a range about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 310
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):                         #child class
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery = Battery()


##Importing a module into a module
        
# from pizza_module import make_pizza ##(pizza details are not required here, but if there is any other details in that module, it can be imported like this(an example only))


