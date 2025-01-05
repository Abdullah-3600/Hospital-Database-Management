from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import employee_registration_ui
import pymysql
import doctor_ui
import nurse_ui
import receptionist_ui
import admin_ui


class Login_UI:
    def __init__(self,window):
        self.login_ui=window
        self.login_ui.geometry('500x500')
        self.login_ui.title('LOGIN USER INTERFACE')
        self.login_ui.resizable(FALSE,FALSE)
        self.login_ui.config(bg='light blue')
        self.radio=IntVar()
        self.name=StringVar()
        self.id=StringVar()
        self.password=StringVar()
        login_title=Label(self.login_ui,text='WELCOME TO LOGIN INTERFACE', bg='light blue',font=('Times New Roman',20,'bold')).pack()
        self.login_frame1=LabelFrame(self.login_ui,text='Login As',borderwidth=3.5,height=60,width=480,bg='light blue').place(x=10,y=90)
        Radiobutton(self.login_frame1, text='DOCTOR', variable=self.radio, value=1,bg='light blue').place(x=20, y=110)
        Radiobutton(self.login_frame1, text='NURSE', variable=self.radio, value=2,bg='light blue').place(x=140, y=110)
        Radiobutton(self.login_frame1, text='RECEPTIONIST', variable=self.radio, value=3,bg='light blue').place(x=250, y=110)
        Radiobutton(self.login_frame1,text='ADMIN',variable=self.radio,value=4,bg='light blue').place(x=390,y=110)
        name_label=Label(self.login_ui,text='Enter Name       :',font=('Times New Roman',15,'bold'),bg='light blue').place(x=10,y=200)
        id_label=Label(self.login_ui,text='Enter ID            :',font=('Times New Roman',15,'bold'),bg='light blue').place(x=10,y=260)
        passw_label=Label(self.login_ui,text='Enter Password :',font=('Times New Roman',15,'bold'),bg='light blue').place(x=10,y=320)
        name_entry=Entry(self.login_ui,font=('Times New Roman',15,'bold'),textvariable=self.name)
        name_entry.place(x=200,y=200)
        id_entry=Entry(self.login_ui,font=('Times New Roman',15,'bold'),textvariable=self.id)
        id_entry.place(x=200,y=260)
        passw_entry=Entry(self.login_ui,font=('Times New Roman',15,'bold'),textvariable=self.password,show='*')
        passw_entry.place(x=200,y=320)
        login_button=Button(self.login_ui,text='LOGIN',font=('Times New Roman',12,'bold'),bg='pink',command=self.login)
        login_button.place(x=330,y=420)
        new_account_button=Button(self.login_ui,text='CREATE NEW USER ACCOUNT',font=('Times New Roman',12,'bold'),bg='pink',command=self.new_acc)
        new_account_button.place(x=20,y=420)

    def login(self):
        if self.radio.get()==1:
            con = pymysql.connect(host='localhost', user='root', password='',database='hospital_management')
            mycursor = con.cursor()
            query='select * from doctor_registration_table where ID=%s and name =%s and password=%s'
            mycursor.execute(query,(self.id.get(),self.name.get(),self.password.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Invalid Login','Invalid Entry. Please try again.')
            else:
                self.login_ui.destroy()
                d_ui=Tk()
                doc_ui=doctor_ui.Doctor_UI(d_ui)
                d_ui.mainloop()
        elif self.radio.get()==2:
            con = pymysql.connect(host='localhost', user='root', password='',database='hospital_management')
            mycursor = con.cursor()
            query = 'select * from nurse_registration_table where ID=%s and name =%s and password=%s'
            mycursor.execute(query, (self.id.get(), self.name.get(), self.password.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Invalid Login', 'Invalid Entry. Please try again.')
            else:
                self.login_ui.destroy()
                n_ui = Tk()
                nur_ui = nurse_ui.NURSE_UI(n_ui,self.id.get(),self.name.get())
                n_ui.mainloop()

        elif self.radio.get()==3:
            con = pymysql.connect(host='localhost', user='root', password='',database='hospital_management')
            mycursor = con.cursor()
            query = 'select * from admin_receptionist_table where ID=%s and name =%s and password=%s and register_as=%s'
            mycursor.execute(query, (self.id.get(), self.name.get(), self.password.get(),'RECEPTIONIST'))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Invalid Login', 'Invalid Entry. Please try again.')
            else:
                self.login_ui.destroy()
                rec_ui = Tk()
                recept_ui = receptionist_ui.RECEPTIONIST_UI(rec_ui)
                rec_ui.mainloop()

        elif self.radio.get()==4:
            con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
            mycursor = con.cursor()
            query = 'select * from admin_receptionist_table where ID=%s and name =%s and password=%s and register_as=ADMIN'
            mycursor.execute(query, (self.id.get(), self.name.get(), self.password.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Invalid Login', 'Invalid Entry. Please try again.')
            else:
                self.login_ui.destroy()
                ad_ui = Tk()
                adm_ui = admin_ui.Admin_UI(ad_ui)
                ad_ui.mainloop()



    def new_acc(self):
        self.login_ui.destroy()
        window1 = Tk()
        new_account = employee_registration_ui.Employee_Registration_UI(window1)
        window1.mainloop()

hospital_app=Tk()
login=Login_UI(hospital_app)
hospital_app.mainloop()