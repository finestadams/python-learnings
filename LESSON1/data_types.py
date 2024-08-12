
import math

# string data type


#literal assignment
first = 'Dave'
last = 'Grey'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str('Pepertoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation

# fullname = first + " " + last
# print(fullname)
# fullname += '!'
# print(fullname)

#casting a number

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the "  + decade + "s"
print(statement)


# Multiple lines

# multi = '''
# Hey, how are you?

# I was just checking in.
#                             You good?

# '''

# print(multi)

# sentence = 'I\'m  back at work\t Hey!\nWhere\'s this at\\located?'
# print(sentence)


# String Methods

# name = '  My name is didi  '
# print(name)
# print(name.upper())
# print(name.lower())
# print(name)

# print(name.title())
# print(name.replace('didi', 'mimi'))
# print(len(name)) #counts whitespace also
# print(name.strip()) #remove white space
# print(name.lstrip()) #remove white space from the left side
# print(name.rstrip()) #remove whit space from the right side


#menu
title = 'menu'.upper()
print(title.center(20, '=')) #right justify
print('Coffee'.ljust(16, '.') + '$1'.rjust(4)) 
print('Muffin'.ljust(16, '.') + '$2'.rjust(4)) 
print('Cheesecake'.ljust(16, '.') + '$4'.rjust(4)) 

#sting index value 0,1,2...

print(first[1]) 
print(first[-1]) # index of the last letter
print(first[1:-1]) # providing a range
print(first[1:]) 

#some methods returns boolean data

print(first.startswith('D'))
print(first.endswith('Z'))

#Boolean data type

myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool)) 

# Number types

#int number type
box = 5
box = int(5)
print(type(box))
print(isinstance(box, int))

# float

box_amount = 5.3
print(type(box_amount))
print(isinstance(box_amount, float))

# complex type

box_com = 5+3j #j is use to indentify complex value
print(type(box_com))
print(isinstance(box_com, complex))


#built in function for numbers

print(abs(box_com))
print(abs(box_com * -1))

# oythin inbuikt math module

print(math.pi)
print(math.sqrt(64))
print(math.ceil(box_amount))
print(math.floor(box_amount))

#casting a string to a number
