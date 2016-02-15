def snow_days(january, febuary):
	print "These are the number of snow days in each month:"
	print "In January we had %d snow days" % january
	print "In Febuary we had %d snow days" % febuary
	print "You'd better get a warmer jacket!"
	print "." * 10

print "We can give the function numbers directly:"
print "How many days did it snow in January?"
january = raw_input()
print "How many days did it snow in Febuary?"
febuary = raw_input()

print "Or, we can use variables from our script:"
january = 20
febuary = 20

snow_days(january, febuary)

print "We can even do math inside too:"
print "Addition:"
snow_days(10 + 5, 15 + 5)

print "We can even subtract:"
snow_days(10 - 5, 15 - 5)

print "We can even multiply:"
snow_days(10 * 2, 15 * 1)

print "We can even divide:"
snow_days(10 / 5, 15 / 5)

snow_days(january + 100, febuary + 1000)
snow_days(january - 20, febuary - 20)
snow_days(january * 2, febuary * 2)
snow_days(january / 2, febuary / 2)