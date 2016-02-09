# imports the system module
from sys import argv

script, age, height, weight, hair_color = argv

# added several arguments
print "The script is called:", script
print "Your first variable is:", age
print "Your fourth variable is:", height
print "Your third variable is:", weight
print "Your fourth variable is:", hair_color

age = raw_input("How old are you?")
height = raw_input("How tall are you? ")
weight = raw_input ("How much do you weigh? ")
hair_color = raw_input ("What color is your hair? ")

print "So, you're %ryr's old, %rft tall, %rlbs heavy, and have %r hair." % (
	age, height, weight, hair_color) 