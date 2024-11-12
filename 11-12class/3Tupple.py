sport = ("tennis", "cricket", "football")

#Tuple are ordered , unchangeable , allow duplicate values
#single variable can multiple data type 

print(len(sport))
print(type(sport))

sport_1 = ("Rugby",)#end of the tuple enter the " , " beac 

print(type(sport_1))

#negative index

#abtract tupple 
print(sport[0:2])


#we can't chnage value in tuples values
tuple_animal = ("Rat", "Dog", "Elepant")

#animal[1] = "Cat"

print(tuple_animal)

#but wen can work arround thing changable (chnage type tuple in to list) using tuple cuntructor

list_animal_2 = list(tuple_animal)

list_animal_2[2] = "Cat"

tuple_animal_3 = tuple(list_animal_2)

print(tuple_animal_3)

#tuple append remove


#activites
my_tuple_1 = (10,8,20,5)

my_tuple_2 = (5, 9 ,-1)

my_list_1 = list(my_tuple_1)

my_list_1.pop(2)

my_list_2 = my_list_1


new_tuple = tuple(my_list_2)

new_tuple_1 = new_tuple + my_tuple_2

print(sorted(new_tuple_1))

#Nested Tuple

nested_tuple = ((1,10,8), ("Dog", "Cat", "Rat"), (True, False))

print(nested_tuple[0][1])
print(nested_tuple[1][2])
print(nested_tuple[2][0])

