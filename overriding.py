class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, empid, pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def display_details(self):
        print(f'''firstname is {self.first}
        lastname is {self.last}
        Employee id is {self.empid}
        Pay is {self.pay}''')


class Developer(Employee):
    raise_amt = 1.05

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Manager(Employee):

    raise_amt = 1.06

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp1 = Manager("The", "Manager", 1001, 20000)
emp2 = Developer("The", "Developer", 1002, 10000)

print(emp1.pay)
print(emp2.pay)

emp1.apply_raise()
emp2.apply_raise()

print(emp1.display_details())
print(emp2.display_details())
