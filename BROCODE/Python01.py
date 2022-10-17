#By sahansa jayawardhana instagram : @seasonsixty email : methjaya252@gmail.com

#V1 Printing
print('i love pizza')
print("it's really good")
print("hehe")


#V2 variables and int to typecasting to str()
age = 21

print("you are " + str(age) + " years old")
print("you are",age,"years old")
#f-string  -- insert f before ""
print(f"You are {age} years old")

#INTEGER

age  = 21
players = 2
quantity =5

print(f"you are {age} year old")
print(f"There ae {players} players online")
print(f"You would like to buy {quantity} items")

#FLOAT

gpa = 3.2
distance=2.5
price=10.99

print(f"your gpa is {gpa}")
print(f"you ran {distance} KM")
print(f"The Pricfe is ${price}")

#STRING

name = "Meth"
food = "pizza"
email = "methjaya252@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is : {email}")


#BOOLEAN

online = True
for_sale = False
running = True

print(f"Are you oline? : {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game is {running}")


if running:
    print("The game is runnig")
else:
    print("The game is not running")


#tricks with variables

x=1
y=2
z=3

print(x)
print(y)
print(z)

# we can use MULTIPLE ASSIGNMENT  rather using as above

x,y,z = 1,2,3


print(x)
print(y)
print(z)


# V3 - Typecasting
# Proces of converting a value of one data type to anoher
# (string,integer,float,boolean)
# Types of Typecastings : Explicit vs Implicit


#let's try Explicit typecasting
name = "Meth"
age = 21
gpa = 1.9
student = True

#print the type of variable
#should include type(name) in a print() to see what happens
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# convert to flaot
age = float(age)
print(age)
print(type(age))

# convert to int
gpa = int(gpa)
print(gpa)

# convert to string
print(type(student))
student= str(student)
print(student)
print(type(student))

# int to boolean
#when converting int to bool it gives True for all isntances except for int value is 0
age2=0
age3=-89

age= bool(age)
age2=bool(age2)
age3=(bool(age3))
print(age)
print(age2)
print(age3)

#string to bool
#unless the string is not "" - empty it will say true
#Even though it is empty in " " as there's a space it will say as True
name = bool(name)
print(name)
name2 = ""
name2=bool(name2)
print(name2)

#let's try Implicit typecasting

# in here, value/variable is converted to a different data type automatically
# x will automatically converted to float
# here there's no need to do a separate type casting in arithmatic ops like / ... it will automatically change

x=2
y=2.0

x=x/y
print(x)

# V4 - USER INPUTS

name =input("Enter your name " )
age = input("Enter your age ")
age = int(age)

print(f"You are now {age} years old")
age= age+1
print(f"Hello {name}")
print(f"You are {age} years old next year")

# we can do converting to int in single step for above scenario
# how??
age = int(input("Enter your age: "))
print(f"Age: {age}")

#Exercise 1 mad libs game

adjective1=input("Enter an adjective: ")
noun=input("Enter a noun: ")
adjective2=input("Enter an adjective: ")
verb=input("Enter a verb: ")
adjective3=input("Enter an adjective")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")


#Exercise 2 area calc

length = float(input("Enter the length of the rectangle "))
width = float(input("Enter the width of the rectangle "))
height = float(input("Enter the heght of the rectangle"))

area= length * width
volume = length * width * height
print(f"The area is {area} cm2 ")
print(f"The volume is {volume} cm3")


#Exercise 3 shopping cart

item = input("What item would you like to buy ? ")
price=float(input("What is the price ? "))
quantity=int(input("How many would you like ? "))

total = price*quantity

print(f"You have bought {quantity} x {item} /s")
print(f"Your total is: ${round(total,2)}")
#above we addded round(total,2) to round off upto 2 decimal places



#V5 Math in Python

friends = 10

#normal incrementing
# friends=friends+1  instead  we can use,

#augmented assignment operators


#friends=friends+1    ---> friends+=1
#friends=friends-2    ---> friends-=2
#friends=friends*3    ---> friends*=3
#friends=friends/4    ---> friends/=4
#friends=friends**2   ---> friends**=2

print(friends)

remainder = friends%3

print(remainder)



#BULT IN math related Functions

x=3.14
y=4
z=5

result1 = round(x)
#absoulte value - abs   : distance away from zero as a whole number
result2 = abs(y)

result3 = pow(4,3)

#find the maximum value
result4=max(x,y,z)

#find the minimum value
result5=min(x,y,z)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

