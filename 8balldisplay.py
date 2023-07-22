import tkinter as tk
import random

val = ["It is certain","It is decidedly","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
window = tk.Tk()
window.title("Magic 8 Ball")
Q1 = tk.Label(window, text="What is your question?")
Q1.pack(anchor='nw',side='left')
E1 = tk.Entry(window)
E1.pack(anchor='n',side='left')
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
        B2.config(state="disabled")

def clear():
    E1.delete(0,'end')

def reset():
    B1.config(state="active")
    B2.config(state="active")
    L1.config(text="")
    E1.delete(0,'end')

def close():
    window.destroy()


B1 = tk.Button(window,text="Shake the magic 8-ball!",command=prediction)
B1.pack()

B2 = tk.Button(window, text="Clear text",command=clear)
B2.pack(anchor='w',side='top')

B3 = tk.Button(text="Play Again",command=reset)
B3.pack(anchor='sw',side='top')

B4 = tk.Button(text="Quit",command=close)
B4.pack(anchor='sw',side='bottom')


#L1 = tk.Label(window,text=E1.get())
#L1.pack()

window.mainloop()