import random
playrsp = input("pick rock, paper or scissors \n")
complist = ["rock","paper","scissors"]
playlist = ["paper","scissors","rock"]
comprsp = (random.choice(complist))
print(comprsp) 
if complist.index(comprsp) == playlist.index(playrsp):
	print("You win!")
elif comprsp  == playrsp:
	print("It's a Tie!")
else:
	print("You lose!")
