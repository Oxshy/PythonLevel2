# try:
#     print(10/0)
# except NameError:
#     print("Name error occured")
# except ArithmeticError:
#     print("error occured")

# finally:
#     print("Welcome")

# print("Hello I am Akshay")

name=input("enter your name: ")
if name.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {name}")