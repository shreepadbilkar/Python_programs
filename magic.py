class operator:
    def __init__(self,*args):
        self.list=[arg for arg in args]
    def get(self):
        print(self.list)
    def __add__(self,other):
        zipped_list=zip(self.list,other.list)
        new_list=[n[0]+n[1] for n in zipped_list]
        return new_list
    def __sub__(self,other):
        zipped_list=zip(self.list,other.list)
        new_list=[n[0]-n[1] for n in zipped_list]
        return new_list
    def __mul__(self,other):
        zipped_list=zip(self.list,other.list)
        new_list=[n[0]*n[1] for n in zipped_list]
        return new_list
    def __floordiv__(self,other):
        zipped_list=zip(self.list,other.list)
        new_list=[n[0]//n[1] for n in zipped_list]
        return new_list
