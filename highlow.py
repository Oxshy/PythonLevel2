import random
# print("HIGHLOW")
# number=[1,2,3,4,5,6,7,8,9,10]
# numbers=random.choice(number)
# print(numbers)
# x= int(input("Guess a number between 0 and 11 you have 3 attempts: "))
# if x!=numbers:
#     if x<numbers:
#         print("Too low")
#     elif x>numbers:
#         print("Too high")
#     y=int(input("try again: "))
#     if y==numbers:
#         print("BINGO")
#     elif y!=numbers:
#         if y<numbers:
#             print("Too low")
#         elif y>numbers:
#             print("Too high")
#         z=int(input("last try: "))
#         if z==numbers:
#             print("BINGO")
#         elif z!=numbers:
#             print("you lost")

# elif x==numbers:
#     print("BINGO")

#do it using while loop
number=[1,2,3,4,5,6,7,8,9,10]
numbers=random.choice(number)
trys=1
print(numbers)
while trys<=3:
    y=int(input("guess a number from one to 10 "))
    if y==numbers:
        print("BINGO")
        break
    elif y<numbers:
        print("too low")
        trys+=1
    elif y>numbers:
        print("too high")
        trys+=1
if trys==4:
    print("GAME OVER")
