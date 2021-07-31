import json
x={
    "shopping list":{
        "chaco":"15",
        "biscut":"12",
        "cadboury":"10",
        "vadapav":"20"

    }
}
print(type(x))
with open("shopping.json","w") as f:
    json.dump(x,f,indent=4)
name=input("which you want to buy")
items=int(input("how many item you want"))
for keys in x:
    for value in x:
        for i,k in x[keys].items():
            if i==name:
                t=int(k)-items