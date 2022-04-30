class Cat:
    att1="mammal"
    att2="cat"
    def fun(self):
        print("I am a",self.att1)
        print("I am a",self.att2)
object1=Cat()
print(object1.att1)
object1.fun()
c2=Cat()  
print(c2.att2)
c2.fun()

