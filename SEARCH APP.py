from tkinter import *
import wikipedia
root = Tk()
root.title("Search App")
root.geometry("300x400")
def get():
    entry_value =entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "Please insert valid search or check the internet connection")

topframe = Frame(root)
topframe.pack(side=TOP)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text ="Click Here", command=get)
button.pack()
bottomframe = Frame(root)
bottomframe.pack()
scroll = Scrollbar(bottomframe)
scroll.pack(side = RIGHT, fill = Y)
answer = Text(bottomframe, width=300, height=300,yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command = answer.yview)
answer.pack()

root.mainloop()
