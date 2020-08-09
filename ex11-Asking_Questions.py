#end is used at the end of each line - this tells print to not end th eline witha newline character and go to the lext line
print("How old are you?", end=' ')
#Converts user input to an integer
#one way to break the code is not putting in a number.
#Later example shows how to recover and prompt again.
age = int(input())
#debug  repr = representation shows the user input after they input characters.
print(">>>> age=", repr(age))


print("How tall are you?", end=' ')
#Converts user input into an integer
height = int(input())
print("how much do you weigh?", end=' ')
#User input is kept as a string?
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Extra credit
# Adds the two integers together with math.
print(age + height)

#Uses format doesn't matter if string or integer. it maes a string and uses the inputs.
#One is an integer, and the other is a string
print(f"{height} + {weight}")

#Converts Integer into string so you can combine the two inputs in a string
print(str(height) + (weight))


# Below doesn't work because you have integer and string
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(height + weight)      #Remove pound sign to test print