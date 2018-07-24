from sys import argv

# store arguments in variables
script, filename = argv
# open the file and assign it to the variable
txt = open(filename)

# print the file name that will be red
print(f"Here's your file {filename}:")
# print the contents of the file
print(txt.read())
# close the file after use
txt.close()

#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
