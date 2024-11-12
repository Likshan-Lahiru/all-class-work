#ordered , changeable , does not allow duplicate , key values pair hold

dictionary_1 = {
    "name":"Sugar", 
    "price":250.50,
    "weight":"1KG"
}

#"name":"Sugar" key and value

print(dictionary_1,type(dictionary_1))

#do not allow dupliacte value replace last value 

dictionary_2 = {
    "name":"Sugar", 
    "price":250.50,
    "price":400.50,
    "weight":"1KG",
    
}
#print output {'name': 'Sugar', 'price': 400.5, 'weight': '1KG'}

print(len(dictionary_2))

#we can access value using key
print(dictionary_2["weight"])

#advnace dictonary
dictionary_3 = {
    "name":"lahiru", #String
    "price":250.50,  #float
    "grade":[20,30,40], #list
    "coordinate":(12.4, 56.78), #Tuple
    "preferences": {"Blue","Red","Green","Black"} #dictionary
}

#update dictinary item
dictionary_3["name"] = "Lahiru Lolitha"

print(dictionary_3)

#update method
dictionary_update = {
    "name":"lahiru", #String
    "price":250.50,  #float
    "age": 25
   
}
dictionary_update.update({"name":"Hiruni Thathsarani","price":500.10})

print(dictionary_update)

#add new key and value

dictionary_update["color"] = "white"

print(dictionary_update)

#remove item pop method

dictionary_update.pop("price")

print(dictionary_update)

#delete specific index

del dictionary_update["age"]

print(dictionary_update)

# del dictionary_update destroy full dictinary

#clear in dictinary 
dictionary_update.clear()
print(dictionary_update)


#copy another dic method 1 copy method

dict_1 = {
    "name": "sugar",
    "weight" "1kg"
    "price": 30
}

dict_2 = dict_1.copy()

dict_1["name"] = "rice"

print(dict_2)
print(dict_1)

#copy another dic method 2 dictinary constructor

dict_3 = dict(dict_1)

print(dict_3)

#key method

dict_4 = {
    "color": "green",
    "number": 1
}

print(dict_4.keys())