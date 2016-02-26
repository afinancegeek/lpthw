# imports system module 
from sys import exit
# the order in which the functions are place are irrelevant
# you can place the start function at the end and it would work the same
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "You can also choose to use a jetpack and fly up."
	print "Which one do you take?"
# choice allows the user to input a choice
# the conditional statement s if elif and else execute when a choice
# is or is not made
	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	elif choice == "jetpack":
		jet_pack()
	else:
		dead("You stumble around the room until you starve.")

# up choice
def jet_pack():
	print "You're flying high!"
	print "Go higher or stay leveled?"

	choice = raw_input("> ")

	if "leveled" in choice:
		dead("You get attacked by wild birds!")
	elif "higher" in choice:
		dead("You run out of fuel and drop down to an angry bear...")
	else:
		jet_pack()

#left choice
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	# boolean variable is created using bear_moved

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not  bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True


		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
# right choice
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for you life or eat your head?"

	choice = raw_input("> ")
# in means what the user inputs into the choices
# it's basically a keyword that tiggers the exucution of an arg
	if "flee" in choice:
		print "You take cover in a huge sparkling room."
		print gold_room()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input ("> ")
	if "0" in choice or "1" in choice:
		# int(choice) --> converts the raw_input into a string
		# this string is an interger
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def dead(why):
	print why, "Good job!"
	exit(0)

start()