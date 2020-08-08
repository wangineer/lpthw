print("Mary had a little lamb.")
# Inserts snow inside the statement because sometimes you can't do an f string (format like previous example.
print("It's fleece was white as {}.".format('snow'))
# Same as going this
print(f"It's fleece was white as {'snow'}.")
#You can add additional - this was not part of excercise i did this on my own.
print("This is the {} and this is the {}.".format('first', 'second'))
print("And everywhere that Mary went.")

# Repeats . 10 times - multiplies string 10 times
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# When you remove the end=" " adds a space instead of creating a new line for burger
# End seems to be a predefined statement.
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)

print(end1 + end2 + end3 + end4 + end5 + end6, end=" should always be on your ")
print(end7 + end8 + end9 + end10 + end11 + end12)

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)