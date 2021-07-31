
import json
a=["neelam","programer",24,2400,]
b=["komal","trainer",24,20000]
c=["anuradha","HR",25,40000]
d=["Abhishek","manager",29,63000]
key=["name","designation","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict5={"dict1":dict1,"dict2":dict2,"dict3":dict3,"dict4":dict4}
for i in range(len(a)):
    dict1.update({key[i]:a[i]})
for j in range(len(b)):
    dict2.update({key[j]:b[j]})
for k in range(len(c)):
    dict3.update({key[k]:c[k]})
for l in range(len(d)):
    dict4.update({key[l]:d[l]})
with open("pooja2.json","w")as f:
    json.dump(dict5,f,indent=6)


