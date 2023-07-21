import tkinter as tk
import random

val = ["It is certain","It is decidedly","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
window = tk.Tk()
window.title("Magic 8 Ball")
Q1 = tk.Label(window, text="What is your question?")
Q1.pack()
E1 = tk.Entry(window)
E1.pack()

#window.geometry("750x250")

def prediction():
    tk.Label(window, text =random.choice(val)).pack()


B1 = tk.Button(window,text="Shake the magic 8-ball!",command= lambda: prediction())
B1.pack()
window.mainloop()