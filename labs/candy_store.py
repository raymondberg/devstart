######
# We're going to the candy store. How do we figure out how much things cost with tax?
#
#  To build this on your own, head over to http://repl.it and choose Python 3.
#     Paste the code in the window on the left and hit 'Run'
######

# First, lets save the tax rate somewhere we can use it later.
SALES_TAX = .0625

# First we start with an empty store (we'll use something called a dictionary)
store = {}

store['chocolate_bar'] = 1.27
store['tootsie_roll'] = 0.05
store['ice_cream_bar'] = 2.50
store['licorice'] = 1.50

## Cool, so the store keeps the value of the items.
print(store['tootsie_roll'])

# Then you can calculate the tax for an item
item_tax = store['chocolate_bar'] * SALES_TAX

# Let's print the base cost by itself
print('The base cost is', store['chocolate_bar'])

# Let's print the value just by itself
print('The tax is ', item_tax)

# Now add the value when you print (be sure to add the tax)
print('Total cost with tax = ', store['chocolate_bar'] + item_tax)

# What if we just want the dollars and cents?
print('Total cost with tax = ', format(store['chocolate_bar'] + item_tax , '.2f'))


## This is really cool, but I want to know all the taxes. Maybe we can make a FUNCTION?
def calculate_tax(cost_of_an_item):
    item_tax = cost_of_an_item * SALES_TAX
    total_cost = cost_of_an_item + item_tax
    return total_cost

my_total = calculate_tax(store['chocolate_bar'])
my_total = my_total + calculate_tax(store['tootsie_roll'])
my_total = my_total + calculate_tax(store['ice_cream_bar'])
my_total = my_total + calculate_tax(store['licorice'])

print('My trip to the store costs ', my_total)
