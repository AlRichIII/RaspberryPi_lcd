from tkinter import *

root = Tk()

root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

#topframe = Frame(root)
#topframe.pack(side=TOP)
#bottomframe = Frame(root)
#bottomframe.pack(side=BOTTOM)


#button1 = Button(topframe, text = "Lights", bg="black", fg = "white")
#button2 = Button(topframe, text = "Water", bg="black", fg = "white")
#button3 = Button(topframe, text = "Temp/Humidity", bg="black", fg = "white")
#button4 = Button(topframe, text = "Other", bg="black", fg = "white")
#button5 = Button(bottomframe, text = "INFO", bg="white", fg = "red")
menu1 = ['Lights','Water','Temp/humidity','Other']

r = 0
for c in menu1:
    Button(text=c,bg='black',fg='white', relief=RIDGE,width=30,height=8).grid(row=r,column=0)
    #Entry(bg='black', relief=SUNKEN,width=50).grid(row=r,column=1)
    r=r+1
    

Button(text='Up',bg='blue',fg='white', relief=RIDGE,width=30,height=8).grid(row=1,column=1)
Button(text='Down',bg='blue',fg='white', relief=RIDGE,width=30,height=8).grid(row=2,column=1)
Button(text='INFO',bg='blue',fg='white', relief=RIDGE,width=30,height=8).grid(row=3,column=1)
#button1.grid(row=0,column=0)
#button2.grid(row=0,column=1)
#button3.grid(row=1,column=0)
#button4.grid(row=1,column=1)
#button5.pack(bottomframe)

#c = Checkbutton(root, text="keep me signed in")
#c.grid(columnspan=2)

root.mainloop()
