### Problem 1: <------------------
# Ask a user for the year they were born by calculating their age.
# Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
# userInput = int(input("Enter the year you were born "))
#
# print(f'You are {userInput} years old')


### Problem 2:
# Ask the user for a string.
# If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”.
# Otherwise print “Hello Student”
# userInput2 = input("Enter your name ")
# if userInput2 == 'Kenn':
#     print("Hello Teacher")
# elif userInput2 == 'Kevin':
#     print("Hello Teacher")
# elif userInput2 == 'Erin':
#     print("Hello Teacher")
# elif userInput2 == 'Autumn':
#     print("Hello Teacher")
# else:
#     print("Hello Student")

### Problem 3: <-------------------
# Ask the user for a negative number.
# Print from 7 down to the user's negative number.
# You must include the user's number.
# userInput3 = int(input("Enter a negative number: "))
# for x in userInput3:
#
# print(x)


### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not between
# the two numbers ask them to do it again until they get it right.
# # Afterward they print the correct number, print "Good job"
# userInput4 = int(input("Enter a number between -10 to -5 "))
# while userInput4 != -10:
#     if (userInput4 < -10):
#         userInput4 = int(input('try again '))
#     elif (userInput4 > -5):
#         userInput4 = int(input('try again '))
# print("Good Job")

### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"].
# Print the list in reverse without using a list method.
squad = ["One", "Two", "Three", "Four", "Five"]

# for y in squad:
#
#     assert isinstance(y, object)
#     print(y)

### Problem 6:
# Create a function that will have the string firstName as a parameter.
# In the function ask the user for their last name.
# Print "Hello [FIRST & LAST NAME]" in the function. Call that function
# def problem6():
#     userInput6 = input("Enter your last name ")
#     firstName = userInput6
#     print(f'Hello {firstName}')
#
# problem6()


### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes.
# Create a class method that will change the rating of the book.
# Outside of the class, create three objects of the class Book and put them in an array.
# Lastly, USING THE ARRAY print only the names of the
# books using any method we’ve learned in class.
class Books:
    def __init__(self, name, rating, genre, author):
        self.name = name
        self.rating = rating
        self.genre = genre
        self.author = author
    def change_rating(self, newRating):
        self.rating = newRating
    def printBook(self):
        return f'{self.name}'

newBook1 = Books("something", "5", "scary", "person")
newBook2 = Books("stuff here", "5", "scary", "person")
newBook3 = Books("other stuff", "5", "scary", "person")
# print(newBook1.printBook(), newBook2.printBook(), newBook3.printBook())







# ### Problem 8: <-------------------
# Create a function that asks the user to enter a number.
# If the number is between and include -50 and 5, return "Funds too low".
# If the number is between 5 and 50, return “You should add more funds.”
# If the number is more than 50, return “Just enough.”
# def problem8():
#     userInput = int(input("Enter a number "))
#     if userInput <= 5:
#         print("Funds too low")
#     elif userInput > 5:
#         print("You should add more funds.")
#     elif userInput > 50:
#         print("Just enough")
#
# problem8()







# ### Problem 9:
# Ask the user for a positive number.
# Create an empty array and starting from zero, add each number by 1 into the array.
# Print EACH ELEMENT of the array.
userInput9 = int(input("Enter a positive number "))

emptyArr = []

# ### Problem 10:
# Create a new empty array called pet_list.
# Create a Pet class with a type and breed attribute/property.
# Include a method that will print each attribute/property.
# Add 3 pet objects to the pet_list array.
# Print the attributes/properties for each pet.
class Pet:
    def __init__(self, breed, attribute, property):
        self.breed = breed
        self.attribute = attribute
        self.property = property
    def print_pet(self):
        return f'{self.breed} {self.attribute} {self.property}'

pet_list = []
newPet1 = Pet("dog1", "animal", "land")
newPet2 = Pet("dog2", "beast", "yard")
newPet3 = Pet("dog3", "creature", "house")
print(newPet1)
newPet1.print_pet()