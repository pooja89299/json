
import json


a=["neelam","programer","24","2400",]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]

dict1={}
dict2={}
dict3={}
dict4={}
key=["name","designation","age","salary"]

dict={"dict1":dict1,"dict2":dict2,"dict3":dict3,"dict4":dict4}


for i in range(len(a)):
    dict1.update({key[i]:a[i]})
    dict2.update({key[i]:b[i]})
    dict3.update({key[i]:c[i]})
    dict4.update({key[i]:d[i]})
with open("pooja3.json","w")as k:
    json.dump(dict,k,indent=5)