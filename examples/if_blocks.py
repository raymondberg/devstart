## This Script shows how programs can be controlled by using control blocks.
##  This is how scripts make decisions or change based on what's happening.
##  A lot of people also call this "LOGIC", because it's how machines think


#####################
# In Python, scripts are evaluated in order from top to bottom. The events from earlier
#   steps impacts later ones.

number = 1              #Step one: Assign the value 1 to a variable named 'number'
number = number + 1     #Step two: Take the value of number (1) and add it to 1 and assign this value(2) to number
print(number)           #Step three: Print the value of number(2) to the screen
number = number + 1     #Step four: Take the value of number (2) and add it to 1 and assign this value(3) to number
print(number)           #Step five: Print the value of number(3) to the screen
print("done!")          #Step six: Print done!

### Notice that number is changing as the script continues.
###  Number is different after Step five than it was after Step one
###  Because the script is self-contained (i.e. it has everything it needs to run in the script),
###  we know it will always execute the same way. Very boring. It will always print 2 then 3.


#####################
# We can add uncertainty by asking the user to provide us information as the program runs.
#  the input command in Python 3 (raw_input in Python 2) lets us ask for a string from the user.

name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
print("Hello, " + name + ". I am glad you are using my program.") #Step two: Print message to user
number = 1                              #Step three: Assign the value 1 to a variable named 'number'
number = number + 1                     #Step four: Take the value of number (1) and add it to 1 and assign this value(2) to number
number = number + 1                     #Step five: Take the value of number (2) and add it to 1 and assign this value(3) to number
print("done!")                          #Step six: Print done!

## Example: if the user types in `Jim` the program would print out:
##  Hello, Jim. I am glad you are using my program."
## The program would continue doing the number math after that


#####################
## But suppose we ONLY wanted to say hi if the person was named Jim? We can do that with an `if` block.
##  This will create a PATH in the code that only gets run if the user entered Jim.

name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Jim':                       #Step two: Check if the user's name is Jim. If so, run what is inside it.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
number = 1                              #Step three: Assign the value 1 to a variable named 'number'
number = number + 1                     #Step four: Take the value of number (1) and add it to 1 and assign this value(2) to number
number = number + 1                     #Step five: Take the value of number (2) and add it to 1 and assign this value(3) to number
print("done!")                          #Step six: Print done!

## Example: if the user types in `Jim` they will see the message
## Example: if the user types in `Judy` they will not see the message.


#####################
# We can even make it so that Jim is the only one who can work with Number

name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Jim':                       #Step two: Check if the user's name is Jim. If so, run what is inside it.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
    number = 1                              #Step two.B: Assign the value 1 to a variable named 'number'
    number = number + 1                     #Step two.C: Take the value of number (1) and add it to 1 and assign this value(2) to number
    number = number + 1                     #Step two.D: Take the value of number (2) and add it to 1 and assign this value(3) to number
print("done!")                          #Step three: Print done!

## Example: if the user types in `Jim` they will see the message and math happens before "done!" is printed
## Example: if the user types in `Judy` no message, no math, only "done!" is printed.


#####################
# What if we imagine Judy has math too, but she's in more advanced class. We want Jim to have some math, and Judy to do other math.
#   We can make this happen with an `elif` block (else if)

name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Jim':                       #Step two: Check if the user's name is Jim. If so, run what is inside it.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
    number = 1                              #Step two.B: Assign the value 1 to a variable named 'number'
    number = number + 1                     #Step two.C: Take the value of number (1) and add it to 1 and assign this value(2) to number
    number = number + 1                     #Step two.D: Take the value of number (2) and add it to 1 and assign this value(3) to number
elif name == 'Judy':                 #Step two': If step two came up false, check if users name is Judy. If so, run what's inside it
    number = 100                            #Step two'.A: Assign the value 100 to a variable named 'number'
    number = number / 25                    #Step two'.B: Take the value of number (100) and divide it by 25 and assign this value(4) to number
    number = number * 4                     #Step two'.C: Take the value of number (4) and multiply it by 4 and assign this value(16) to number
print("done!")                          #Step three: Print done!


