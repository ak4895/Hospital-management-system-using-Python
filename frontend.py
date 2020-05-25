'''In a big hospital it would be hard for a receptionist when is doctor opd open and when it is
close, when a patient have appointment and with whom, a patient admitted is in which ward, when
is operation theatre empty and many more management things needed to ease the work of a hospital.'''
import backend
from tkinter import *
r=Tk(screenName="Hospital Management")
w, h = r.winfo_screenwidth(), r.winfo_screenheight()
r.geometry("%dx%d+0+0" % (w, h))
f=Frame(r,width=w,height=h,bg="#181589") #Dark blue
f.propagate(0)
f.pack()

'''l=Label(f,text="Hospital Management System",fg="#F9FE50") #yellow
l.place(x=100,y=150)'''


'''def get_selected_row_A(event):
    global selected_tuple
    index=t.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[6])
'''
'''def get_selected_row_P(event):
    global selected_tuple
    index=t.curselection()[0]
    selected_tuple = t.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
'''






def Doctors():#red

    def get_selected_row_D(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e31.delete(0, END)
        e31.insert(END, selected_tuple[3])
        e32.delete(0, END)
        e32.insert(END, selected_tuple[4])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[5])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[6])

    def add_command():
        #back.insert(name_text.get(), address.get(), phno.get(), purpose.get(), arrival.get(), departure.get())
        backend.AddD(e1.get(), e2.get(), e31.get(),e32.get(), e4.get(), e5.get())
        t.delete(0, END)
        t.insert(END, (e1.get(),e2.get(),e31.get(),e32.get(),e4.get(),e5.get()))

    def delete_command():
        backend.DelD(e6.get())
        #backend.DelD(selected_tuple[0])

    def view_command():
        t.delete(0, END)
        t.insert(END,"Name       Department OPD time from  to  Room no. Phone no.")
        for row in backend.ViewD():
            t.insert(END, str(row))

    r1 = Tk()
    fd = Frame(r1, width=w, height=h, bg="#FEB29F")
    fd.propagate(0)
    fd.pack()

    e1 = StringVar()
    b = StringVar()
    c1 = IntVar()
    c2 = IntVar()
    d = IntVar()
    e = IntVar()
    x = StringVar()
    # Labels
    l1 = Label(fd, text="Name          :")  # 3 tab means 12 spaces after name
    l2 = Label(fd, text="Department      :")
    l31 = Label(fd, text="OPD Timing      :")
    l32 = Label(fd, text="to")
    l4 = Label(fd, text="Room no.        :")
    l5 = Label(fd, text="Phone no.       :")
    # Entry boxes
    e1 = Entry(fd, width=100, textvariable=e1)
    e2 = Entry(fd, width=100, textvariable=b)
    e31 = Entry(fd, width=30, textvariable=c1)
    e32 = Entry(fd, width=30, textvariable=c2)
    e4 = Entry(fd, width=100, textvariable=d)
    e5 = Entry(fd, width=100, textvariable=e)

    # Placing
    l1.place(x=100, y=100)
    l2.place(x=100, y=130)
    l31.place(x=100, y=160)
    l32.place(x=480, y=160)
    l4.place(x=100, y=190)
    l5.place(x=100, y=220)

    e1.place(x=250, y=100)
    e2.place(x=250, y=130)
    e31.place(x=250, y=160)
    e32.place(x=530, y=160)
    e4.place(x=250, y=190)
    e5.place(x=250, y=220)

    B1 = Button(fd, text="Add Entry", command=add_command , relief=RAISED)
    e6 = Entry(fd, width=50, textvariable=x)
    B2 = Button(fd, text="Delete Entry", command= delete_command , relief=RAISED)
    B3 = Button(fd, text="View all", command= view_command, relief=RAISED)
    B1.place(x=200, y=250)
    e6.place(x=300, y=280)
    B2.place(x=200, y=280)
    B3.place(x=200, y=310)

    # for displaying
    t = Listbox(fd, height=100, width=100)
    t.place(x=200, y=350)

    t.bind('<<ListboxSelect>>', get_selected_row_D)


