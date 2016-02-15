# cheese_and_cracker is a function of cheese_count and boxes_of_cracker
def cheese_and_crackers(cheese_count, boxes_of_crackers):
 	# %d is used when printing a number (digits)
 	# %s is used when print a name (string)
 	# don't forget that strings must start with a aplpha character ==! number
 	# this will print the cheese_count using %d
 	print "You have %d cheeses!" % cheese_count
 	# will print the number of boxes_of_crackers
 	print "You have %d boxes of crackers!" % boxes_of_crackers
 	# this line is just a statment
 	print "Man that's enough for a party!"
 	# this line is a statment but includes a \n to print that statement onto another line
 	print "Get a blanket."

# this will take 20 and 30 and place them in the lines above
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this will take 10 and 50 and place them in the lines above
# it sill also reset the variables that we are working will and apply them to all new lines else below
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this will take the addition equations and calculate them then place the in the lines above
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this will take the 10 and 50 and add 100 and 1000 to them respectively and place them in the original lines above
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


