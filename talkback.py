# REQUIRED: describe the program & what it will do
# I want this program to ask the user for 
# their name "What's your name?" and then, 
# I want the program to say "Hi, NAME" 
# back where NAME is the user's actual name
# Secondly, this program will ask for the user's
# birth year, calculate their approx. age, and then
# say that age back to the user.
# Lastly, this program will divide the user's age
# by 2, and print out that in a message as well

# OPTIONAL: describe each step the program will take
# step 1, ask the user what their name is
print("What is your name?")
# step 2: input the user's name from the keyboard
# and save it into a variable so we can use it later
user_name = input()
# step 3: say hi back using the user's name
print("Hi, " + user_name + ".")

# one line version of the code above
# print("Hi, " + input("What is your name?") + ".")

print("In what year were you born?")

birth_year = int(input())

your_age = 2025 - birth_year

print("You are about " 
    + str(your_age) 
    + " years old.")

# math we could do here is
# addition, subtraction, multiplication,
# division, modulo (divide & get remainer),
# exponentiation (powers)
# examples are: 
# - calculating age or birth year
# - converting between metric and imperial

half_age = your_age / 2

print("Half of your age is " 
    + str(half_age)
    + ".")