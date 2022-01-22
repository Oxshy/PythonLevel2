# d={"hello":"a greeting","world":"earth"}
# x=input("enter the word: ")
# print(d[x])
import json
data=json.load(open("dictionary.json"))
#print(data)
def translate(w):
    # print(w)
    # return "hi"
    if w in data:
        return data[w]
word=input("enter the word: ")
output=translate(word)
if output==None:
    print("word not present in dictionary please check spelling or find an another word")
else:
    print(output)