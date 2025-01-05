from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class NURSE_UI:
    def __init__(self,window,id,name):
        self.nurse_ui=window
        self.nurse_ui.geometry('500x400')
        self.nurse_ui.resizable(FALSE,FALSE)
        self.nurse_ui.title('Nurse User Interface')
        self.id=id
        self.name=name
        self.supervisor=''
        self.room=''
        self.doctor=''
        self.type=''
        self.view()
        title_label=Label(self.nurse_ui,text='MY INFORMATION',font=('Times New Roman',20,'bold')).pack()
        name_label=Label(self.nurse_ui,text='Name :',font=('Times New Roman',13,'bold')).place(x=5,y=100)
        id_label=Label(self.nurse_ui,text='ID :',font=('Times New Roman',13,'bold')).place(x=5,y=150)
        type_label=Label(self.nurse_ui,text='Type :',font=('Times New Roman',13,'bold')).place(x=5,y=200)
        supervisor_label=Label(self.nurse_ui,text='Assigned Supervisor :',font=('Times New Roman',13,'bold')).place(x=5,y=250)
        assigned_room_label=Label(self.nurse_ui,text='Assigned Room :',font=('Times New Roman',13,'bold')).place(x=5,y=300)
        assigned_doctor_label=Label(self.nurse_ui,text='Assigned Doctor :',font=('Times New Roman',13,'bold')).place(x=5,y=350)
        name_label2=Label(self.nurse_ui,text=self.name,font=('Times New Roman',13,'bold')).place(x=200,y=100)
        id_label2=Label(self.nurse_ui,text=self.id,font=('Times New Roman',13,'bold')).place(x=200,y=150)
        type_label2=Label(self.nurse_ui,text=self.type,font=('Times New Roman',13,'bold')).place(x=200,y=200)
        supervisor_label2=Label(self.nurse_ui,text=self.supervisor,font=('Times New Roman',13,'bold')).place(x=200,y=250)
        assigned_room_label2=Label(self.nurse_ui,text=self.room,font=('Times New Roman',13,'bold')).place(x=200,y=300)
        assigned_doctor_label2=Label(self.nurse_ui,text=self.doctor,font=('Times New Roman',13,'bold')).place(x=200,y=350)

    def view(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
        mycursor=con.cursor()
        query='select doctor_id, supervisor_id, assigned_room ,nurse_type from nurse_registration_table where id=%s and name=%s '
        mycursor.execute(query,(self.id,self.name))
        row=mycursor.fetchone()
        self.doctor=row[0]
        self.supervisor=row[1]
        self.room=row[2]
        self.type=row[3]

        con.commit()
        con.close()

