from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# In order to run the script you have to provide th e arguments in the python script
# PS C:\Users\lpthw> python .\ex13-Parameters_Unpacking_Variables.py first 2nd 3rd
# The script is called: .\ex13-Parameters_Unpacking_Variables.py
# Your first variable is: first
# Your third variable is: 3rd
# PS C:\Users\lpthw>