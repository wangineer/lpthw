# How to run python test.txt ex16output.txt
# This copies contents of file and transfers to another.
#PS C:\Users\github\lpthw> python .\ex17-More_Files.py test.txt ex17output.txt
#Copying from test.txt to ex17output.txt
#The input file is 51 bytes long
#Does the output file exist? False
#Ready, hit RETURN to continue, CTRL-C to abort.

#Alright, all done.
#PS C:\Users\github\lpthw>


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#LEN gets the length of the string that we pass and returns a number.
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
