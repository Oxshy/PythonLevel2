# #for i in range (4):
#     for j in range (4):
#         print("*",end="")
#     print("\r")

# for i in range (4):
#     for j in range (1+i):
#         print("*",end="")
#     print("\r")

# k=4
# for i in range (4):
#     for j in range (k):
#         print("*",end="")
#     k=k-1
#     print("\r")

# k=3
# for i in range (4):
#     for j in range (k):
#         print(" ",end="")
#     k=k-1
#     for j in range (1+i):
#         print("*", end="")
#     print("\r")

k=3
for i in range (4):
    for j in range (k):
        print(" ",end="")
    k=k-1
    for j in range (1+i):
        print("* ", end="")
    print("\r")