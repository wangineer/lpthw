from sys import argv

# set arguments. so first is filename, and then you have to enter the Filename
script, filename = argv
# Varaiable
txt = open(filename)

#f string calles the filename and tells user the filename
print(f"Here's your file {filename}:")
#Prints the file contents from the filename mentioned from user from first call "python ./ex15-Reading_Files.py .\ex15_sample.txt
print(txt.read())

#Displays text asking user to enter filename
print("Type the filename again:")

#creating variable file_again to be called later and store the filename prompted by user
file_again = input("> ")
# creating variable to be called. when variable is called, it asks to open what is stored for file_again
txt_again = open(file_again)

#calling txt_again variable opens file_again which has user imported filename.
print(txt_again.read())

#closing stuff at the end
#you close these because they call the "open()"
txt.close
txt_again.close

######################## Output
#C:\Users\lpthw> python .\ex15-Reading_Files.py .\ex15_sample.txt
#Here's your file .\ex15_sample.txt:
#This is stuff I typed into a file.
#It is really cool stff.
#Lots and lots of fun to have in here.
#Type the filename again:
#> ex15_sample.txt
#This is stuff I typed into a file.
#It is really cool stff.
#Lots and lots of fun to have in here.
##PS C:\Users\lpthw>