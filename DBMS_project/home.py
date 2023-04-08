from tkinter import *

master = Tk()
master.geometry("500x150")

def patient():
    master.destroy()
    import patientSide   

def donor():
    master.destroy()
    import donorSide

Label(master,text="CHOOSE TO PROCEED WITH PATEINT SIDE OR DONOR SIDE").place(x=20,y=20)
Button(master,text="PATIENT",command=patient).place(x=130,y=80)
Button(master,text="DONOR",command=donor).place(x=280,y=80)

master.mainloop()
 