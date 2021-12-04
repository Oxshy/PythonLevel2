print("this is a linear search")
def linearSearch(a,num):
   # print("I am inside linear search")
    #print(a,num)
    #print(len(a))
    for i in range(0,len(a)):
       # print(a[i])
        if(a[i]==num):
            print(i," is where its index on the array")
            return i
    return -1
            
        
        


arr=[56,12,565,76,567,563,23,87]

arrnum=int(input("Which number do you want to search up?"))

result=linearSearch(arr,arrnum)
# print(result)
if(result==-1):
    print("it is not in the array")
else:
    print("that is on the index number",result)

