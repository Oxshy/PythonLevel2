f=open("test1.txt","r+")#a used for appending w used for writting r is used for reading r+ for all
print(f.read()) 
print("----------------------------------------------------------------------------")
f.write("\n Horses eat hay")
print(f.read()) 
#print(f.readline()) 
f.close()