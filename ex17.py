# imports argument variable from system modules
from sys import argv
# os path is used because of different os (ex: max, win, linux)
# we import exists from os.path module or library
# exists is a function that returns true if the file path is valid
from os.path import exists
# we setup the argument starting with self
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
indata = open(from_file).read()
# this will out put the bytes in the file using the len (length) function	
# this will check if the file exisit and return true or false respectfully
# raw_input will read wether your input RETURN or CTRL-C and print according
print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continuem CTRL-C to abort."
raw_input()
# the out_file function will open the new file and if it doesn't exisit
# it will create the file allowing you to write to it
# 'w' stand for write

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."
# this make sure to close the file and we use one line because
# we shortened the earlier line opening the files
out_file.close()


# one line version:
# from sys import argv; from os.path import exists; script, from_file, to_file = argv; in_file = open(from_file).read; out_file = open(to_file), 'w'); out_file.write(indata); out_file.close()
