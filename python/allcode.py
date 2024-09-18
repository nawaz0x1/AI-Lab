print('Hello World')
print('*' * 20)
# Define boolean variables
is_rainy = True
is_sunny = False

# If statement to check if it's rainy
if is_rainy:
    print("Carry an umbrella")
# Else if statement to check if it's sunny
elif is_sunny:
    print("No need to carry an umbrella")
# Else statement if neither condition is true
else:
    print("Please check the weather")
good_condition = True
reasonable_price = True

if good_condition and reasonable_price:
    print("We will buy the house")

# Using OR operator
good_condition = True
reasonable_price = False

if good_condition or reasonable_price:
    print("We are interested")

# Using NOT operator
good_condition = True
poor_foundation = False

if good_condition and not poor_foundation:
    print("It is a good deal")
# Setting price to 10
price = 10

# Comparing price with 10
if price == 10:
    print("We will buy it")

# Changing price to 11 and comparing
price = 11
if price != 10:
    print("The price is not 10")

# Changing price to 9 and comparing
price = 9
if price < 10:
    print("It is cheap")

# Comparing price with 10 using greater than
price = 11
if price > 10:
    print("It is expensive")

# Using greater than or equal to
price = 10
if price >= 10:
    print("Price is greater than or equal to 10")

# Using less than or equal to
price = 9
if price <= 10:
    print("Price is less than or equal to 10")
i = 0
while i < 5:
    print(i)
    i += 1
print("While loop ended")
# Guessing Game using While Loop

# Set the actual price of the product
actual_price = 10

# Initialize guess_count and guess_limit
guess_count = 0
guess_limit = 5

# Start the while loop
while guess_count < guess_limit:
    # Get user input and convert it to an integer
    guess = int(input("Guess the price: "))
    
    # Check if the guess is correct
    if guess == actual_price:
        print("You won!")
        break
    
    # Increment the guess count
    guess_count += 1

# After the while loop
else:
    print("You failed")
# Example 1: Iterating over a string
string = "python"
for character in string:
    print(character)

# Example 2: Iterating over a list of items
grocery_list = ["egg", "rice", "oil"]
for item in grocery_list:
    print(item)

# Example 3: Iterating over a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Example 4: Using the range function
for number in range(10):
    print(number)

# Example 5: Using range with a starting point and step
for number in range(5, 10, 2):
    print(number)

# Example 6: Calculating the total bill
bills = [10, 30, 50, 10]
total = 0
for bill in bills:
    total += bill
print(f"Total bill: ${total}")
for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")
# Define a list of grocery items
grocery_list = ['egg', 'rice', 'bread', 'sugar']
print(grocery_list)

# Access elements using index
print(grocery_list[0])  # egg
print(grocery_list[1])  # rice
print(grocery_list[-1]) # sugar
print(grocery_list[-2]) # bread

# Slice the list
print(grocery_list[2:])   # ['bread', 'sugar']
print(grocery_list[:2])   # ['egg', 'rice']
print(grocery_list[1:2])  # ['rice']

# Modify an item in the list
grocery_list[1] = 'oil'
print(grocery_list)      # ['egg', 'oil', 'bread', 'sugar']

# Working with numeric lists
price = [10, 5, 8, 15, 3]
max_price = price[0]

for value in price:
    if value > max_price:
        max_price = value

print(max_price)         # 15
# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the 2D list
print(matrix)

# Accessing elements
print(matrix[0])  # First row
print(matrix[1])  # Second row
print(matrix[2])  # Third row
print(matrix[0][2])  # Element at row 0, column 2
print(matrix[1][1])  # Element at row 1, column 1

# Modifying a value
matrix[0][2] = 15
print(matrix)

# Using nested for loops to print each item
for row in matrix:
    for item in row:
        print(item)
# Creating a list
number_list = [1, 2, 5, 1, 10, 14]
print(number_list)

# Appending an element
number_list.append(20)
print(number_list)

# Inserting an element at a specific index
number_list.insert(1, 7)
print(number_list)

# Removing a specific element
number_list.remove(2)
print(number_list)

# Sorting the list
number_list.sort()
print(number_list)

