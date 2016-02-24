the_count = [1, 2, 3, 4]
fruits = ['apple', 'orange', 'pear', 'strawberry']
coffee - [1, 'black', 2, 'white', 3, 'mocha']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "This is %s" % fruit

for i in coffee:
	print "This is %r" % i

elements = []

for i in range(0, 6):
	print "This is %r" % i
	elements.append(i)