class Employee:

    variable_class = 0.19

    def __init__(self, fname, lname, email):
        # variables_instance
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello " + self.fname)
        print("Class Variables can be accessed this was: ", Employee.variable_class)

emp1 = Employee("Yagmur", "Gümüs", "yg@web.de")
emp1.greet_person()