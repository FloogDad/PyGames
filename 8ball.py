import random
import time
def script():
	val = ["It is certain","It is decidedly","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
	input("What is your question? \n ")
	time.sleep(1)
	print("thinking")
	time.sleep(1) 
	print("...") 
	time.sleep(1)
	print(random.choice(val))
	time.sleep(1)
	while True:
		restart = input("Do you want to ask another question? (yes/no)")
		if restart in ('yes,''y'):
			script()
			break
		if restart in ('no','n'):
			time.sleep(1)
			print("Thanks for playing 8ball. Bye")
			time.sleep(1)
			break
		print("type yes or no")
script()
