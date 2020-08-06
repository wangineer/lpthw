from sys import argv

script, filename = argv

# String that calls the filename from argument above
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

#Outputs a ? needing you to exit script. or press enter to continue.
input("?")

print("opening the file...")
target3 = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target3.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target3.write(line1)
target3.write("\n")
target3.write(line2)
target3.write("\n")
target3.write(line3)
target3.write("\n")

print("And finally, we close it.")
target3.close()
