import tkinter as tk
import random

val = ["It is certain","It is decidedly","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
window = tk.Tk()
window.title("Magic 8 Ball")
Q1 = tk.Label(window, text="What is your question?")
Q1.pack()
E1 = tk.Entry(window)
E1.pack()
L1 = tk.Label(window)

#window.geometry("200x200")

def prediction():
    if E1.get() == "" or "?" not in E1.get():
        L1.config(text= "You haven't asked a question!")
        L1.pack()
    else:
        L1.config(text =random.choice(val))
        L1.pack()
        B1.config(state="disabled")

B1 = tk.Button(window,text="Shake the magic 8-ball!",command= lambda: prediction())
B1.pack()

#L1 = tk.Label(window,text=E1.get())
#L1.pack()

window.mainloop()