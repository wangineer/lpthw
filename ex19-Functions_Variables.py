# This is the definition
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# This calls the definition above and applies 20 and 30
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# This sets up the varialbes
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# This calls the definition and uses the variables listed above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This calls the definition and does match inside the arg
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# This calls the Function and puts the variables and math as well.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#Bonus  Try to prompt user
crackerinput = input("Type the cracker input? ")
print(f"This is what user inputted {crackerinput}!")
cheese_and_crackers(int(crackerinput), amount_of_crackers + int(crackerinput))

