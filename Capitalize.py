# Python program to read a file and capitalize
# the first letter of every word in the file.

#A file named "gfg", will be opened with the
# reading mode.
file_test1 = open('text1.txt','r')

# This will traverse through every line one by one
# in the file

for line in file_test1:

    # This will convert the content
    # of that line with capitalized
    # first letter of every word

    output = line.title()

    # This will print the output
    print(output)
