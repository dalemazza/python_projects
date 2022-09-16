import random
import time
import os



###
#Need to make the game loop better
#Make a level system
### Art used at the start of the program
def art():
	print("""
 ███████ ██  ██████  ██   ██ ████████     ███    ███ ███████     ██████  ██████   ██████  
 ██      ██ ██       ██   ██    ██        ████  ████ ██          ██   ██ ██   ██ ██    ██ 
 █████   ██ ██   ███ ███████    ██        ██ ████ ██ █████       ██████  ██████  ██    ██ 
 ██      ██ ██    ██ ██   ██    ██        ██  ██  ██ ██          ██   ██ ██   ██ ██    ██ 
 ██      ██  ██████  ██   ██    ██        ██      ██ ███████     ██████  ██   ██  ██████  
                                                                                         
""")


## This is the games intro and also takes the hero's name
def intro():

	print("""
The aim of the game is to beat enemies and level up, making you STRONK bro
""")

## Class of character in game
class person():
	def __init__(self, health, attack, gold):
		self.health = health
		self.attack = attack
		self.gold = gold

class item():
	def __init__(self, name, attack, cost, health):
		self.name = name
		self.attack = attack
		self.cost = cost
		self.health = health

## Function to take a random integer of 1-6 if it equal 1 it does double damage
def crit():
	crit = random.randint(1,3)
	if crit == 1:
		return 2
	else:
		return 1

## Function that attacks with the default value and then times it by the crit (if rolled)
def crit_apply(a):
	damage = a.attack * crit()
	return damage

## function to take damage from health
def turn(enemy, user):
	while 1 == 1:
		a = crit_apply(user)
		health(user, enemy)
		time.sleep(2)
		print("Your hero attacks the orc!")
		enemy.health = enemy.health - a
		print(f"You hit the orc for {a}")
		win(user, enemy)
		health(user, enemy)
		time.sleep(2)
		print("The orc attacks you!")
		a = crit_apply(enemy)
		user.health = user.health - a
		print(f"The orc hit you for {a}")
		time.sleep(2)

## user classes
user = person(10,2,2)
enemy = person(10,2,0)

# This checks if the characters has died or not
defwin(user, enemy):
	if user.health <= 0:
		print("The orc has killed you. YOU LOSE")
		exit()
	elif enemy.health <= 0:
		print("You killed the orc. YOU WIN GG")
		print("You found 2g on the orc")
		user.gold += 2
		menu()

# This displays the characters health 
def health(user, enemy):
	print(f"Your hero has {user.health} health, the orc has {enemy.health} health")

# This is the home screen allowing the user to select to fight or go to the shop
def home():
	user.health = 10
	enemy.health = 10
	stats(user)
	option = int(input("""
1. Fight
2. Shop 
"""))
	if option == 1:
		return game()
	elif option == 2:
		return shop()
	else:
		print("That was not an option, Select 1 or 2")
		home()

# This will be shop that can be used to purchase a weapon and armor to increase attack damage and health points with gold.
def shop():
	# Shop items
	dagger = item("Dagger",1,3,0)
	sword = item("Sword",2,6,0)
	axe = item("Axe",4,10,0)
	chainmail = item("Chain Mail",0,2,3)

	#clears the screen 
	os.system('cls')
	print("============ Shop ============")
	print('Shopkeeper - "Looking to protect yourself, or deal some damage?"')
	print(f"You currently have {user.gold}g")
	print("1. Protect yourself \n2. Deal some damage \n3. Leave the creepy shop")
	selection = int(input("Select an option: "))

	if selection == 1:
		os.system("cls")
		print("Armour shop")
		print(f"You currently have {user.gold}g")
		print("1. Chain Mail: 3g")
		armour_sel = int(input("Select an option:"))
		if armour_sel == 1:
			if user.gold > 2:
				user.health += chainmail.health
				user.gold -= 2
				print(f"Your players health is now {user.health}")
				menu()
			else:
				print("You don't have enough gold. Kill more orcs and come back later")
				time.sleep(2)
				shop()


		else:
			print("Guessing you wanted to leave")
			os.system("cls")
			time.sleep(2)
			menu()

	elif selection == 2:
		os.system("cls")
		print("Weapon shop")
		print(f"You currently have {user.gold}g")
		print("1. Dagger: 3g \n2. Sword: 6g \n3. Axe: 10g")
		wpn_sel = int(input("Select an option:"))
		if wpn_sel == 1:
			if user.gold > 3:
				user.attack += dagger.attack
				user.gold -= 3
				print(f"Your players damage is now {user.attack}")
				time.sleep(2)
				os.system("cls")
				menu()
			else:
				print("You don't have enough gold. Kill more orcs and come back later")
				time.sleep(2)
				shop()
		elif wpn_sel == 2:
			if user.gold > 6:
				user.attack += sword.attack
				user.gold -= 6
				print(f"Your players damage is now {user.attack}")
				time.sleep(2)
				os.system("cls")
				menu()
			else:
				print("You don't have enough gold. Kill more orcs and come back later")
				time.sleep(2)
				shop()				
		elif wpn_sel == 3:
			if user.gold > 10:
				user.attack += axe.attack
				user.gold -= 10
				print(f"Your players damage is now {user.attack}")
				time.sleep(2)
				os.system("cls")
				menu()
			else:
				print("You don't have enough gold. Kill more orcs and come back later")
				time.sleep(2)
				shop()

		else:
			print("Guessing you wanted to leave")
			os.system("cls")
			time.sleep(2)
			menu()

	else:
		print("Guessing you wanted to leave")
		os.system("cls")
		time.sleep(2)
		menu()

def stats(user):
	print(f"You have {user.health} HP, {user.attack} attack and {user.gold}g")


def menu():
	art()
	intro()
	home()

def game():
	turn(enemy, user)


menu()