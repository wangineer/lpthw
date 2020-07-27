#end is used at the end of each line - this tells print to not end th eline witha newline character and go to the lext line
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("how much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
