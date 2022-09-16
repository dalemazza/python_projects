import random, time, sys

#win, lose, ties
wins = 0
loses = 0
ties = 0

#Intro to print intro
def intro ():
	print("""Rock, Paper, Scissors
		- Rock beats Scissors
		- Paper beats Rock
		- Scissors beats Paper""")
#chooses what the ai is going to use based on a random 1-3 
def ai_turn():
	turn = random.randint(1,3)
	if turn == 1:
		print("The ai choose rock")
		return "r"
	elif turn == 2:
		print("The ai choose paper")
		return "p"
	else:
		print("The ai choose scissors")
		return "s"
#simple countdown to build suspense
def countdown():
	print("The computer has chosen..")
	time.sleep(0.50)
	print("1")
	time.sleep(0.50)
	print("2")
	time.sleep(0.50)
	print("3")
#works out if the ai beat the player and adds to the scoreboard
def workings(selection, ai_selection):
	global ties
	global wins
	global loses
	if selection == ai_selection:
		ties += 1
		print("You tied")
	elif selection == "r" and ai_selection == "s":
		print("You win")
		wins += 1
	elif selection == "r" and ai_selection == "p":
		print("You loose")
		loses += 1
	elif selection == "p" and ai_selection == "s":
		print("You loose")
		loses += 1
	elif selection == "p" and ai_selection == "r":
		print("You win")
		wins += 1
	elif selection == "s" and ai_selection == "r":
		print("You loose")
		loses += 1
	elif selection == "s" and ai_selection == "p":
		print("You win")
		wins += 1


#Main game loop 
def game_loop():
	while True:
		while True:
			print(f"You have {wins} wins, {loses} loses and {ties} ties")
			selection = input("Enter your choice (r)ock, (p)aper, (s)cissors or (q)uit >".lower())
			if selection == "q":
				print("Thanks for playing")
				sys.exit()

			if selection == "r" or selection == "p" or selection == "s":
				break
			else:
				print("That wasnt an option")

		if selection == "r":
			print("You have selected rock")
			countdown()
			workings(selection, ai_turn())
		elif selection == "p":
			print("You have selected paper")
			countdown()
			workings(selection, ai_turn())
		else:
			print("You have selected scissors")
			countdown()
			workings(selection, ai_turn())




def game():
	intro()
	game_loop()

game()