# Reversing the list
number_list.reverse()
print(number_list)

# Checking if an element is in the list
print(1 in number_list)
print(12 in number_list)

# Counting occurrences of an element
print(number_list.count(1))

# Finding the index of an element
print(number_list.index(10))

# Copying the list
number_list2 = number_list.copy()
print(number_list)
print(number_list2)

# Popping the last element
number_list.pop()
print(number_list)

# Clearing the list
number_list.clear()
print(number_list)
age = 30
age = 20
name = "Shah Nawaz Haider"
good_programmer = True

print(f"{name} age of {age} is a {'Good Programmer' if good_programmer else 'Bad Programmer'}")
number_list = [1, 2, 1, 5, 6, 10]
unique = []

for number in number_list:
    if number not in unique:
        unique.append(number)

print(unique)
# Define a tuple
number_tuple = (1, 2, 3)

# Print the tuple
print(number_tuple)

# Print the element at index 1
print(number_tuple[1])

# Attempt to insert an element at index 1 (this will raise a TypeError)
# number_tuple[1] = 10  # Uncommenting this line will cause an error

# Count occurrences of an item in the tuple
print(number_tuple.count(2))

# Find the index of the first occurrence of an item
print(number_tuple.index(2))

# Define a tuple
number_tuple = (1, 2, 3)

# Traditional approach
add_number_tuple = number_tuple[0] + number_tuple[1] + number_tuple[2]
print(add_number_tuple)

# Assigning to variables
x, y, z = number_tuple
print(x + y + z)

# Python unpacking
a, b, c = number_tuple
print(a + b + c)

# Using a list
number_list = [1, 2, 3]
a, b, c = number_list
print(a + b + c)
# Using tuple
number_tuple = (1, 2, 3)
a, b, c = number_tuple
print(a + b + c)

# Using list
number_list = [1, 2, 3]
a, b, c = number_list
print(a + b + c)
# Creating a dictionary
user = {
    "name": "my name",
    "age": 28,
    "email": "myemail@gmail.com",
    "is_verified": True
}

# Printing the dictionary
print(user)

# Accessing values using keys
print(user["name"])  # Outputs: my name
print(user["age"])   # Outputs: 28

# Accessing a non-existent key
print(user.get("password"))  # Outputs: None

# Accessing a key with get method
print(user.get("age"))  # Outputs: 28

# Modifying existing values
user["age"] = 29
print(user["age"])  # Outputs: 29

# Adding a new key-value pair
user["job"] = "teaching"
print(user)  # Outputs: Dictionary with the new key-value pair added
# Create the emoji dictionary
emoji_dict = {
    ':)': 'ðŸ˜Š',
    ':(': 'ðŸ˜¢'
}

# Take input from the user
message = input("Type your message: ")

# Split the message into words
separated_words = message.split()

# Initialize an empty output string
output = ""

# Convert words to emojis using the dictionary
for word in separated_words:
    output += emoji_dict.get(word, word) + " "

# Print the output
print(output)
# Define a function to calculate the total cost
def total_cost(price, shipping, discount):
    total = price + shipping - discount
    print(f"Total cost: {total}")

# Call the function with different arguments
total_cost(10, 5, 1)   # Output: Total cost: 14
total_cost(20, 5, 5)   # Output: Total cost: 20
total_cost(40, 10, 1)  # Output: Total cost: 49

# Define a function with keyword arguments
def welcome(name):
    print(f"Hi {name}")

# Call the function with positional arguments
welcome("Nurgeomon Varikey")  # Output: Hi Nurgeomon Varikey

# Define a function to handle first and last names
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")

# Call the function with positional arguments
greet("Nurgeomon", "Faraki")  # Output: Hi Nurgeomon Faraki
def add(number_1, number_2):
    return number_1 + number_2

result = add(1, 2)
print(result)
def emoji_converted(message):
    separated_words = message.split()
    emoji = {
        "happy": "ðŸ˜Š",
        "sad": "ðŸ˜¢"
    }
    output = ""
    for word in separated_words:
        output += emoji.get(word, word) + " "
    return output

