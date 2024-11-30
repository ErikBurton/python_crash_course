mydict = {
    "make": "Chevy",
    "name ": "Camaro",
    "year": "2020",
    "sub_model": "SS"
}
x = mydict["make"]
y = mydict.get("year")
z = mydict.keys()
print(x) 

print(y)
print(z)

m = mydict.items()
print(m)
mydict["Engine"] = "LT4"
print(m)  

mydict["color"] = "black"

print(mydict)

if "model" in mydict:
    print("Yes, 'model' is one of the keys in the mydict dictionary")
else:
    print("Model is not in this dictionary")

# print(mydict)
# print(mydict["model"])
# print(type(mydict))

# newdict = dict(name="Erik", age=57, city="Riverton")
# print(newdict)
