print("Convert the time from 12 into 24")
def convert24(str1):
    #print(str[-2:])
    if(str1[-2:]=="am" and str1[0:2]=="12"):
        #print("00:"+str[3:-2])
        return "00:"+str1[3:-2]
    elif(str1[-2:]=="am"):
        return str1[0:-2]
    elif(str1[-2:]=="pm" and str1[0:2]=="12"):
        return str1[0:-2]
    else:
        return str(int(str1[0:2])+12)+":"+str1[3:-2]
print (convert24("01:24:24 pm"))
