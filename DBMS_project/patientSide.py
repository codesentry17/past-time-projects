from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox


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
# part 1 of Patient :


root = Tk()
root.title("PATIENT STEP 1")
root.geometry('700x700')


def insert():
    p1 = PNAME.get()
    p2 = PPHONE.get()
    p3 = PADDRESS.get()
    p4 = PBLOOD.get()

    
    if (p1 and p2 and p3 and p4):
        yesno = MessageBox.askquestion("CONFIRMATION","ARE YOU SURE ?")
        if yesno=='yes':
            c.execute(f"insert into patient (PaName,PaPhno,PaAdd,PaBloodType) values ('{p1}',{p2},'{p3}','{p4}') ")
            c.execute("commit")

            c.execute("select * from patient")
            x = c.fetchall()
            MessageBox.showinfo("NOTICE",f"REGISTRATION SUCCESSFUL\nYOUR PATIENT ID IS {x[-1][0]}\nTHANK YOU")
            PNAME.delete(0,'end')
            PPHONE.delete(0,'end')
            PADDRESS.delete(0,'end')
            PBLOOD.delete(0,'end')

    else:
            MessageBox.showinfo("ERROR","ALL DETAILS NEED TO BE FILLED !!")


alreadyRegistered = MessageBox.askquestion("READ","ARE YOU ALREADY REGISTERED AS A PATIENT ?") 
if alreadyRegistered == 'yes':
    root.destroy()
else:
    Label(root,text="Name: ").place(x=20,y=20)
    Label(root,text="Phone No: ").place(x=20,y=50)
    Label(root,text="Address: ").place(x=20,y=80)
    Label(root,text="BLOOD GROUP: ").place(x=20,y=110)

    PNAME = Entry()
    PNAME.place(x=180,y=20)

    PPHONE = Entry()
    PPHONE.place(x=180,y=50)

    PADDRESS = Entry()
    PADDRESS.place(x=180,y=80)

    PBLOOD = ttk.Combobox(root,values=bloodGROUPS)
    PBLOOD.place(x=180,y=110)

    PBUTTON = Button(root,text="ENTER CREDENTIALS",command=insert).place(x=100,y=200)

root.mainloop()




# part 2 of Patient is SUCCESSFULLY DONE : )


root2 = Tk()
root2.geometry("700x400")
root2.title("PATIENT STEP 2")



c.execute("select * from Patient")
pa_list = c.fetchall()
pa_name = []
for i in pa_list:
    pa_name.append(i[0])


# storing PaId and showing him his name and blood group
def fetching_paaa():
    global paID
    global dest1,dest2
    paID = e_choo_ID.get()

    c.execute(f"select PaName from patient where PaId = {paID}")
    pa_name = c.fetchall()
    dest1 = Label(root2,text=f"Your name is {pa_name[0][0]}")
    dest1.place(x=20,y=50)      # destroy Label after successful

    c.execute(f"select PaBloodType from patient where PaId = {paID}")
    pa_blood_typeeee = c.fetchall()
    dest2 = Label(root2,text=f"Your blood type is {pa_blood_typeeee[0][0]}")
    dest2.place(x=200,y=50)  #destroy Label after successful


# taking in PaId and confirming Patient his name 
Label(root2,text="Select Patient ID").place(x=20,y=20)
e_choo_ID = ttk.Combobox(root2,values=pa_name)
e_choo_ID.place(x=200,y=20)
fetch_pa = Button(root2,text="FETCH INFO",command=fetching_paaa).place(x=450,y=20)










c.execute("Select * from BloodBank");
bb_list = c.fetchall()
bb_name_list = []
for i in bb_list:
    bb_name_list.append(i[1])



# getting bb_Id from selected bloodbank and getting details if blooddelivery is possible; if blood of patient's blood group is more than 1
def fetching_bbbb():
    
    c.execute(f"Select PaBloodType from Patient where PaId = '{paID}'")
    PATIENTBLOODTYPE = c.fetchall()     #use value = PATIENTBLOODTYPE[0][0]

    bb_NAME = e_choo_BB.get()
    c.execute(f"select BB_id from bloodBank where BB_Name = '{bb_NAME}'")
    global bb_ID_haha
    bb_ID_haha = c.fetchall()           #use value = bb_ID_haha[0][0]


    c.execute(f"Select {bloodGroupDictionary[PATIENTBLOODTYPE[0][0]]} from storage where BB_Id = '{bb_ID_haha[0][0]}'")     
    bb_count = c.fetchall()

    yesno = MessageBox.askquestion("Alert","Do you want to proceed ?")
    if yesno == 'yes':
        try:
        #critical condition check
            if(bb_count[0][0]==0):                  # if no blood of required blood group
                MessageBox.showinfo("SORRY",f"NO {PATIENTBLOODTYPE[0][0]} BLOOD LEFT IN {bb_NAME}\nCHOOSE ANOTHER BLOODBANK")

            else:                                   # if blood available of required blood group
                c.execute(f"update storage set {bloodGroupDictionary[PATIENTBLOODTYPE[0][0]]} = {bloodGroupDictionary[PATIENTBLOODTYPE[0][0]]} - 1 where BB_Id = {bb_ID_haha[0][0]}")
                c.execute("commit")
                c.execute(f"insert into blooddelivery (BB_Id,PaId,BD_Date) values ({bb_ID_haha[0][0]},{paID},{'curdate()'})")
                c.execute("commit")
                MessageBox.showinfo("SUCCESSFULL",f"{PATIENTBLOODTYPE[0][0]} BLOOD WILL BE DELIVERING SOON\nFROM {bb_NAME}")    

                e_choo_ID.delete(0,'end')
                e_choo_BB.delete(0,'end')
                dest1.destroy()
                dest2.destroy()

        except mysql.errors.IntegrityError:
            MessageBox.showinfo("ERROR","You just asked for Blood")

# making the patient select his blood bank name
Label(root2,text="Select BloodBank").place(x=20,y=100)
e_choo_BB = ttk.Combobox(root2,values=bb_name_list)
e_choo_BB.place(x=200,y=100)
fetch_bb = Button(root2,text="ASK FOR BLOOD",command=fetching_bbbb).place(x=100,y=150)


root2.mainloop()
