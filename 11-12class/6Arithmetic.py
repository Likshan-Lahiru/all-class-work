#addition
 
a = 1 + 2

print("addition :",a)

#Subraction

b = 7 - 1

print("Subraction :",b)

#multiplication

c = 2 * 10

print("multiplication :",c)

#exponentiation

d = 3**8

print("exponentiation :", d) 

#divison

e = 10 / 5

print("divison",e)

#Floor division

f = 40 // 7

print("Floor division",f)




g = 10

g += 5

print(g)

#comparison operator

#comparison Equal
h = 5

print("comparison operator equal to:",h==5)
print("comparison operator equal to:",h==6)

#comparison Not Equal to

i = 10

print("comparison Not Equal :",i!=10)
print("comparison Not Equal :",i!=11)

#comparison Not Equal to
#less than " < "
#Greater than " >"
#less than or equal to " <= "
#greater than or equal than " >= "


#logical operator
x = 10 
y = 6

#Logical operator And
print("Logical operator And:",x<20 and y>3)
print("Logical operator And:",x>20 and y>3)

#Logical operator Or
print("Logical operator Or:",x>20 or y>3)
print("Logical operator Or:",x<5 or y>7)

#Logical operator Not
print("Logical operator Not:", not x>2)
print("Logical operator Not:", not x<2)

#activites

#y =input("Enter the value :")

#y = int(y)

#print(  y % 2 == 1 and (y<=100 and y>=0))

#Identity Operators

#compare the memomry locations of two objects

a = 10 **10
b = 1000

print("Identity Operators :" , a is b)
print("Identity Operators" ,a is not b)

#Membership operators

nums = [10, 20, 30, 1 , 4 ]

print("Membership operators :",4 in nums)
print("Membership operators :",5 not in nums)

#control flow Statement


l = -3
n = 10


#if else

if l % 2 == 0:
    print("This is EVEN Number")
else:
    print("This is ODD Number")

#else if

if l<0:
    print("This is negative Number!")
elif l>0:
    print("This is positive number!")
else:
    print("Zero")
    
#activites1

marks = input("Enter Your Marks :")

marks = int(marks)

if marks > 100 or marks<0 :
    print("Enter the valide marks(range 0-100)")
elif marks >= 85:
    print("Grade is A!")
elif marks >= 75:
    print("Grade is B!")
elif marks >= 65:
    print("Grade is C!")
elif marks >= 55:
    print("Grade is D!")
else:
    print("Grade is F!")

#activites2

M = 80
N = 1
O = 67


temp = M #80

if N > temp: #80
    temp = N #80
if O > temp: #80
    temp = O #80


print("Largest number is:", temp)

