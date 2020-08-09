# Escape sequence for Tabbed in
tabby_cat = "\tI'm tabbed in."
#Escape sequence for new line
persian_cat = "I'm split\non a line."
#Use escape sequence to show \
backlash_cat = "I'm \\ a \\ cat."

#\t is escape sequency for new line
# URL for ascii code. Games used to be made out of these
# https://theasciicode.com.ar/ascii-control-characters/vertical-tab-male-symbol-mars-ascii-code-11.html
# \v doesn't show because its so old
fat_cat = """
I'll do a list:
\t\v* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#Line above does a new line and tab so it looks similar


print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)