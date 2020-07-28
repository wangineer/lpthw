# If you compare with previous ex11 file you will see that there are multiple print statements.
# Here within setting the variable, you are requesting input from user while asking the prompt.
# What the user provides, it will be stored as the varialb.e and later be printed out.
# f in print statment allows you to pull the variables into the string.
# using pydoc
# python -m pydoc .\ex12-Prompting_People.py
# This prints out descriptions. and the inputted data that users provided. and filename.

age = input("How old are you?" )
height = input("How talla re you? ")
weight = input("How much do you weigh> ")

print(f"So, your {age} old, {height} tall and {weight} heavy.")
