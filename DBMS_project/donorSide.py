from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import re

mydb = mysql.connect(
    host='localhost',
    user='root',
    passwd='rootPass',
    database='bdms')

c = mydb.cursor()

bloodGroupDictionary = {
    'A+':'Apos',
    'A-':'Aneg',
    'B+':'Bpos',
    'B-':'Bneg',
    'AB+':'ABpos',
    'AB-':'ABneg',
    'O+':'Opos',
    'O-':'Oneg',
}

bloodGROUPS = ['A+','A-','B+','B-','AB+','AB-','O+','O-']

genders = ['M','F']


# donor side part 1

root = Tk()
root.geometry('700x700')
root.title("DONOR STEP 1")




def insert():
    dName = D1.get()
    dBG = D2.get()
    dPh = D3.get()
    dGen = D4.get()
    dAdd = D5.get()
    dAge = D6.get()



    if (dName and dBG and dPh and dGen and dAdd and dAge):           # check if all entries filled
        if(int(dAge) < 18):
            MessageBox.showinfo("REQUIREMENT","Age of Donor should be more than 18")
        else:
            yesno = MessageBox.askquestion("NOTICE","CONFIRM REGISTRATION ?")
            if yesno == 'yes':
                c.execute(f"insert into donor (DonName,DonBloodType,DonPhno,DonGender,DonAdd,DonAge) values ('{dName}','{dBG}','{dPh}','{dGen}','{dAdd}','{dAge}')")
                c.execute("commit")

                c.execute("select * from donor")
                donortab = c.fetchall()

                MessageBox.showinfo("NOTICE",f"REGISTRATION SUCCESSFULL\nYOUR NEW DONOR ID IS {donortab[-1][0]}")

                D1.delete(0,'end')
                D2.delete(0,'end')
                D3.delete(0,'end')
                D4.delete(0,'end')
                D5.delete(0,'end')
                D6.delete(0,'end')
            
    else:
        MessageBox.showinfo("ERROR","ENTER ALL DETAILS FOR REGISTRATION !")


yesno = MessageBox.askquestion("READ","ARE YOU ALREADY REGISTERED AS A DONOR ?")
if yesno == 'yes':
    root.destroy()
else:
    Label(root,text="NAME: ").place(x=20,y=20)
    Label(root,text="BLOOD TYPE: ").place(x=20,y=50)
    Label(root,text="Phone No: ").place(x=20,y=80)
    Label(root,text="Gender: ").place(x=20,y=110)
    Label(root,text="Address: ").place(x=20,y=140)
    Label(root,text="Age: ").place(x=20,y=170)


    D1 = Entry()                                    #name
    D1.place(x=200,y=20)

    D2 = ttk.Combobox(root,values=bloodGROUPS)      # blood group
    D2.place(x=200,y=50)

    D3 = Entry()                                    # phone
    D3.place(x=200,y=80)

    D4 = ttk.Combobox(root,values=genders)          # gender
    D4.place(x=200,y=110)

    D5 = Entry()                                    # Address
    D5.place(x=200,y=140)

    D6 = Entry()                                    # Age
    D6.place(x=200,y=170)

    insert = Button(root,text="REGISTER AS DONOR",command=insert).place(x=150,y=250)

root.mainloop()









# step 2 

root2 = Tk()
root2.geometry('700x500')
root2.title("DONOR STEP 2")

c.execute("select * from donor")
donList = c.fetchall()
DONIDD = []
for i in donList:
    DONIDD.append(i[0])


def fetching_dddd():
    global donor_id
    global donor_blood_g
    global destroy_later_2
    global destroy_later_3

    donor_id = chooID.get()
    c.execute(f"select DonName from donor where DonId = {donor_id}")
    donor_name = c.fetchall()
    destroy_later_2 = Label(root2,text=f"Your name is {donor_name[0][0]}")
    destroy_later_2.place(x=20,y=50)

    c.execute(f"select DonBloodType from donor where DonId = {donor_id}")
    donor_blood_g = c.fetchall()            #use donor_blood_g[0][0]
    destroy_later_3 = Label(root2,text=f"Your Blood Group is {donor_blood_g[0][0]}")
    destroy_later_3.place(x=200,y=50)

Label(root2,text="Select Donor ID: ").place(x=20,y=20)
destroy_later_1 = chooID = ttk.Combobox(root2,values=DONIDD)
chooID.place(x=150,y=20)
button1 = Button(root2,text="FETCH",command=fetching_dddd).place(x=400,y=20)








c.execute("select * from BloodBank")
bblist = c.fetchall()
bb_names = []
for i in bblist:
    bb_names.append(i[1])


c.execute("select * from doctor")
docList = c.fetchall()
doc_Id_name=[]
for i in docList:
    doc_Id_name.append(f"ID: {i[0]}  Dr.{i[1]}")


def donate():
    # check for entered all details


    doctorID = choo_doc.get()
    bbname = choo_bb_name.get()

    if (doctorID and bbname):
        
        x = re.search(' (.*) ',doctorID)
        doctorID = x.group(1)

        c.execute(f"select BB_Id from BloodBank where BB_name = '{bbname}'")
        bloodbankID = c.fetchall()          #use bloodbankID[0][0]

        yesno = MessageBox.askquestion("READ","ARE YOU SURE ?")
        if yesno == 'yes':
            try:
                c.execute(f"insert into examineandstore (DocId,DonId,BB_Id,eventDate) values ({doctorID},{donor_id},{bloodbankID[0][0]},{'curdate()'})")
                c.execute("commit")

                c.execute(f"update storage set {bloodGroupDictionary[donor_blood_g[0][0]]} = {bloodGroupDictionary[donor_blood_g[0][0]]} + 1 where BB_Id = {bloodbankID[0][0]}")
                c.execute("commit")

                MessageBox.showinfo("SUCCESSFULL",F"YOUR {donor_blood_g[0][0]} BLOOD IS DONATED AT\nBLOOD BANK {bbname}")

            except mysql.errors.IntegrityError:
                MessageBox.showinfo("ERROR","YOU CANNOT DONATE BLOOD TODAY AGAIN")
        
            choo_doc.delete(0,'end')
            choo_bb_name.delete(0,'end')
            destroy_later_2.destroy()
            destroy_later_3.destroy()
            destroy_later_1.delete(0,'end')

    else:
        MessageBox.showinfo("ERROR","PLEASE ENTER ALL DETAIL !")



Label(root2,text="Select Doctor that took Blood:").place(x=20,y=150)
choo_doc = ttk.Combobox(root2,values=doc_Id_name)
choo_doc.place(x=250,y=150)

Label(root2,text="Select Blood Bank:").place(x=20,y=200)
choo_bb_name = ttk.Combobox(root2,values=bb_names)
choo_bb_name.place(x=190,y=200)

deposit = Button(root2,text="DONATE",command=donate).place(x=50,y=250)








root2.mainloop()