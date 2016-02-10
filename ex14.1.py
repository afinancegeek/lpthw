from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "What type of coffee do you like dirnking %s?" % user_name
likes = raw_input(prompt)

print "What do you like in your coffee?"
add = raw_input(prompt)

print "Where do you usually drink coffee?"
where = raw_input(prompt)

print """
Here You Are %r coffe with %r at %r >;P

     )))
    (((
  +-----+
  |     |]
  `-----'   
___________
`---------'



""" % (likes, add, where)