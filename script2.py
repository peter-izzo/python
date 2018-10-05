from tkinter import *

window=Tk()
window.title(string="Pete's Magical Number Converter")

#conversions
def kgconvert():
    try:
        #calculating values
        gm=float(ui_value.get())*1000
        lb=float(ui_value.get())*2.20462
        oz=float(ui_value.get())*35.274

        #hopefully getting the values to stay in their boxes
        gm1box.insert(END, gm)
        lb1box.insert(END, lb)
        oz1box.insert(END, oz)
    except:
        #should create an error popup if any values other than numbers are entered
        top= Toplevel()
        top.title("Error")

        msg = Message(top, text="Please enter a valid number")
        msg.pack()

        butt = Button(top, text="Ok", command=top.destroy)
        butt.pack()



#added top photo
photo= PhotoImage(file="C:\\Users\\Pete\\Pictures\\shrek.gif")
ppLb1=Label(image=photo, width=432, background="white")
ppLb1.grid(row=0, column=0, columnspan=4)

#convert button
b1=Button(window,text="Convert", width=20, command=kgconvert)
b1.grid(row=1, column=3)

kg=Label(window, text="Kg", width=20)
kg.grid(row=1, column=0)

#user input kilograms
ui_value=StringVar()
ui_value=Entry(window, textvariable=ui_value)
ui_value.grid(row=1, column=1)
#this creates a placeholder that gets removed upon clicking the box
ui_value.bind("<FocusIn>", lambda args:ui_value.delete('0', 'end'))
ui_value.insert(0,"Enter a number")



#grams label and conversion text
gm1=Label(window, text="Grams", width=20)
gm1.grid(row=2, column=0)
gm1box=Text(window, height=1, width=20)
gm1box.grid(row=3, column=0)

#pounds label and conversion text
lb1=Label(window, text="Pounds", width=20)
lb1.grid(row=2, column=1)
lb1box=Text(window, height=1, width=20)
lb1box.grid(row=3, column=1)

#ounces label and conversion text
oz1=Label(window, text="Ounces", width=20)
oz1.grid(row=2, column=3)
oz1box=Text(window, height=1, width=20)
oz1box.grid(row=3, column=3)







window.mainloop()
