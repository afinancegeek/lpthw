# creates an empty list (similar to an array in other languages) 
i = 0
numbers = []

# for while-loops and argument is created that is similar to 'def' 'if' and
# for for-loops we put an colon at the end of the first statement and an
# indent in the following statement 
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num
