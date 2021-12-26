class STUDENT(object):
    def __init_(self, usn, name, age):
        self.usn = usn
        self.name = name
        self.age = age

    def dispaly(self):
        print(self.usn)
        print(self.name)
        print(self.age)


class UGSTUDENT(STUDENT):
    def __init_(self, sem, fees, stipend):
        usn = input('enter your usn number')
        name = input('enter your name')
        age = input('enter your age')
        self.semester = input('enter semester')
        self.fees = int(input('enter fee'))
        self.stipend = int(input('enter your stipend'))
        STUDENT.__init_(self, usn, name, age)
        STUDENT.display(self)
        UGSTUDENT.display(self)

    def display(self):
        print(self.semester)
        print(self.fees)
        print(self.stipend)


class PGSTUDENT(STUDENT):
    def __init_(self):
        usn = input('enter your usn number:')
        name = input('enter you name:')
        age = input('enter your age:')
        self.semester = input('enter semester:')
        self.stipend = int(input('enter your stipend:'))
        STUDENT.__init_(self, usn, name, age)
        STUDENT.dispaly(self)
        PGSTUDENT.display(self)

    def display(self):
        print(self.semester)
        print(self.fees)
        print(self.stipend)


while True:
    print('1.if ugstudent\n 2.if pg student')
    ch = int(input('enter your choice'))
    if not(ch):
        print('enter choice is empty')
    else:
        if ch == 1:
            ug = UGSTUDENT()
        elif ch == 2:
            pg = PGSTUDENT()
        else:
            print('wrong choice entered')
            break
