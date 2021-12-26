#FIVE TYPES OF EXCEPTION HANDLING MECHANISMS
import os
while True:
    print("1:FILE NOT FOUND ERROR:")
    print("2:TYPE ERROR:")
    print("3:IO ERROR:")
    print("4:FILE EXISTS ERROR:")
    print("5:ATTRIBUTE ERROR:")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 1:
        try:
            f = open('abc.txt', 'r')
            print()
            print("SUCCESSFULLY")
            print()
        except FileNotFoundError:
            print()
            print("FileNotFoundError")
            print()
    elif choice == 2:
        try:
            f = open('abc.txt', 'w', 'a')
            print()
            print("SUCCESSFULLY")
            print()
        except TypeError:
            print()
            print("TypeError")
            print()
    elif choice == 3:
        try:
            f = open('abc.txt', 'w+')
            f.write('sample content')
            f1 = open('ab.txt', 'r')
            print()
            print()
            print("SUCCESSFULLY")
        except IOError:
            print()
            print("IOError")
            print()

    elif choice == 4:
        try:
            f = os.path.exists('123.txt')
            print(f)
            if f == False:
                raise FileExistsError
            print()
            print("SUCCESSFULLY")
            print()
        except FileExistsError:
            print()
            print("FileExistError")
            print()
    elif choice == 5:
        try:
            f = open('abc.txt', 'a')
            f.open('abc.txt', 'r')
            print()
            print("SUCCESSFULLY")
            print()
        except AttributeError:
            print()
            print("AttributeError")
            print()
            break
    else:
        print("INVALID CHOICE!")
