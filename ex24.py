print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# \t indents 8 spaces; if written twice will indent 16 spaces
# \n is the same an hitting return on the keyboard
poem = """
\tThe lovely world
with logic so firmly planeted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# prints poem and puts some space in-between
print "_______________"
print poem
print "_______________"

# this sets the variable five to 5
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# thesse variables are assigned within the function
# they are know as local variables as opposed to global variables
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# this calls our function and fills the three variables
# any varibales can be used (ex: x,y,z)
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# takes the variable divides it by 10 and spits it back out
start_point = start_point / 10
# %d outputs a digit in the order that it was input above
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)