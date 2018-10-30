"""
print("Hello World")

# Apparently I'm going too slow, so I will speed up
# This is a comment
# This has no affect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work

print("Notice what is happening here ")
print()  # This creates a new line
print()  # Do you notice the underline here?
# Hover over top it and see what is wrong

# Watch
print(5+3)
print(5-3)
print(5*3)
print(5/3)
print()

# Semi-advanced math
print("Figure this out...")
print(6//4)
print(12//3)
print(9//4)
print()  # This will ONLY give me a whole number

print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)

# Defining Variables
car_name = "Wiebe mobile"  # string
car_type = "Tesla"  # string
car_cylinders = 16  #
car_mile_per_gallon = 0.01

print("I have a car called %s. It's pretty nice" % car_name)
print("It has %d cylinder, but gets %f mpg" % (car_cylinders, car_mile_per_gallon))

# Taking Input
name = input("What is your name?")
print("Hello %s " % name)

age = input("How old are you?")
print("%s? You belong in a museum!" % age)

# Recasting
real_age = int(input("How old are you again?"))
hidden_age = real_age + 5
print(hidden_age)

print("I saw a %s %s" % (adjective, noun))
"""
# Multi-line Comments

"""
This is a multi-line comment
anything is between them is automatically connected
"""


# Defining Function
def say_it():
    print("Hello World")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
   dist = ((x2-x1) **2 + (y2-y1)**(1/2))
   print(dist)


   distance()