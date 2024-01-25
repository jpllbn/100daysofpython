# String Format
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 20
item_no = 2345
price = 99.9
my_order = "I want {} pieces of {} for {} dollars"
print(my_order.format(quantity, item_no, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 20
item_no = 2345
price = 99.9
my_order = "I want {2} pieces of {1} for {0} dollars"
print(my_order.format(quantity, item_no, price))