def Appointments():#blue

    def get_selected_row_A(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[5])


    def add_command():
        #back.insert(name_text.get(), address.get(), phno.get(), purpose.get(), arrival.get(), departure.get())
        backend.AddA(e1.get(), e2.get(), e3.get(), e4.get())
        t.delete(0, END)
        t.insert(END, (e1.get(),e2.get(),e3.get(),e4.get()))

    def delete_command():
        backend.DelA(e5.get())
        #backend.DelD(selected_tuple[0])

    def view_command():
        t.delete(0, END)
        t.insert(END,"Name                Doctor           Timing    Phone no.")
        for row in backend.ViewA():
            t.insert(END, str(row))


    r2=Tk()
    fa = Frame(r2, width=w, height=h, bg="#B4F4FE")
    fa.propagate(0)
    fa.pack()

    a = StringVar()
    b = StringVar()
    c = IntVar()
    d = IntVar()

    x=StringVar()
    # Labels
    l1 = Label(fa, text="Patient Name   :")  # 3 tab means 12 spaces after name
    l2 = Label(fa, text="Doctor      :")
    l3 = Label(fa, text="Timing      :")
    l4 = Label(fa, text="Phone no.       :")
    # Entry boxes
    e1 = Entry(fa, width=100,textvariable=a)
    e2 = Entry(fa, width=100,textvariable=b)
    e3 = Entry(fa, width=100,textvariable=c)
    e4 = Entry(fa, width=100,textvariable=d)

    # Placing
    l1.place(x=100, y=100)
    l2.place(x=100, y=130)
    l3.place(x=100, y=160)
    l4.place(x=100, y=190)

    e1.place(x=250, y=100)
    e2.place(x=250, y=130)
    e3.place(x=250, y=160)
    e4.place(x=250, y=190)

    B1 = Button(fa, text="Add Entry", command=add_command, relief=RAISED)
    e5 = Entry(fa, width=50, textvariable=x)
    B2 = Button(fa, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fa, text="View all", command=view_command, relief=RAISED)

    t = Listbox(fa, height=100, width=100)

    B1.place(x=200, y=230)
    e5.place(x=300, y=260)
    B2.place(x=200, y=260)
    B3.place(x=200, y=290)

    t.place(x=200, y=350)

    t.bind('<<ListboxSelect>>', get_selected_row_A)


def Patients():#green

    def get_selected_row_P(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[5])

    def add_command():
        # back.insert(name_text.get(), address.get(), phno.get(), purpose.get(), arrival.get(), departure.get())
        backend.AddP(e1.get(), e2.get(), e3.get(), e4.get())
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e3.get(), e4.get()))
    def delete_command():
        backend.DelP(e5.get())
        # backend.DelD(selected_tuple[0])

    def view_command():
        t.delete(0, END)
        t.insert(END,"Name      Ward no.    Disease     Doctor Incharge")
        for row in backend.ViewP():
            t.insert(END, str(row))

    def view_queryw():
        t.delete(0, END)
        t.insert(END,"Ward no.")
        for row in backend.QueryPw(e6.get()):
            t.insert(END, row)
    def view_queryd():
        t.delete(0, END)
        t.insert(END,"Disease    Doctor Incharge")
        for row in backend.QueryPd(e7.get()):
            t.insert(END, str(row))


    r3=Tk()
    fp = Frame(r3, width=w, height=h, bg="#B1FE7C")
    fp.propagate(0)
    fp.pack()

    a = StringVar()
    b = IntVar()
    c = StringVar()
    d = StringVar()

    x=StringVar()
    # Labels
    l1 = Label(fp, text="Patient Name   :")  # 3 tab means 12 spaces after name
    l2 = Label(fp, text="Ward no.      :")
    l3 = Label(fp, text="Disease      :")
    l4 = Label(fp, text="Doctor Incharge :")
    # Entry boxes
    e1 = Entry(fp, width=100,textvariable=a)
    e2 = Entry(fp, width=100,textvariable=b)
    e3 = Entry(fp, width=100,textvariable=c)
    e4 = Entry(fp, width=100,textvariable=d)

    # Placing
    l1.place(x=100, y=100)
    l2.place(x=100, y=130)
    l3.place(x=100, y=160)
    l4.place(x=100, y=190)

    e1.place(x=250, y=100)
    e2.place(x=250, y=130)
    e3.place(x=250, y=160)
    e4.place(x=250, y=190)

    B1 = Button(fp, text="Add Entry", command=add_command, relief=RAISED)
    e5=Entry(fp,width=50,textvariable=x)
    B2 = Button(fp, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fp, text="View all", command=view_command, relief=RAISED)
    B1.place(x=200, y=230)
    e5.place(x=300,y=260)
    B2.place(x=200, y=260)
    B3.place(x=200, y=290)

    '''2 Queries for this section are What is ward no of patient admitted? 
    And what is Disease and who is Incharge Doctor of patient?(Input is Name of patient)'''
    x=StringVar()
    y=StringVar()
    B4=Button(fp, text="What is Ward no. of patient admitted? Patient name:", command=view_queryw, relief=RAISED)
    B5=Button(fp, text="What is Disease and who is Incharge of Particular Patient? Patient name:", command=view_queryd, relief=RAISED)

    e6=Entry(fp,width=100,textvariable=x)
    e7 = Entry(fp, width=100, textvariable=y)

    B4.place(x=200,y=350)
    e6.place(x=240,y=380)
    B5.place(x=200,y=410)
    e7.place(x=240,y=440)

    # for displaying
    t =Listbox(fp, height=100, width=100)
    t.place(x=200, y=460)

    t.bind('<<ListboxSelect>>',get_selected_row_P)

D=Button(f,text="Doctors",command=Doctors,bd=4,width=30,height=10,bg="#EC7C7A",relief=RAISED,font="Times")#red
A=Button(f,text="Appointments",command=Appointments,bd=4,width=30,height=10,bg="#98F6F6",relief=RAISED,font="Times")#blue
PA=Button(f,text="Patients",command=Patients,bd=4,width=30,height=10,bg="#7AF678",relief=RAISED,font="Times")#green
D.place(x=150,y=300)
A.place(x=600,y=300)
PA.place(x=1050,y=300)

r.mainloop()