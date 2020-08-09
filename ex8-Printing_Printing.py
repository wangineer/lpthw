#Format is used in previous example.
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# Debug test

lines = (
    "Try your", #Remove Comma to test.
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)
print(">>>> lines", repr(lines))
print(formatter.format(*lines))
# This is the output showing that comma is missing
#>>>> lines ('Try yourOwn text here', 'Maybe a poem', 'or a song about fear')

