print("1.Superset")
print("2.subset")
print("3.Union")
print("4.intersection")
print("5.Symmetric difference")
print("6.set difference")
print("7.Disjoint")
print("8.length of set")
print("9.MAX value of set")
print("10.MIN value of set")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        if not(any(A) or any(B)):
            print("please Enter elements of Both sets")
            continue
        print(A.issuperset(B))
    elif ch==2:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print(A.issubset(B))
    elif ch==3:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print("Union :",A.union(B))
        #print("union :", A|B)
    elif ch==4:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print("Intersection:",A.intersection(B))
        #print("Intersectin:", A&B)
    elif ch==5:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print("Symmatric Difference:", A.symmetric_difference(B))
        #print(A^B)
    elif ch==6:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print("Set diffence:",A.difference(B))
        #print(A-B)
    elif ch==7:
        A=set(input("Enter set A:\n"))
        B=set(input("Enter set B:\n"))
        print("Disjoint:",A.isdisjoint(B))
    elif ch==8:
        A=set(input("Enter set A:\n"))
        print("Length of A:",len(A))
    elif ch==9:
        A=set(input("Enter set A:\n"))
        print("Largest element of set:",max(A))
    elif ch==10:
        A=set(input("Enter set A:\n"))
        print("Smallest element of set A:",min(A))
    else:
        break