from tkinter import *
from tkinter import filedialog
import pandas as pd
from qr import createqr


 
def openFile():
    filepath= filedialog.askopenfilename()
    df = pd.read_excel (filepath)

    list  = df.values.tolist()
    for i in range(len(list)):
        id = list[i][0]
        name = list[i][1]
        phonenumber = list[i][2]
        email = list[i][3]
        guestcount = list[i][4]
        createqr(id,name,phonenumber,email)
    


root = Tk()
root.title("Hepevento")
root.geometry('350x200')
lbl = Label(root, text = "Choose your excel file")
lbl.place(relx=0.5, rely=0.3, anchor=CENTER)
btn = Button(root, text = "Choose file" ,
             fg = "black", command=openFile)


btn.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()