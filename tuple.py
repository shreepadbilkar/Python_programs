while True:
    print("1: concatinating tuples")
    print("2: To find Max")
    print("3: get index of 'a' in tupple")
    print("4: to check if 'a' is in tupple")
    print("5: length of tuple")
    print("6: to reverse a tuple")
    print("7: repeatation")
    print("8: Sorting of tuple")
    print("9: to slice the tuple from 0 to 5th element ")
    print("10: To find Min element of tuple")
    
    ch = int(input("Enter your choice : "))
    if ch == 1:
        t1=tuple(input("Enter Tuple t1:"))
        t2=tuple(input("Enter Tuple t2:"))
        print("Concatination :",t1+t2)
    elif ch == 2:
        t=tuple(input("Enter tuple elements:"))
        print("largest:",max(t))
    elif ch == 3:
        t=tuple(input("Enter tuple elements:"))
        
        print("index of element: ", t.index('a'))
    elif ch == 4:
        t=tuple(input("Enter tuple elements:"))
        print("checking 'a' in tupple :", 'a' in t)
    elif ch == 5:
        t=tuple(input("Enter tuple elements:"))
        print("length of tuple:", len(t))
    elif ch == 6:
        t=tuple(input("Enter tuple elements:"))
        print("Reverse of tuple:",(t[::-1]))
    elif ch == 7:
        t=tuple(input("Enter tuple elements:"))
        print("Repeatation of tuple:", (t*2))
    elif ch == 8:
        t=tuple(input("Enter tuple elements:"))
        print("Sorting of tuple:", sorted(t))
    elif ch == 9:
        t=tuple(input("Enter tuple elements:"))
        print("Slicing tuple:",t[0:5])
    elif ch == 10:
        t=tuple(input("Enter tuple elements:"))
        print("Minimum:",min(t))
    else:
        break