message = input("Type your message: ")
result = emoji_converted(message)
print(result)
# Celsius to Fahrenheit Converter with Exception Handling

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Try-Except block to handle exceptions
try:
    # Input from user
    celsius = int(input("Enter temperature in Celsius: "))
    
    # Check for zero division error
    if celsius == 0:
        raise ZeroDivisionError("Celsius cannot be zero")

    # Conversion and output
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")

except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as e:
    print(e)
name = input("What's your name: ")
address = input("Your address: ")

print(f"{name} lives in {address}")
class Keyboard:
    def definition(self):
        print("Keyboard is an input device")
    
    def number_of_keys(self):
        print("There are 101 keys")

# Creating an object of the class
my_keyboard = Keyboard()

# Calling methods on the object
my_keyboard.definition()       # Output: Keyboard is an input device
my_keyboard.number_of_keys()   # Output: There are 101 keys

# Setting and printing an attribute
my_keyboard.brand = "Logitech"
print(my_keyboard.brand)       # Output: Logitech

# Creating another object of the class
new_keyboard = Keyboard()
new_keyboard.definition()      # Output: Keyboard is an input device

# Attempting to print a non-existent attribute
# print(new_keyboard.brand)    # Raises an AttributeError

# Setting an attribute for the new object
new_keyboard.brand = "Dell"
print(new_keyboard.brand)      # Output: Dell
# Keyboard class with constructor
class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

# Creating a keyboard object
my_keyboard = Keyboard("English", "Wireless")
print(my_keyboard.language)  # Output: English
print(my_keyboard.connection)  # Output: Wireless

# AboutMe class with constructor
class AboutMe:
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    def talk(self):
        print(f"My name is {self.name}. I'm from {self.address}.")
        print(f"I am a {self.occupation}.")

# Creating an object of AboutMe class
fairuki = AboutMe("Nirjaman Faruki", "Bangladesh", "Teacher")
fairuki.talk()
# Output:
# My name is Nirjaman Faruki. I'm from Bangladesh.
# I am a Teacher.
# Parent class
class Laptop:
    def parts(self):
        print("Keyboard, Display, Motherboard")

# Adding an additional method to the Desktop class
class Desktop(Laptop):
    def weight(self):
        print("Desktops are heavyweight")

# Create objects and call methods
my_laptop = Laptop()
my_laptop.parts()  # Output: Keyboard, Display, Motherboard

my_desktop = Desktop()
my_desktop.parts()  # Output: Keyboard, Display, Motherboard



# Create object and call the new method
my_desktop = Desktop()
my_desktop.parts()  # Output: Keyboard, Display, Motherboard
my_desktop.weight()  # Output: Desktops are heavyweight
from mypackage import module1, module2

print(module1.greet("Abul"))
print(module2.farewell("Kabul"))
# Import the sys module
import sys

# List all available modules
available_modules = sys.modules.keys()

# Display the first 10 modules for demonstration
print("Available Modules:")
for module in list(available_modules)[:10]:
    print(module)
import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")


for i in range(1, 36):
    # Create a new directory
    new_dir = f'lesson-{str(i)}'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"Directory '{new_dir}' created.")
    else:
        print(f"Directory '{new_dir}' already exists.")

# List all files and directories in the current directory
print("Contents of Current Directory:")
for item in os.listdir(current_dir):
    print(item)
celsius = input("Temperature in Celsius: ")
fahrenheit = int(celsius) * (9/ 5) + 32
print(f"Fahrenheit: {fahrenheit}")
random_string = "This is a random sentance what doesn't make any sense"

print(random_string[10:17])
print(random_string[17:26])
person_a = "Abul"
person_b = "Kabul"

print(f"{person_a} and {person_b} are good friends.")
course_name = "Introduction to AI"
print(len(course_name))
print(course_name.upper())
print(course_name.lower())
print(course_name.find("AI"))
print(course_name.replace("AI", "Python"))
print("Introduction" in course_name)
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 / 2)
print(5 % 2)
print(5 ** 2)

a = 1
b = 2
w = 3
y = a * w + b
print(y)
import math

print(math.ceil(5.7))
print(math.floor(5.7))
print(math.factorial(5))
print(round(5.7))
print(abs(-5.7))
