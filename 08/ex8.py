# create a format string
formatter = "{} {} {} {}"

# fill in the placeholders of the format string with integers
print(formatter.format(1, 2, 3, 4))
# repeat with other strings
print(formatter.format("one", "two", "three", "four"))
# repeat with boolean
print(formatter.format(True, False, False, True))
# repeat with the formatter string
print(formatter.format(formatter, formatter, formatter, formatter))
# repeat with strings written in code on separate lines
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
