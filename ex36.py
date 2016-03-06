from sys import exit

def theater():
	print "You just realized that you forgot your headshot."
	print "There is a photographer on site."
	print "But there is a huge line."
	print "How are you going to skip the line?"
	print "Choices = [taunt people] or [offer them coffee]"
	people_moved = False

	while True:
		choice = raw_input("> ")

		if "coffee" in choice:
			dead("No one wants the coffee and you give it to a hobo...")
		elif choice == "taunt people" and not people_moved:
			print "The people move from the booth becase they get scared."
			print "You can take your picture now."
			people_moved = True
		elif choice == "taunt people" and people_moved:
			dead("Latina happened to be on that and sat on your face...")
		else:
			start()


def film():
	print "You are the only person there."
	print "You are not sure if this is the right place."
	print "What do you do?"
	print 'Choices = [wait], [leave], [ring cow bell]'

	choice = raw_input("> ")

	if "leave" in choice:
		dead("You head out the door and get on with your day.")
	elif "wait" in choice:
		print "You wait for two hours and finally the casting director shows-up."
		print "He gives you the part because you were the only one to show-up."
		print "You later find out that people were stuck in a snow storm."
		print "You walk away with a big grin on your face. Good job!"
	elif choice == "ring cow bell":
		dead("You are kicked out for making nosie")
	else:
		film()




def tv_commercial():
	print "You are waiting on line for 3 hours. What are you going to do?"

	choice = raw_input ("> ")

	if "wait" in choice:
		print "Congrats! You patience paid off and you got the role! Good job!"
	elif "bathroom" in choice:
		dead("You lost your place in line! Better luck next time!")
	else:
		dead("Better luck next time...")

def dead(why):
		print why, " "
		exit(0)

def start():
	print "Welcome to Central Casting!"
	print "What would you like to audition for?"
	print "TV Commercials, Theater, or Film?"

	choice = raw_input("> ")

	if "tv" in choice:
		tv_commercial()
	elif "theater" ==  choice:
		theater()
	elif "film" == choice:
		film()
	else:
		dead("You get kicked out for not being able to make a choice.")

start()


