# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('Enter letter a-z: ')
    print(f'The User entered {letter}')
    vowels= 'aeiouyAEIOUY'
    if len(letter) != 1 or not letter.isalpha():
        print(f'{letter} is not a letter a-z.')
    elif letter in vowels:
        print(f"The letter {letter} is a vowel.")
    elif letter not in vowels:
        print(f'The letter {letter} is a consontant')

# Call the function
check_letter()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    age = int(input("Input a dog's age: "))
    dog_years = 0
    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = ((age - 2) * 7) + 20
    print(f'The dogs age in dog years is {dog_years}')
# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    temperature = input('Is it Cold? yes/no: ')
    raining = input('Is is raining? yes/no: ')

    if temperature == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif temperature == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif temperature == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif temperature == 'no' and not raining == 'yes':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter yes/no.")
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input('Enter the month (Jan-Dec): ').capitalize()
    day = int(input('Enter the day of the (1-31): '))

    winter = ('Jan', 'Feb', 'Mar')
    spring = ('Apr', 'May', 'Jun')
    summer = ('Jul', 'Aug', 'Sep') 
    fall = ('Oct', 'Nov', 'Dec')

    if (month == 'Dec' and day >= 21) or (month in winter and not (month == 'Mar' and day > 19)):
        season = 'Winter'
    elif (month == 'Mar' and day >= 20) or (month in spring and not (month == 'Jun' and day > 20)):
        season = 'Spring'
    elif (month == 'Jun' and day >= 21) or (month in summer and not (month == 'Sep' and day > 21)):
        season = 'Summer'
    elif (month == 'Sep' and day >= 22) or (month in fall and not (month == 'Dec' and day > 20)):
        season = 'Fall'
    else:
        season = 'Invalid date'

    print(f"{month} {day} is in {season}.")

determine_season()

