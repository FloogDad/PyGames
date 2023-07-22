import tkinter as tk
import random

val = ["It is certain","It is decidedly","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
window = tk.Tk()
window.title("Magic 8 Ball")
window.geometry("750x270")

left_frame = tk.Frame(window)
left_frame.grid(row=0, column=0)


Q1 = tk.Label(left_frame, text="What is your question?",font='Arial 18 bold')
Q1.grid(row=1, column=0)

E1 = tk.Entry(left_frame,font='Arial 18 bold',fg='blue')
E1.grid(row=1,column=1)

#L1 = tk.Label(left_frame)


def prediction():
    if E1.get() == "" or "?" not in E1.get():
        T1 = tk.Toplevel(window)
        T1.geometry("750x270")
        T1.title("Did you forget the question mark?")
        tk.Label(T1, text="You haven't asked a question!",font=('Arial 18 bold')).pack()
        
    else:
        T1 = tk.Toplevel(window)
        T1.geometry("750x270")
        T1.title("Prediction")
        tk.Label(T1,text =random.choice(val),font=('Arial 18 bold')).pack()
        B1.config(state="disabled")
        B2.config(state="disabled")

def clear():
    E1.delete(0,'end')

def reset():
    B1.config(state="active")
    B2.config(state="active")
    #L1.config(text="")
    E1.delete(0,'end')

def close():
    window.destroy()


B1 = tk.Button(left_frame,text="Shake the magic 8-ball!",command=prediction,font='Arial 18 bold')
B1.grid(row=2,column=1)

B2 = tk.Button(left_frame, text="Clear text",command=clear)
B2.grid(row=1,column=2)

B3 = tk.Button(left_frame,text="Play Again",command=reset)
B3.grid(row=2,column=0)

B4 = tk.Button(left_frame,text="Quit",command=close)
B4.grid(row=4,column=0)


#L1 = tk.Label(window,text=E1.get())
#L1.pack()

window.mainloop()