print("1.Convert String to UpperCase:")
print("2.Convert String to lowerCase:")
print("3.Check if 'a' is in String:")
print("4.Reverse String:")
print("5.Check count of 'a' in String:")
print("6.Slice String from 0 to 5th character:")
print("7.Check if String is Digit:")
print("8.split a String:")
print("9.Index of 'a' in String:")
print("10.concatinate two Strings:")
while True:
    ch=int(int(input("Enter your choice:")))
    if ch==1:
        s=input("Enter your string: \n")
        print("UperCase:",s.upper())
    elif ch==2:
        s=input("Enter your string: \n")
        print("LowerCase:",s.lower())
    elif ch==3:
        s=input("Enter your string: \n")
        print("chech 'a' is there or not:",'a' in s)
    elif ch==4:
        s=input("Enter your string: \n")
        print("Reverse String:",s[::-1])
    elif ch==5:
        s=input("Enter your string: \n")
        print("Count of 'a' in String:",s.count('a'))
    elif ch==6:
        s=input("Enter your string: \n")
        print("Slice String:",s[0:5])
    elif ch==7:
        s=input("Enter your string: \n")
        print("check if a is digit:",s.isdigit())
    elif ch==8:
        s=input("Enter your string: \n")
        print("Sliting of String:",s.split())
    elif ch==9:
        s=input("Enter your string: \n")
        print("Index of a in String:",s.index('a'))
    elif ch==10:
        s1=input("Enter your string1: \n")
        s2=input("Enter your string2: \n")
        print("Concatinate strings:",s1+s2)
    else:
        break