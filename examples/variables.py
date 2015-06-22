## This Script Shows how Variables can be used, very simply.
## Just a reminder that anything after a '#' is a comment and is not part of the
## code logic. Comments are just for humans to read as they try to understand the
## computer code. Here's a great article on good comments: http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/

#####################
#Without variables, repetitive tasks with values are painful and limited
print(7+7)      # Prints 14
print(7+7+2)    # Prints 16
print(7+7+7+7)  # Prints 28
print("My number is " + str(7+7))   #Prints `My number is 14`

#####################
#Variables let you save values for use later
my_number = 7+7
print(my_number)    # Prints 14
print(my_number+2)  # Prints 16
print(my_number*2)  # Prints 28
print("My number is " + str(my_number))   #Prints `My number is 14`

#but notice how the variable hasn't been changed in these examples
print(my_number)    # Prints 7

#####################
#Variables can be changed if you reassign them with a new value
her_number = 12
print(her_number)   #Prints 12

her_number = 14
print(her_number)   #Prints 14

her_number = her_number + 4
print(her_number)   #Prints 18

her_number = her_number / 2
print(her_number)   #Prints 9


#####################
#Variables can be used together or alone, they are just places to save values
his_number = 3
her_number = 2
print(his_number + her_number)  # Prints 5
print(her_number)               # Prints 2

his_number = her_number - 1
print(his_number)               #prints 1

####################
### Variables can contain any kind of data that the language supports
### and in Python you can change the type of the variable at will

thing = 2       # This is an integer (e.g. 0 or 1 or -3 or 100002456)
thing = 4.5     # This is a float (e.g. 1.1 or 1.2 or 19.845 or -0.6124)
thing = True    # This is a boolean (e.g. True or False)
print(thing)    # Prints True

thing = "banana"    #This is a string, it can contain any letters or numbers or spaces
print(thing)        # Prints banana

thing = [1,2,3,4,5] # This is an array, it can contain all kinds of objects, just like variables
print(thing)        # Prints [1,2,3,4,5]
print(thing[0])     # Prints 1
print(thing[2])     # Prints 3

thing = range(1,6)
print(thing)        # Prints [1,2,3,4,5]

thing = { 'name': 'Ray' }   # This is a dict, it contains key:value pairs where you can lookup values by key names
print(thing)                # Prints {'name': 'Ray'}
print(thing['name'])        # Prints Ray
