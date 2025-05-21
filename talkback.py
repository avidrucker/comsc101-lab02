# REQUIRED: describe the program & what it will do
# I want this program to ask the user for 
# their name "What's your name?" and then, 
# I want the program to say "Hi, NAME" 
# back where NAME is the user's actual name
# Secondly, this program will ask for the user's
# birth year, calculate their approx. age, and then
# say that age back to the user

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

birth_year = input()

print("You are about " 
    + str(2025 - int(birth_year)) + " years old.")