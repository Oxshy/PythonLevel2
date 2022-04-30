class Car:
    def __init__(self,name,color):
        self.n1=name
        self.c1=color
    def dreamcar(self):
        print("One day I will buy",self.n1)
c1=Car("Nissan gtr","red")
c1.dreamcar()
c2=Car("Ferari","black")
c2.dreamcar()