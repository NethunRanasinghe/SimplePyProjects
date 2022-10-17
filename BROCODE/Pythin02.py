
# math Module

import math

#value of pi  value
print(math.pi)

#e value --but not gonna use in this series
print(math.e)
#square root

a=9
b=3.1
result6=math.sqrt(a)
print(result6)


#round off floating value always up
result7= math.ceil(b)
print(result7)


#ropund off flaoting value always down
result8= math.floor(b)
print(result8)


#circumference and area of a circle
import math

radius=float(input("Enter the radius of a circle : "))

circumference = 2 * math.pi *radius

print(f"The circumference is: {round(circumference,2)}")

area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area)}cm2")



#hypothenus of a rigt angled traingle

import math

a=float(input("Enter side A "))
b=float(input("Enter side B "))

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"Side C = {c}")



# V6  Control Flow in Python (if, elif, else)


#if and elif

age= int(input("Enter your age "))

if age>=60:
    print("You are way older to sign up !!! ")
elif age<0:
    print("You haven't been born yet .. hahah !!!")
elif age>=18:
    print("Eligible")
else:
    print("Not Eligible")



response = input("Would yopu like food?(Y/N) ")

if response == "Y":
    print("Have some food !!!")
elif response =="y":
    print("Have some food  !!!")
elif response =="n":
    print("No food for you !!!")
elif response =="N":
    print("No food for you !!!")
else:
    print("Invalid input !!!")



#above one in a simple way using OR operator
res = input("Want? (Y/N)")

if (res=="y") or (res=="Y"):
    print("Ok")
elif (res=="n") or (res=="N"):
    print("No")
else:
    print("Invalid !!!")

#V7 CALCULATOR

operator = input("Input an operator (+ - * /) ")

if ((operator=="+") or (operator=="-") or (operator=="/") or (operator=="*")):
    print("Okay, Operator is valid")
else:
    print("Invalid operator !!!")
    breakpoint()
num1 = float(input("Enter number 01 : "))
num2 = float(input("Enter number 02 : "))



if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1* num2
    print(round(result,3))
else:
    result = num1/num2
    print(round(result,3))




# V8 Temparature Convertion     (C*9/5)+32 = F     and (F-35)*5/9 -= C

unit = input("Is this temparature in Celcius or Fahrenheit (C/F) ?")
temp=float(input("Enter the temperature "))

if (unit == "C") or (unit == "c"):
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenhite is : {temp} F")
elif (unit=="F") or (unit=="f"):
    # to pass the process we can use  ---> pass
    temp= round((temp-32)*5/9,1)
    print(f"The temperature in Celcius is : {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement !!!!")

"""

"""
# V9 Logical Operators

#and
#or
#not

temp=25
if temp>0 and temp<30:
    print("Temperature is Good")
else:
    print("Temperature is Bad !!!")

temp2=0
if temp2<=0 or temp>=30:
    print("Temperature is Bad !!! ")
else:
    print("Temperature is Good")

Sunny= False

if not Sunny:
    print("It is Sunny ")
else:
    print("It is not Sunny")
    



# V10 String Methods

# A String is a series of characters

#useful string methods

#length of a String
name = input("Enter your full name : ")
result = len(name)
print(result)

#find merthod will return the first occurance of the given character : the position
#that means keeweni position ekeda me api find eka athule daana letter eka thyenne kiyali
name2 = input("Enter the Word 1 :")
result2=name2.find("a")
print(result2)

#if we need the last occurance
#aga idala e adala character eka mulinma hambenne keewinyatada thiynne kiyala hoaynna

result3= name2.rfind("a")
print(result3)

#if can't find it will say -1


#CAPITALIZE fir character of a String ----> name.capitalize()

name3=name2.capitalize()
print(name3)
#UPPER METHOD will make all the characters Uppercase

name4=name2.upper()

print(name4)

#LOWER Method will make all trhe character LOWERCASE

name5=name2.lower()
print(name5)


#If a String contains only intergers ???   ---> isdigitr()
#True -- only there's integers
name6=input("Enter to check there's only digit ")
result4=name6.isdigit()
print(result4)

#check whether there're only String characters ??

name7=input("Enter to check whether there's only letters ")
result5=name7.isalpha()
print(result5)

#check whether there're letters and integers only  ??

name8=input("Enter to check whether there are only both string and integers values ")
result6=name8.isalnum()
print(result6)



# count how many times a selected character is repeated in the word

name9=input("Enter to check how many times ' a ' is repeated ")
result7=name9.count("a")
print(result7)


#replace
name10=input("Enter a word . all the 'a' will replace to '#' ")
result8=name10.replace("a","#")
print(result8)




#exercise

#validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a Username : ")

#1
if len(username)>12:
    print("You have exceeded the character limit !!! ")
elif not username.find(" ") == -1:
    print("Username can't contain Spaces !!! ")
elif not username.isalpha():
    print("Username can't contain numbers !!! ")
else:
    print(f"Welcome {username} ")


