class A:#super class/base class
    var1="i am class variable of class a"
    def __init__(self):#init is a constructor funtion
        self.var1="instance variable of class a"
        self.special="special"

class B(A):#sub class/derived class
    var2="im class variable of class b"
    def __init__(self):
        super().__init__()
        self.var1="instance varbiable of class b"

#a=A()
b=B() #small b is an instance of class B, when you create instance b then by default constructor function works and initializ the value for instance(instance means memory)
print(b.var1)
print(b.special)