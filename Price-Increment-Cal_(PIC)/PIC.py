from tkinter import *


fpage = Tk()
fpage.geometry("200x130")
fpage.configure(bg="Black")
fpage.title("PIC")
fpage.iconbitmap('C:/Python/Projects/Trading/T.ico')
fpage.resizable(width=False, height=False)


U1 = Entry(fpage,width=200,borderwidth=5)
U1.insert(0, "Starting Value")

U2 = Entry(fpage,width=200,borderwidth=5)
U2.insert(0, "Final Value")

U3 = Entry(fpage,width=200,borderwidth=5)
U3.insert(0, "Answer")
U3.configure(state='readonly')


def Calculate():

    SV = float(U1.get())
    FV = float(U2.get())

    PI = (FV-SV)/SV*100


    U3.configure(state='normal')
    U3.delete(0, END)
    U3.insert(0, str(PI) + ' %')
    U3.configure(state='readonly')




CALbutton = Button(fpage, borderwidth=5, text="Calculate", font=("Consolas 10 bold"), padx=200, pady=10, command=Calculate)

U1.pack()
U2.pack()
U3.pack()
CALbutton.pack()
fpage.mainloop()
