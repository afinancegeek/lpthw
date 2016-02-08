#This is the first string within a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#This is the second string within a string
print "I said: '%s'." % y
print "I also said: '%s." % y

#This is the third string within a string
hilarious = False
joke_evaluation = "Itsn't that joke so funny?! %r"

print joke_evaluation % hilarious

#This is the fourth string within a string
w = "This is the left side of..."
e = "a string with a right side."

print w + e