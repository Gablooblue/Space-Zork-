from sys import exit

def start():
	print "You wake up and find yourself inside a spaceship"
	choice = raw_input("> ")
	global crowbar
	crowbar = False
	while True:
		if "look" in choice:
			print "You look around and see a crowbar on the ground, there is also an airlock in front of you. "
			print "What do you do?"
			choice2 = raw_input("> ")
			
			if "crowbar" in choice2 or "pickup" in choice2:
				print "You have picked up the crowbar"
				crowbar = True
				
			elif "airlock" in choice2 or "open" in choice2:
				print "It's locked. You look to your right and you see a terminal. What do you do?"
				choice3 = raw_input("> ")
				
				if "terminal" in choice3 or "use" in choice3:
					print "You use the terminal and the airlock hisses and then opens."
					choice4 = raw_input("> ")
					
					if "go" in choice4 or "airlock" in choice4 or "leave" in choice4:
						main_room()
						break						
					else:
						print "You can't do that" 
						continue
				else: 
					print "You can't do that" 
					continue
			else:
				print "You can't do that" 
				continue	
				
		elif "Harambe" in choice:
			print "Dicks out for Harambe"
		
		else:
			print "You can't do that" 
			continue

def main_room():
	print "You walk into the main room"
	print "What do you do?"
	choice = raw_input("> ")
	door = False
	door2 = False
	stop = True
	while stop:
		if "look" in choice:
			print "You look around and you see 2 doors, one to the left and one to the right. There seems to be a foul odor coming from the right door"
			print "Which door do you go to?"		
			
			stop = False
		while True:
			choice2 = raw_input("> ")
			if "left" in choice2 and not door:
				print "The door is jammed. It looks like you could pry it open with a crowbar."
				print "What do you do?"
				choicecb = raw_input("> ")
				
				if "crowbar" in choicecb and crowbar:
					print "You pry the door open with a crowbar"
					door = True
					continue
					
			
			if "left" in choice2 or "door" in choice2 or "go" in choice2 and door:
				print "You go through the door"
				locker_room()
				break
			elif "right" in choice2 and door2: 
				print "The door is locked. It seems like you need a keycard to enter"	
			elif "right" in choice2 and not door2:
				print "You walk up to the door, swipe your keycard, and you go through the door."
				command_bay()
				break
			elif "back" in choice2 or "airlock" in choice2:
				print "The door wont budge"
		
			else:
				print "You can't do that"
				continue
		

def locker_room():
	print "You enter the room"
	print "What do you do?"
	choice = raw_input("> ")
	global door2
	door2 = False
	death = False
	while True:
		if "look" in choice:
			print "You look around the room and you see three numbered lockers."
			print "Do you open locker 1, 2, or 3 or do you leave?"
			choicelck = raw_input("> ")
			
			if "1" in choicelck or "one" in choicelck:
				print "The locker is empty"
			elif "2" in choicelck or "two" in choicelck:
				print "The locker swings open and you see a keycard. Do you pick it up?"
				choicekc = raw_input("> ")
				
				if "yes" in choicekc or "pick" in choicekc:
					print "You pick up the keycard."
					door2 = True
				elif "no" in choicekc:
					print "You dont pick it up"
				else:
					print "You can't do that" 
					continue
			
			elif "3" in choicelck and not death:
				print "It doesn't want to open"
				death = True
			elif "3" in choicelck and death:
				print "The locker swings open and a creature jumps out and melts your face off"
				dead()
			elif "exit" in choicelck or "leave" in choicelck or "back" in choicelck:
				main_room()
				break
			else: 
				print "You can't do that" 
				continue
		
		elif "quit" in choice:
			exit()
		else:
			print "You can't do that" 
			continue
		
def command_bay():
	print "You walk in and the odor is so strong it almost makes you vomit"
	print "What do you do?"
	choice = raw_input("> ")
	path = False
	stop = True
	while stop:
		
		if "look" in choice:
			print "You look around and you see blood everywhere, the floor is littered with dead bodies."
			print  "You see the emergency communication system on the other side of the room"
			print "Suddenly a 5ft salamander-like creature lunges at you, you manage to hit it with a crowbar and it's discombobulated"
			print "You need to finish it off"
			print "there's a survival knife to your left and your crowbar is in your hand, which one do you choose?"
			stop = False
			
		while True:
			choicewep = raw_input("> ")
			if "knife" in choicewep:
				print "You grab the knife and stab it in the heart and you kill it. It's acid blood starts melting the knife, turning it into a weird grey goo"
				print "The path to the comms system is now clear. "
				path = True
				break
			elif "crowbar" in choicewep:
				print "You go and try to bludgeon the creature with the crowbar; but as you swing your crowbar snaps in half." 
				print "You realize that the creature's naturally acidic blood must have weakened it."
				print "The creature recovers and bites your arm off; then as you're screaming, it bites your head off"
				dead()
			else: 
				print "Your indecisiveness and stupidity allowed the creature to recover and it lunges at you a second time. "
				print "The creature claws your neck and blood starts gushing out."
				dead()
		
	if path:
		print "You walk up to the comms system and move the dead body that was lying on the console"
		print "As the body falls on the floor you see it's nametag \"Sherry\""
		print "Memories flood your head and you start to remember everything"
		print "You were out on a space walk, talking to Sherry about settling down when you get home, suddenly you started hearing screaming coming from your intercoms"
		print "You enter the airlock and suddenly the ship jerks violently and you hit your head and pass out"
		print "And now you're here"
		print "Suddenly you hear someone talking to you on the comms system"
		print '"Hello is anybody there? I repeat, is anybody there?"'
		print '"I hear you loud and clear, this is engineer James Earl ship 90382 and we require immediate assistance in sector 5, there has been a breach"'
		print '"Copy that 90382, sending emergency services over now"'
		print "THE END"
		exit()
	
	if "quit" in choice or "exit" in choice:
		exit()
	else: 
		print "You can't do that" 
			
		
def dead():
	print "You're dead."
	print "Retry? Y or N"
	retry = raw_input("> ")
	if "Y" in retry:
		main_room()
	else:
		exit()
		

def menu():
	while True:
		print "start game"
		print "help"
		print "quit"
		menu_input = raw_input("> ")
		
		if "start" in menu_input or "game" in menu_input:
			start()
			break
		elif "help" in menu_input:
			help()
		elif "quit" in menu_input:
			exit()
		else: 
			print "Please select one of the options"
			continue
	
def help():
	while True:
		print "The game is a text adventure"
		print "If you want to look around, type \"look\" and press enter"
		print "If you want to interact with something, type it out and press enter."
		print "If you want to leave the game at any point type \"quit()\""
		print "Make sure to type in lowercase"
		print "Do you want to go back to the menu?"
		help_choice = raw_input("> ")
		if "yes" in help_choice or "menu" in help_choice:
			menu()
			
		else:
			print "Repeating help"
		
menu()
				
