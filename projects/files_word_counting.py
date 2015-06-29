#This script reads in a file called "myfile.txt" which needs to be in the same folder as this script.
#Try to figure out how this script works then try to make this script better.
# I have provided a file, but you could read in any text file. Try using others?

my_file = open("myfile.txt", "r")

all_words = dict()

for line in my_file:
    words = line.split()
    for word in words:
        lower_case_word = word.lower()
        if lower_case_word not in all_words:
            all_words[lower_case_word] = True

print(all_words)


#Some ideas to fix:
## Instead of just saving True as the value...can we keep track of
##      how many times that word has been seen?
## I don't really want to see punctuation as long as it isn't part
##      of a word, so remove any commas, question marks, periods,
##       colons etc... (but don't remove apostraphes in words like don't).
## I don't care too much about common words like "if" or "i" or "to",
##      can you filter them out?