####################
# That's cool, but what if we want to keep that cool message for Jim and Judy (but not for anyone else)?
#  We can nest (like russian nesting dolls) if blocks inside others. See the following example:
name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Judy' or name == 'Jim':     #Step two: Check if user's name is Judy or Jim.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
    if name == 'Jim':                       #Step two.B: Check if the user's name is Jim. If so, run what is inside it.
        number = 1                              #Step two.B.A: Assign the value 1 to a variable named 'number'
        number = number + 1                     #Step two.B.B: Take the value of number (1) and add it to 1 and assign this value(2) to number
        number = number + 1                     #Step two.B.C: Take the value of number (2) and add it to 1 and assign this value(3) to number
    elif name == 'Judy':                 #Step two.B': If step two.B came up false, check if users name is Judy. If so, run what's inside it
        number = 100                            #Step two.B'.A: Assign the value 100 to a variable named 'number'
        number = number / 25                    #Step two.B'.B: Take the value of number (100) and divide it by 25 and assign this value(4) to number
        number = number * 4                     #Step two.B'.C: Take the value of number (4) and multiply it by 4 and assign this value(16) to number
print("done!")                          #Step three: Print done!


###################
# One last step, we'd like to print a message to all those non-Jims and non-Judys to stop using the script
#  How do we tell everyone ELSE? We do it with an `else` block.
name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Judy' or name == 'Jim':     #Step two: Check if user's name is Judy or Jim.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
    if name == 'Jim':                       #Step two.B: Check if the user's name is Jim. If so, run what is inside it.
        number = 1                              #Step two.B.A: Assign the value 1 to a variable named 'number'
        number = number + 1                     #Step two.B.B: Take the value of number (1) and add it to 1 and assign this value(2) to number
        number = number + 1                     #Step two.B.C: Take the value of number (2) and add it to 1 and assign this value(3) to number
    elif name == 'Judy':                 #Step two.B': If step two.B came up false, check if users name is Judy. If so, run what's inside it
        number = 100                            #Step two.B'.A: Assign the value 100 to a variable named 'number'
        number = number / 25                    #Step two.B'.B: Take the value of number (100) and divide it by 25 and assign this value(4) to number
        number = number * 4                     #Step two.B'.C: Take the value of number (4) and multiply it by 4 and assign this value(16) to number
else:                                   #Step two': If step two didn't match, run what's inside
    print("Wait, " + name + "? I don't know that name. You probably shouldn't use my program.") #Step two'.A
print("done!")                          #Step three: Print done!


###################
# Notice how the lines match up. The else matches the FIRST if, not the others.
#   We could add in another else for that set of if/else if/else blocks...but why?
name = input("What is your name? ")     #Step one: Print question and save user input in variable named 'name'
if name == 'Judy' or name == 'Jim':     #Step two: Check if user's name is Judy or Jim.
    print("Hello, " + name + ". I am glad you are using my program.") #Step two.A: Print message to user
    if name == 'Jim':                       #Step two.B: Check if the user's name is Jim. If so, run what is inside it.
        number = 1                              #Step two.B.A: Assign the value 1 to a variable named 'number'
        number = number + 1                     #Step two.B.B: Take the value of number (1) and add it to 1 and assign this value(2) to number
        number = number + 1                     #Step two.B.C: Take the value of number (2) and add it to 1 and assign this value(3) to number
    elif name == 'Judy':                  #Step two.B': If step two.B came up false, check if users name is Judy. If so, run what's inside it
        number = 100                            #Step two.B'.A: Assign the value 100 to a variable named 'number'
        number = number / 25                    #Step two.B'.B: Take the value of number (100) and divide it by 25 and assign this value(4) to number
        number = number * 4                     #Step two.B'.C: Take the value of number (4) and multiply it by 4 and assign this value(16) to number
    else:                                   #Step two.B'': If two.B and two.B' failed (which is impossible), run what's inside. 
        print("Wait...this will never get run. How can your name be Judy or Jim and then NOT be Judy or Jim?? Impossible!") # Step two.B''.A
else:                                   #Step two': If step two didn't match, run what's inside
    print("Wait, " + name + "? I don't know that name. You probably shouldn't use my program.") #Step two'.A
print("done!")                          #Step three: Print done!



