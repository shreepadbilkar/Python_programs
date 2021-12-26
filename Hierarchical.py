#Hierarchical Inheritance
class student:
    def __init__(self):
        self.usn = ' '
        self.name = ' '
        self.age = ' '

    def getdata(self):
        self.usn = input("enter usn:")
        self.name = input("enter name:")
        self.age = input("enter age:")

    def display(self):
        print("usn:", self.usn)
        print("name:", self.name)
        print("age:", self.age)


d = {}


class ugstudent(student):
    def __init__(self):
        super().__init__()
        self.sem = ' '
        self.fee = ' '
        self.stipend = ' '

    def uggetdata(self):
        super().getdata()
        self.sem = input("enter sem:")
        self.fee = input("enter fee:")
        self.stipend = input("enter stipend:")

    def display(self):
        super().display()
        print("sem : ", self.sem)
        print("fee : ", self.fee)
        print("stipend : ", self.stipend)


d1 = {}


class pgstudent(student):
    def __init__(self):
        self.sem = ' '
        self.fee = ' '
        self.stipend = ' '

    def pggetdata(self):
        super().getdata()
        self.fee = input("enter fee:")
        self.sem = input("enter sem:")
        self.stipend = input("enter stipend:")

    def diplay(Self):
        super().display()
        print("sem : ", self.sem)
        print("fee : ", self.sem)
        print("stipend : ", self.stipend)

    def dis(self):
        for key in d:
            print(key, d[key])


while True:
    ch = int(input(
        "\n 1.accept and display ug student details \n 2.display all students \n 3. accept and display pg details \n 4. display all pg students \n enter choice:"))
    if ch == 1:
        ug = ugstudent()
        ug.uggetdata()
        print("\n diplay \n")
        ug.display()
    elif ch == 2:
        d[ug.name] = ug.__dict__
        print(d)
    elif ch == 3:
        pg = pgstudent()
        pg.pggetdata()
        pg.display()
    elif ch == 4:
        d1[pg.name] = pg.__dict__
        print(d1)
    else:
        break
