# print out all escape sequences

escape_sequences = '''
\\
\'
\"
\a
testing\b\b\b backspace
test\fformfeed
test\nlinefeed
\N{DAGGER}
test Carriage\rreturn
\t* tab
\u041a unicode 16 bit
\U000001a9 unicode 32 bit
\043 octal character value
\x23 hex character value
'''

print(escape_sequences)
print("." * 80)
print(u"\u041a")
print(u"\U000001a9")
