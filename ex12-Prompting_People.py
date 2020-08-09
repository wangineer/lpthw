# If you compare with previous ex11 file you will see that there are multiple print statements.
# Here within setting the variable, you are requesting input from user while asking the prompt.
# What the user provides, it will be stored as the varialb.e and later be printed out.
# f in print statment allows you to pull the variables into the string.
# using pydoc
# python -m pydoc .\ex12-Prompting_People.py
# This prints out descriptions. and the inputted data that users provided. and filename.

age = int(input("How old are you? "))
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, your {age} old, {height} tall and {weight} heavy.")


#extra credit
#for some reason "age1" prompt has cursor at beginning of string instead of end
age1 = input("How old are you? ")
#call the previous inputted age into next input string
height1 = input(f"You're {age1}? Nice. How tall are you? ")
weight1 = input("How much do you weigh? ")

print(f"So, your {age1} old, {height1} tall and {weight1} heavy.")