print "You are hiking and see a fork in the road. Do you follow the 1st road or the 2nd?"

road = raw_input("> ")

if road == "1":
	print "There is a panda bear eating children. What do you do?"
	print "1. Rescue the screaming child."
	print "2. Run for your life because pandas normally don't eat people."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your ear off. Good job!"
	elif bear == "2":
		print "The enar eats your nose off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif road == "2":
	print "You stare into an empty white space."
	print "1. Strawberries"
	print "2. Nutella"
	print "3. Banana"

crepe = raw_input("> ")
if crepe == "1" or crepe == "2":
	print "Your body survives because of sugar. Good job!"
else:
	print "The crepe rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble into a bar and have a crepe throw in your face. Free food!"