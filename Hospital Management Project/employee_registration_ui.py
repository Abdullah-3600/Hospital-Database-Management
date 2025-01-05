from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pymysql


class Employee_Registration_UI:
    def __init__(self,window):
        self.employee_regi_ui=window
        self.employee_regi_ui.geometry('800x650')
        self.employee_regi_ui.title('Employee Registration UI')
        self.employee_regi_ui.resizable(FALSE,FALSE)
        self.id=str(random.randint(0000,9999))

        self.option_frame=Frame(self.employee_regi_ui,bg='light green')
        self.option_frame.pack()
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=800,height=150)

        self.main_frame=Frame(self.employee_regi_ui,highlightbackground='green',highlightthickness=2,bg='#b2f338')
        self.main_frame.pack()
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500,width=800)
        title_label=Label(self.option_frame,text='EMPLOYEE REGISTRATION UI',font=('Times New Roman',20,'bold'),bg='light green').pack()
        admin_regi_btn=Button(self.option_frame,text='Register as Admin / Receptionist',font=('Times New Roman',15,'bold'),bg='light green',command=lambda :self.indicate(self.admin_indicate,self.admin_recep_regi_ui)).place(x=5,y=90)
        doc_regi_btn=Button(self.option_frame,text='Register as Doctor',font=('Times New Roman',15,'bold'),bg='light green',command=lambda :self.indicate(self.doc_indicate,self.doc_regi_ui)).place(x=350,y=90)
        nurse_regi_btn=Button(self.option_frame,text='Register as Nurse',font=('Times New Roman',15,'bold'),bg='light green',command=lambda :self.indicate(self.nurse_indicate,self.nurse_regi_ui)).place(x=600,y=90)

        self.admin_indicate = Label(self.option_frame, text='', bg='light green')
        self.admin_indicate.place(x=5, y=85, width=296, height=5)
        self.doc_indicate=Label(self.option_frame, text='', bg='light green')
        self.doc_indicate.place(x=350, y=85, width=172, height=5)
        self.nurse_indicate=Label(self.option_frame, text='', bg='light green')
        self.nurse_indicate.place(x=600, y=85, width=167, height=5)

    def indicate(self,lb,page):
        self.hide_indicators()
        lb.config(bg='yellow')
        self.delete_frames()
        page()

    def hide_indicators(self):
        self.admin_indicate.config(bg='light green')
        self.doc_indicate.config(bg='light green')
        self.nurse_indicate.config(bg='light green')

    def delete_frames(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()
    def admin_recep_regi_ui(self):


        def register():
            if name_entry.get()=='' or age_entry.get()==None or phone_entry.get()=='' or register_as.get()=='' or password_entry.get()=='':
                messagebox.showerror('Registration Error','Please fill all the information above')
            elif len(str(phone_entry))==11 :
                messagebox.showerror('Registration Error', 'Invalid Phone number. ')
            else:
                con = pymysql.connect(host='localhost', user='root', password='')
                mycursor = con.cursor()
                query = 'create database if not exists hospital_management'
                mycursor.execute(query)
                query='use hospital_management'
                mycursor.execute(query)
                query = 'create table if not exists admin_receptionist_table(ID varchar(4) primary key,name varchar(30),phone varchar(11),age int,register_as varchar(12),password varchar(10))'
                mycursor.execute(query)
                query='insert into admin_receptionist_table(ID,name,phone,age,register_as,password) values(%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.id,name_entry.get(),phone_entry.get(),age_entry.get(),register_as.get(),password_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Employee Registration', 'Employee has been successfully registered.')
                self.employee_regi_ui.destroy()
        title_label=Label(self.main_frame,text='ADMIN / RECEPTIONIST REGISTRATION UI',font=('Times New Roman',20,'bold'),bg='#b2f338').pack()
        id_label=Label(self.main_frame,text='ID :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=5,y=100)
        name_label=Label(self.main_frame,text='ENTER NAME :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=5,y=150)
        age_label=Label(self.main_frame,text='ENTER AGE :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=5,y=200)
        phone_label=Label(self.main_frame,text='ENTER PHONE :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=5,y=250)
        register_as_label=Label(self.main_frame,text='REGISTER AS :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=5,y=300)
        id_label2=Label(self.main_frame,text=self.id,font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=200,y=100)
        password_label=Label(self.main_frame,text='Enter Password :',font=('Times New Roman',15,'bold'),bg='#b2f338').place(x=410,y=100)
        name_entry=Entry(self.main_frame,width=20,font=('Times New Roman',15,'bold'))
        name_entry.place(x=200,y=150)
        age_entry=Entry(self.main_frame,width=20,font=('Times New Roman',15,'bold'))
        age_entry.place(x=200,y=200)
        phone_entry=Entry(self.main_frame,width=20,font=('Times New Roman',15,'bold'))
        phone_entry.place(x=200,y=250)
        password_entry = Entry(self.main_frame, width=17, font=('Times New Roman', 15, 'bold'))
        password_entry.place(x=560, y=100)

        register_as=ttk.Combobox(self.main_frame,font=('Times New Roman',15,'bold'),value=['ADMIN','RECEPTIONIST'])
        register_as['state']='readonly'
        register_as.place(x=200,y=300)
        register_btn=Button(self.main_frame,text='REGISTER NEW ACCOUNT',font=('Times New Roman',15,'bold'),command=register)
        register_btn.place(x=250,y=400)


    def doc_regi_ui(self):
        def register():
            if name_entry.get()=='' or age_entry.get()==None or phone_entry.get()=='' or specialized_in.get()=='' or password_entry.get=='':
                messagebox.showerror('Registration Error','Please fill all the information above')
            elif len(str(phone_entry))==11 :
                messagebox.showerror('Registration Error', 'Invalid Phone number. ')
            else:
                con = pymysql.connect(host='localhost', user='root', password='')
                mycursor = con.cursor()
                query = 'create database if not exists hospital_management'
                mycursor.execute(query)
                query='use hospital_management'
                mycursor.execute(query)
                query = 'create table if not exists doctor_registration_table(ID varchar(4) primary key,name varchar(30),phone varchar(11),age int,specialized_in varchar(15),chamber_no varchar(4) null)'
                mycursor.execute(query)
                query='insert into doctor_registration_table(ID,name,phone,age,specialized_in,chamber_no,password) values(%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.id,name_entry.get(),phone_entry.get(),age_entry.get(),specialized_in.get(),'NULL',password_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Doctor Registration', 'Doctor has been successfully registered.')
                self.employee_regi_ui.destroy()

        title_label = Label(self.main_frame, text='DOCTOR REGISTRATION UI',font=('Times New Roman', 20, 'bold'),bg='#b2f338').pack()
        id_label = Label(self.main_frame, text='ID :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=100)
        password_label = Label(self.main_frame, text='Enter Password :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(
            x=410, y=100)
        name_label = Label(self.main_frame, text='ENTER NAME :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=150)
        age_label = Label(self.main_frame, text='ENTER AGE :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=200)
        phone_label = Label(self.main_frame, text='ENTER PHONE :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5,y=250)
        register_as_label = Label(self.main_frame, text='SPECIALIZATION :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=300)
        id_label2 = Label(self.main_frame, text=self.id, font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=200, y=100)
        name_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        name_entry.place(x=200, y=150)
        age_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        age_entry.place(x=200, y=200)
        password_entry = Entry(self.main_frame, width=17, font=('Times New Roman', 15, 'bold'))
        password_entry.place(x=560, y=100)
        phone_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        phone_entry.place(x=200, y=250)
        specialized_in = ttk.Combobox(self.main_frame, font=('Times New Roman', 15, 'bold'),value=['ENT', 'NEPHROLOGIST','NEUROLOGIST','GENERAL MEDICINE','CARDIOLOGIST'])
        specialized_in['state'] = 'readonly'
        specialized_in.place(x=200, y=300)
        register_btn = Button(self.main_frame, text='REGISTER NEW ACCOUNT', font=('Times New Roman', 15, 'bold'),command=register)
        register_btn.place(x=250, y=400)
        

    def nurse_regi_ui(self):
        def register():
            if name_entry.get() == '' or age_entry.get() == None or phone_entry.get() == '' or nurse_type.get() == '' or password_entry.get=='':
                messagebox.showerror('Registration Error', 'Please fill all the information above')
            elif len(str(phone_entry)) == 11:
                messagebox.showerror('Registration Error', 'Invalid Phone number. ')
            else:
                con = pymysql.connect(host='localhost', user='root', password='')
                mycursor = con.cursor()
                query = 'create database if not exists hospital_management'
                mycursor.execute(query)
                query = 'use hospital_management'
                mycursor.execute(query)
                query = 'create table if not exists nurse_registration_table(ID varchar(4) primary key,name varchar(30),phone varchar(11),age int,nurse_type varchar(14),doctor_id varchar(4) null, supervisor_id varchar(4) null, assigned_room varchar(4) null)'
                mycursor.execute(query)
                query = 'insert into nurse_registration_table(ID,name,phone,age,nurse_type,doctor_id,supervisor_id,assigned_room,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (self.id, name_entry.get(), phone_entry.get(), age_entry.get(), nurse_type.get(), 'NULL','NULL','NULL',password_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Nurse Registration', 'Nurse has been successfully registered.')
                self.employee_regi_ui.destroy()
        title_label=Label(self.main_frame,text='NURSE REGISTRATION UI',font=('Times New Roman',20,'bold'),bg='#b2f338').pack()
        id_label = Label(self.main_frame, text='ID :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=100)
        password_label = Label(self.main_frame, text='Enter Password :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(
            x=410, y=100)
        name_label = Label(self.main_frame, text='ENTER NAME :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=150)
        age_label = Label(self.main_frame, text='ENTER AGE :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=200)
        phone_label = Label(self.main_frame, text='ENTER PHONE :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5,y=250)
        nurse_type_label = Label(self.main_frame, text='NURSE TYPE :', font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=5, y=300)
        id_label2 = Label(self.main_frame, text=self.id, font=('Times New Roman', 15, 'bold'),bg='#b2f338').place(x=200, y=100)
        name_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        name_entry.place(x=200, y=150)
        age_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        age_entry.place(x=200, y=200)
        phone_entry = Entry(self.main_frame, width=20, font=('Times New Roman', 15, 'bold'))
        phone_entry.place(x=200, y=250)
        password_entry=Entry(self.main_frame,width=17,font=('Times New Roman',15,'bold'))
        password_entry.place(x=560,y=100)
        nurse_type = ttk.Combobox(self.main_frame, font=('Times New Roman', 15, 'bold'),value=['OT','GENERAL WARD'])
        nurse_type['state'] = 'readonly'
        nurse_type.place(x=200, y=300)
        register_btn = Button(self.main_frame, text='REGISTER NEW ACCOUNT', font=('Times New Roman', 15, 'bold'),command=register)
        register_btn.place(x=250, y=400)







