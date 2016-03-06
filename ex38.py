# creates a string by setting ten_things to equal to the list
ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."
# what exactly does the .split do?
# stuff = split(ten_things, ' ')
stuff = ten_things.split(' ')
# creates a list by more_stuff to equal to []
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# states that if the length of stuff does not equal 10 items execute the block below
while len(stuff) !=10:
	# next_one is used to populate stuff with more stuff if there isn't enough stuff
	# next_one = pop(more_stuff)
	next_one = more_stuff.pop()
	# next_one will take what's in more_stuff a populate the line
	print "Adding: ", next_one
	# this line will add what'sin next_one to stuff
	# next_one = append(stuff)
	stuff.append(next_one)
	# this line will count the number of things in the list using len()
	print "There are %d items now." % len(stuff)
# this like will out put everything in stuff
print "There we go: ", stuff

print "Let's do some things with stuff."
# this line will call what's in stuff with the cardinal number 1
print stuff[1]
# this line will call what's on stuff with the cardinal number -1
# it goes backwards on the index
print stuff[-1] # whoa! fancy
# this line will populate a list containing everything in stuff
print stuff.pop()
# this line will take everything that's in stuff and join it up to 10 things
print ' '.join(stuff) # what? cool!
# thuis will take stuff and join everything from cardinal 3 to 4
# it works similiar to range and does not include 5 ex: range(3, 5)
print '#'.join(stuff[3:5]) # super stellar

print stuff
