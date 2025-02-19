class Employee:
    """Details of an employee."""
    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary
    def give_raise(self, annual_salary):
        if annual_salary:
            self.annual_salary += annual_salary
        else:
            self.annual_salary = annual_salary + 5000
        