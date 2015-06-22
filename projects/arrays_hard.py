#Here's your first line of code
items = []


# Project Description (part 1):
#   Add a 4th command: laserblast
#   laserblast can remove a single item from anywhere in the list, regardless of its position
#   When a user specifies a laserblast they should also type in the item they want to remove
#   When a user enters another command tell them that you don't understand the command and ask again for command

### Clue (part 1): What happens when you type `"first second".split(" ")` in the Python Console?

### Expected Output (part 1):
# Greetings! I have made a list for you.
# This is what your list looks like: []
# What should I do? (user enters stack 3)
# This is what your list looks like: ["3"]
# What should I do? (user enters stack banana)
# This is what your list looks like: ["3","banana"]
# What should I do? (user enters stack lake)
# This is what your list looks like: ["3","banana","lake"]
# What should I do? (user enters unstack)
# This is what your list looks like: ["3","banana"]
# What should I do? (user enters quit)
# Have a nice day!

############### END PROJECT 1




############### BEGIN PROJECT 2
# Project Description (part 2):

# Add a 4th command: laserblast
# laserblast can remove a single item from anywhere in the list, regardless of its position
# When a user specifies a laserblast they should also type in the item they want to remove
# When a user enters another command tell them that you don't understand the command and ask again for command

### Check out the different ways you can use `[1,2,3,4].pop()` https://docs.python.org/2/tutorial/datastructures.html#more-on-lists

### Expected output (part 2):
# Greetings! I have made a list for you.
# This is what your list looks like: []
# What should I do? (user enters stack 3)
# This is what your list looks like: ["3"]
# What should I do? (user enters unstork)
# ERROR: I don't know what `unstork` means
# What should I do? (user enters stack banana)
# This is what your list looks like: ["3","banana"]
# What should I do? (user enters stack lake)
# This is what your list looks like: ["3","banana","lake"]
# What should I do? (user enters laserblast banana)
# This is what your list looks like: ["3","lake"]
# What should I do? (user enters quit)
# Have a nice day!

