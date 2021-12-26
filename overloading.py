#IMPLEMENTATION OF OVERLOADING CONCEPT
class person:
    def hello(self,name=None,age=None):
        if name is not None and age is None:
            print("hello"+name)
        elif name is not None and age is not None:
            print("hello"+name+"yourage="+str(age))
        else:
            print("hello")
obj=person()
obj.hello()
obj.hello("Shreepad")
obj.hello("Shreepad",23)
