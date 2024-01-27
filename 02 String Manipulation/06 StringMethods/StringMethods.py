# String Methods
# Python has a set of built-in methods that you can use on strings.
#
# Note: All string methods return new values. They do not change the original string.

# capitalize() Converts the first character to upper case

a = "john paul labanon"
print(f"capitalize() - {a.capitalize()}")

# casefold() Converts string into lower case
print(f"casefold() - {a.casefold()}")

# center() Returns a centered string
print(f"center() - {a.center(50)}")

# count() Returns the number of times a specified value occurs in a string
b = "How many apples do you I have?, You like apple too?"
print(f"count() - {b.count("apple")}")


