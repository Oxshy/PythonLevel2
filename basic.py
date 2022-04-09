# print("hello world")
# def addnum(num1,num2):
#     #num1=43
#     #num2=212
#     print(num1+num2)

# addnum(43,10)
# addnum(23,2321)
#---------------------------swaping--------------------------------------------
# a=123
# b=2321
# a,b=b,a
# print(a,b)

#---------------------------dictionary--------------------------------------------
# d1={"Akshay":"Pizza","ASKSjasd":"icecream","jon":"curry"}
# print(d1["Akshay"])
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# for i,j in d1.items():
#     print(i,"likes to have",j)
#--------------------------slicing------------------------------
# strings="hello I am akshay" 
# strs=strings[0:6]
# print(strings[::2])
#print(strs[::-1])

#--------------------------------docstring--------------------------------
# def testing():
#     """This is a doc string"""
#     print("akshay")
# print(testing.__doc__)
# def add(x,y):
#     """this is for adding"""
#     #print(x+y)
#     return x+y
# print(add(5,4))
#--------------------------------Global--------------------------------



def fun():
    global a
    a=90
    print(a)
fun()
print(a)
