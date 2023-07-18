import random
import time
def script():
	while True:
		playrsp = input("pick rock, paper or scissors \n")
		if playrsp in ("rock","paper","scissors"):
			break
		print("only type rock, paper or scissors, try again")
		time.sleep(1)
	complist = ["rock","paper","scissors"]
	playlist = ["paper","scissors","rock"]
	scoreboard = {
  "player": 0,
  "computer": 0
}
	comprsp = (random.choice(complist))
	print(comprsp)
	if complist.index(comprsp) == playlist.index(playrsp):
		print("You win!")
	elif comprsp  == playrsp:
		print("It's a Tie!")
	else:
		print("You lose!")
	while True:
		restart = input("Do you want to play again? (yes/no)")
		if restart in ('yes,''y'):
			script()
			break
		if restart in ('no','n'):
			time.sleep(1)
			print("Thanks for playing. Bye")
			time.sleep(1)
			break
		print("type yes or no")
script()