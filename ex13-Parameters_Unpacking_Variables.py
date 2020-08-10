# argv stands for argument varialble or vector
#allows you to use commandline arguments like "ls ex1*.py   note the use of the astrisk after the ex1
# from Sys "system" module import the argv feature.
#python -m pydoc sys
#argv -- command line arguments; argv[0] is the script pathname if known
from sys import argv
# read the WYSS section for how to run this
first, script, second, third = argv

print("The script is called:", third)
print("Your first variable is:", second)
print("Your second variable is:", first)
print("Your third variable is:", script)



# In order to run the script you have to provide th e arguments in the python script
# PS C:\Users\lpthw> python .\ex13-Parameters_Unpacking_Variables.py first 2nd 3rd
# The script is called: .\ex13-Parameters_Unpacking_Variables.py
# Your first variable is: first
# Your third variable is: 3rd
# PS C:\Users\lpthw>
