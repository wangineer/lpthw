types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#Debug - to test debug remove the "f" on y = statement above.
print(">>>> Print after assign y", y)

print(x)

#debug
print(">>>> Before printing y", y)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evalution = "Isn't that joke so funny?! {}"

print(joke_evalution.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
