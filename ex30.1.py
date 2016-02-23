people = 15
cars = 15
trucks = 7
# if there are more cars then people the print the first statement
# if there are more people than car then print the second statment
# if both cars and people are equal print that we cannot decide
if cars > people:
	print "We should take the cars."
elif cars < people:
		print "We shsould not take the cars."
else:
	print "We can't decide."
# if there are more strucks than cars print the first statement
# if there are more cars the trucks prin the second statement
# if there are equal amounts of cars and trucks that print we cannot decide
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
# if there are more people that trucks print the first statement
# if anyhthing else occurs than print let's stay at home
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
# if there are more or equal as many cars as people and more people
# thank trucks then print the first statement
# ottherwise if the is less people than trucks then print the second
if cars >= people > trucks:
	print "Let's each take our own car"
elif people < trucks:
	print "We should just stay at home"