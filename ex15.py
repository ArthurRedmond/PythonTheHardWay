from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

pritn("Type the filename again:")
file_again = input("> ")

txt_again = open(filename)

print(txt_again.read())
