# import json
# j= '{"name":"jayesh","city":"indore","year":2020}'
# j=json.dumps(j)
# print(j)






# import json


# p={"name":"pooja rani","city":"delhi","year":2021}
# j=json.dumps(p)
# print(j)


# import json
# age=20
# salary=3400.50
# name= "pooja rani"
# print(json.dumps(age))
# print(json.dumps(salary))
# print(json.dumps(name))



# import json
# city=("delhi","pune","mumbai","bangalore","indore")
# print(json.dumps(city,indent=10))
# print(json.dumps(city))
# print(json.dumps(city,separators=("|",":")))






 
# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# } 
# my_file = open("myfile.json", "w")

# json.dump(dict1, my_file, indent = 6)

# my_file.close()





# import json

# a={"lalalalal": 3}
# mystring = json.dumps(a)
# print(mystring)



# import json
# j= {"Name":"Ram", 
# "Class":"IV", 
# "Age":9 }
# j=json.dumps(j)
# print(json.dumps(j,indent=4))





import json 
f=open("python_obj.json","r")
y=json.load(f)
print(y)
f.close()
    
