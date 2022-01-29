import re
str1="this meeting will be counducted on 1st and 22nd of every month"
str2="one two three four five six seven 8 9 10"
#print(r"\n")
#esult=re.findall(r"\d",str1)
#result=re.findall(r"\d[\w]*",str1)
result=re.findall(r"\w{5}",str2)
print(result)