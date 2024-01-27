# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
slice = "Hello World"
print(slice[2:5])

# Slicing from the start
# By leaving out the start index, the range will start at the first character
sliceFromTheStart = "Hello World"
print(sliceFromTheStart[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end

sliceToTheEnd = "Hello World"
print(sliceToTheEnd[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
sliceNegative = "Hello World"
print(sliceNegative[-5:-2])

# Replace String
# The replace() method replaces a string with another

a = "Hello, World!"
print(a.replace("Hello", "Goodbye"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(","))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + " " + b
print(c)

