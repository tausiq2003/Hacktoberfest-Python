from tkinter import *
root= Tk()
root.title("calculator")
root.geometry("300x300")
label1 = Label(root, text="Write Here")
label1.grid(row=0, column=0)
entry= Entry(root)
entry.grid(row=0, column=1)
root.mainloop()

#def submission():
    #print("you have submitted it properly")
#button1= Button(root, text="Click Here",bg="pink", command =submission)
#button1.pack()
#button2=Button(root, text="Click Again", bg="red", command= submission)
#button2.pack()
#root.mainloop()