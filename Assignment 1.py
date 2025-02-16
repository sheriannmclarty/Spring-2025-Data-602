from datetime import datetime
print(datetime.today())

# Assignment: Fix Python Errors
# Name: Sheriann McLarty
# Date: " + datetime.today().strftime('%B %Y')}]}

# This script fixes errors in a program that calculates test score averages, checks for high scores,
# computes rectangle areas, and determines a user's age. Updates include correcting mistakes, improving
# accuracy, and making the program easier to use. The date of birth format was changed to MM-DD-YYYY,
# and the script now wishes the user a happy birthday if today is their birthday. The rectangle areas are
# displayed in square centimeters (cm²) for better clarity.

# Q1 Fix all the syntax and logical errors in the given source code
# add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3:'))

# Calculate the average test score.

average = (test1 + test2 + test3) / 3

# Print the average.

print('The average score is', average)

# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')
else:
    print('Your average needs more work!')
# Q2
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width
# of two rectangles and prints to the user the area of both rectangles.

# Get the length and width of the first rectangle
length1 = int(input("Enter the length of the first rectangle: "))
width1 = int(input("Enter the width of the first rectangle: "))

# Get the length and width of the second rectangle
length2 = int(input("Enter the length of the second rectangle: "))
width2 = int(input("Enter the width of the second rectangle: "))

# Calculate the areas
area1 = length1 * width1
area2 = length2 * width2

# Print the areas
print("The area of the first rectangle is:", area1, "cm²")
print("The area of the second rectangle is:", area2, "cm²")

# Q3
# Ask a user to enter their first name and their age and assign it to the variables name and age.
# The variable name should be a string and the variable age should be an int.

# Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Get the user's first name, last name, and date of birth
first_name = input("Enter your first name: ")  # String input
last_name = input("Enter your last name: ")  # String input
dob = input("Enter your date of birth (MM-DD-YYYY): ")  # String input

# Calculate age
birth_date = datetime.strptime(dob, "%m-%d-%Y")
today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Print a birthday message or a general message if it's not their birthday
if birth_date.month == today.month and birth_date.day == today.day:
    print(f"Happy birthday, {first_name} {last_name}! You are {age} years old today!")
else:
    print(f"Hello, {first_name} {last_name}! Have a wonderful day!")

