import random
import time
scoreboard = {
  "player": 0,
  "computer": 0
}
def script():
	while True:
		playrsp = input("Type rock, paper or scissors \n")
		if playrsp in ("rock","paper","scissors"):
			break
		print("Only type rock, paper or scissors, try again")
		time.sleep(1)
	complist = ["rock","paper","scissors"]
	playlist = ["paper","scissors","rock"]
	comprsp = (random.choice(complist))
	print("computer held out "+comprsp)
	time.sleep(0.5)
	if complist.index(comprsp) == playlist.index(playrsp):
		print("You win!")
		scoreboard["player"]+=1
		time.sleep(0.5)
	elif comprsp  == playrsp:
		print("It's a Tie!")
	else:
		print("You lose!")
		scoreboard["computer"]+=1
		time.sleep(0.5)
	while True:
		for k,v in scoreboard.items():
			print(k+"'s score = "+str(v))
			time.sleep(0.5)
		restart = input("Do you want to play again? (yes/no)")
		if restart in ('yes','y'):
			script()
			break
		if restart in ('no','n'):
			time.sleep(1)
			print("Thanks for playing.")
			time.sleep(0.5)
			bye = 'Bye.\n' 
			for i in range(5): print(bye[i], sep='', end='', flush=True); time.sleep(0.3)
			time.sleep(1)
			break
		print("type yes or no")
script()