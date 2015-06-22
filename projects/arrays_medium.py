#Here's your first line of code
dinosaurs = ["T-Rex", "Pterodactyl", "Triceratops", "Barney"]



# Project Description:
#   Ask the users in what year they think the dinosaurs lived (BCE)
#   Then say "If that's true then..." and list off when the dinosaurs lived
#   Each dinosaur should live one year after the previous, starting with the year +1 (or minus 1 because it's BCE!)


### Clue: It's tricky to mix strings and numbers. What happens when you type `str(9)` in the Python Console? What about `"The number %d." % 9` ?

### Expected output:
#In what year do you think the dinosaurs lived? (user enters 60000)
#    If that's true then...
#    T-Rex lived in the year 59999 BCE
#    Pterodactyl lived in the year 59998 BCE
#    Triceratops lived in the year 59997 BCE
#    Barney lived in the year 59996 BCE
