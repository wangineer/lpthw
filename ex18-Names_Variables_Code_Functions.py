# This one is like your scripts with argv

#the *args tells Python to take all the arguments to the function and then put them in args as a list.  ITs like a argv that you've bene using but for functions.
# Its not normally use too often unless specifically needed.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:  {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nothing'.")

print_two("ZED","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

