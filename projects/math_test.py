## THE MATH TEST
#
#Open this file in IDLE and figure out how it works. Can you make it better?

import random

correct = 0
total = 0

while True:
    number1 = int(random.randint(0,20))
    number2 = int(random.randint(0,20))

    user_answer = input("What is %d + %d? " % (number1, number2))

    if int(user_answer) == number1 + number2:
        print("Correct!")
        correct = correct + 1
    else:
        print("Ooops! The correct answer was %d" % ( number1 + number2))

    total = total + 1

    print("You have %d right out of %d" % (correct, total))
    print("")


#Ideas to improve it:
#    Make it stop after 10 questions (right now you have to CTRL-C to kill it, or close the window)
#    Have it put out the percentage correct at the end (hint: %f and 1.0 might come up)
#    Give the student a grade based on percent at the end (9 or 10 is an A, 8 is a B, etc...)
#    Ask more questions than just addition ( subtraction and multiplication are good candidates)
