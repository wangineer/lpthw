from sys import argv

#i added potatoes
script, user_name, potatoes = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions about {potatoes}.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# I added Carbs
print(f"What kind of Potatoes do you like {user_name}")
carbs = input(prompt)

# I added Carbs
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Oh yeah, don't forget about {carbs}!
""")


################################### How to Run
#PS C:\Users\lpthw> python .\ex14-Prompting_and_Passing.py kfire potatoes
#Hi kfire, I'm the .\ex14-Prompting_and_Passing.py script.
#I'd like to ask you a few questions about potatoes.
#Do you like me kfire?
#> totes
#Where do you live kfire?
#> Hogwartz
#What kind of computer do you have?
#> dell
#What kind of Potatoes do you like kfire
#> french fries
#
#Alright, so you said totes about liking me.
#You live in Hogwartz. Not sure where that is.
#And you have a dell computer. Nice.
#Oh yeah, don't forget about french fries!
#
#PS C:\Users\lpthw>