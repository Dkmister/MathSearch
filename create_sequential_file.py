FIGURE================================================

# This program makes a copy of one sequential file into another.

# Ask the user for the names of the files to read from and to write to:

inputfilename = raw_input("Type input file to copy: ")
outputfilename = raw_input("Type output file: ")  # this can be a name of a
                                             # file that does not yet exist

# A file must be opened --- this requires a new variable to hold the
#   address in heap storage of the file's data-structure representation:

input = open(inputfilename, "r")  # "r" means we will read from inputfilename
output = open(outputfilename, "w") # "w" means we will write to outputfilename

## You can read the lines one by one with a while loop:
#
# line = input.readline()   # read the next line of  input --- this includes
#                           #   the ending  \r  and  \n  characters!
#                           # The line is of course a string.
#
# while line != "" :        # When the input is all used up,  line == ""
#    print line
#    output.write(line)     # Write the string to the output file
#    line = input.readline()

# But here is the simplest way to read all the lines one by one:

for line in input :
    print line    
    output.write(line)

# when finished, you must close the files:
input.close()  
output.close()
