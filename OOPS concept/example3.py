class A:#super class
    var1="i am class variable of class a"
    def __init__(self):
        self.var1="instance variable of class a"
        self.special="special"

class B(A):#sub class
    var2="im class variable of class b"
    def __init__(self):
        super().__init__()
        self.var1="instance varbiable of class b"

#a=A()
b=B()
print(b.var1)
print(b.special)