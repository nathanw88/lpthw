from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit ctrl-c (^c).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print ("And finally, we close it.")
target.close()

target1 = open(filename)
print(target1.read())
