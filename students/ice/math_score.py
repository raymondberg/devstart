import random

correct = 0
total = 0

while True:
    number1 = int(random.randint(1,20))
    number2 = int(random.randint(1,20))
    ops1 = ['+', '-', '*', '/']
    ops = random.choice(ops1)

    user_answer = input("What is %d %s %d? " % (number1, ops, number2))

    if ops == '+':
        temp = number1 + number2
    elif ops == '-':
        temp = number1 - number2
    elif ops == '/':
        temp = number1 / number2
    else:
        temp = number1 * number2

    if float(user_answer) == temp:
        print("Correct!")
        correct = correct + 1
    else:
        print("Ooops! The correct answer was %d" % ( temp))

    total = total + 1

    print("You have %d right out of %d" % (correct, total))
    print("")

    if total > 9:
        score = 100 * (correct / total)
        word = 'a'
        if score > 89:
            grade = "A"
            word = 'an'
        elif score > 79:
            grade = "B"
        elif score > 69:
            grade = "C"
        elif score > 59:
            grade = "D"
        else:
            grade = "F"
            word = 'an'

        print("Game Over")
        print("your score is %d%%" % (score))
        print("you got %s %s" % (word, grade))
        break
