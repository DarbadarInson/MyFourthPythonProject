#If, else ...
print("Welcome to hte rollercoaster")
height = int(input("What is your height in cm "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

"""
  > --- greater tham
  < --- less than
  >= --- greater than or equel to
  <= --- less than or equel to
  == --- equel to
"""

number = int(input("Raqam kiriting: "))

if number % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

#Nested if/else
"""
if condition:
    if another condition:
        do this
    else:
        do this
else:
do this
"""


height1 = int(input("What is your height in cm "))
if height1 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#BMI Function

height2 = float(input("enter your height in m: "))
weight2 = float(input("enter your weight in kg: "))

bmi = round(weight2 / height2 ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight!")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight!")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you have a overweight!")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you have a obese!")
else:
    print(f"Your bmi is {bmi}, you have a clinically obese!")
#Leap Year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else: 
        print("Leap year.")
else:
    print("Not leap year")
#if / elif / else

"""
if condition1:
    do A
elif condition2:
    do B
else:
    do C
"""

#Multiple if
"""
if condition1
    do A
if condition2
    do B
if condition3
    do C
"""




height1 = int(input("What is your height in cm "))
bill = 0
if height1 >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y/y or N/n. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
    

else:
    print("Sorry, you have to grow taller before you can ride.")
#Pizza order Practice

print("Welcome to Python Pizza Deliveries! :)")
size = input("What size pizza do you want? \n Small - S/s \n Medium - M/m \n Large - L/l")



print("Welcome to Python Pizza Deliveries! :)")
size = input("What size pizza do you want? \n Small - S/s \n Medium - M/m \n Large - L/l \n")
add_pepperoni = input("Do you want peperoni? Y/N - y/n ")
extra_cheese = input("Do you want extra cheese? Y/N - y/n ")

Pbill = 0
if size == "S" or size == "s":
    Pbill += 15
elif size == "M" or size == "m":
    Pbill += 20
else:
    Pbill += 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
      Pbill += 2
    else:
      Pbill += 3
if extra_cheese == "Y" or extra_cheese == "y":
    Pbill += 1

print(f"Your final bill is: ${Pbill}")

#Logical Operators
"""
if condition:
    do this
else:
    do this
"""

"""
This is Logical Operators:
A and B
C or D
not E
"""


#Love Calculator
print("Welcome to the Love Calculator! :)")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"You score is {love_score}")


















































