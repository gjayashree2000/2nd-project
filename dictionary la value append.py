#create your own dictionary
dic={}
n=int(input("enter the no. of set"))
for i in range (n):
    #item=(input("enter the key and value separted by comma"))
    #list1=item.split(',')
    #key=list1[0]
    #value=list1[1]
    #dic[key]=value
#print(dic)
    key=int(input("enter the key"))
    value=int(input("enter the value"))
    dic[key]=value
print(dic)
vino
#sort the key
sorted(dic.keys())
print(sorted(dic.keys()))

#sort the value
sorted(dic.values())
print(sorted(dic.values()))

user=int(input("enter key need to check"))
if user in dic:
    print("key is present")
else:
    print("invalid key")    


   