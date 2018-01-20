'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2 
#20
35 / 5
#7.0

35 / 4
#8.75
35 // 4 
#8
# What is the difference between the / operator and the // operator?
# Ignores the number in the decimals place.

2 ** 5 
#32
# What does the ** operator do?
# it is the same as saying to the power of. So 2 to the power of 5.
5 % 3 
#3
5 % 2
#1
5 % 4
#1
# What does the % operator do?
# Takes the remainder of the number divided. So the remainder of 5 divided by 2 would be 1.

(1 + 3) * 2
#
# What effect do the parenthesis have on this statement?
# Order of Operations. The operation in the parenthesis are computed first.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>
type(3.0)
# <class 'float'>
type("word")
# <class 'str'>
type(True)
# <class 'bool'>
type(False)
# <class 'bool'>
type(None)
# <class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
# 3
float(7)
# 7.0
str(55)
# '55'
bool(1)
# True
# '''How can you tell the difference between these four different types?
''' int only shows the integer of the number ignoring the decimal.
 float includes the decimal of the number.
 str represents the string or the word within the parenthesis.
bool represents a true of false statement.'''

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# 'helloworld!' it combines the two words together

"This is a string"[0]
# 'T'
"This is a string"[5]
# 'i'
"This is a string"[8]
# 'a'
# What is happening as you change the number?
# it identified the letter in that position of the string starting with the first letter as [0].

"This is a string"[-1]
# 'g'
# What happens when you use a negative number?
# same thing but backwards with the 'g' now being the first letter but at [-1] instead of

"%s can be %s" % ("strings", "interpolated")
# What is happening here? 
# 'strings can interpolated' unsure of what this exactly means however.

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
# 'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
# Bob wants to eat lasagna

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# 'Hello, Jacob Dubey'
# What just happened?
# It took my response to the input and made it n.

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# It is generating random numbers <1.

randint(1,100)
# How is this different?
# It is generating whole numbers between 1 and 100.

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# It took the numbers within the list and rearranged them in a new order.

print(sample(items, 1))
# What does this do?
# Pulls a single random number from the list.

print(sample(items, 5))
# What does the second parameter control?
# Controls how many random numbers will be pulled from the list.

for i in range(0,5):
	print(i)
'''0
1
2
3
4'''
# What is happening here? What happens if you change the two range parameters?
'''It lists the numbers vertically.
the first parameter indicates where to start. The second parameter indicated where to stop.'''