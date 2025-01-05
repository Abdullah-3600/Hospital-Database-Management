from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime

class RECEPTIONIST_UI:
    def __init__(self,window):
        self.patient_id=self.new_id_creation()
        self.receptionist_ui=window
        self.receptionist_ui.geometry('800x600')
        self.options_frame = Frame(self.receptionist_ui, bg='pink')
        self.options_frame.pack(side=LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=200, height=600)
        self.main_frame = Frame(self.receptionist_ui, bg='light green')
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=600, width=600)
        patient_regi_btn=Button(self.options_frame,text='Patient Registration',font=('Times New Roman',15,'bold'),bg='light blue',command=self.patient_register)
        patient_regi_btn.place(x=5,y=200)
        edit_patient_btn=Button(self.options_frame,text='Edit Patient Details',font=('Times New Roman',15,'bold'),bg='light blue',command=self.edit_patient)
        edit_patient_btn.place(x=5,y=400)
    def delete_frames(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()
    def new_id_creation(self):
        con = pymysql.connect(host='localhost', user='root', password='')
        mycursor = con.cursor()
        mycursor.execute('use hospital_management')
        query = 'create table if not exists patient_registration_table(ID varchar(9),Name varchar(20),Age char(2),Phone varchar(11),Issues varchar(100),Doctor varchar(20))'
        mycursor.execute(query)
        query = 'SELECT MAX(ID) FROM patient_registration_table'
        mycursor.execute(query)
        row = mycursor.fetchone()

        if row[0] == None:
            return'1'
        else:
            return str(int(row[0]) + 1)
        con.close()

    def patient_register(self):
        doctor_lists=[]
        age = IntVar()
        def doctor_list():

            con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
            mycursor=con.cursor()
            query='select name from doctor_registration_table'
            mycursor.execute(query)
            row=mycursor.fetchall()
            for i in row:
                doctor_lists.append(i)
            con.close()

        def register():

            if type(age.get())!=int:
                messagebox.showerror('error','Age entry must be number')
            if name_entry.get()=='' or age.get()==0 or phone_entry.get()=='' or select_doctor.get()=='' or issues_entry.get()=='':
                messagebox.showerror('error','Fill all the blanks. Age must be greater than 0')
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
                mycursor=con.cursor()
                query='create table if not exists patient_registration_table(ID varchar(9),Name varchar(20),Age char(2),Phone varchar(11),Issues varchar(100),Doctor varchar(20))'
                mycursor.execute(query)

                query='insert into patient_registration_table(ID,Name,Age,Phone,Issues,Doctor) values (%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.patient_id,name_entry.get(),age.get(),phone_entry.get(),issues_entry.get(),select_doctor.get()))
                query = 'create table if not exists doctor_patient_treatment(Patient_ID varchar(4),Patient_Name varchar(20),Doctor_Name varchar(20),Date Date)'
                mycursor.execute(query)
                query='insert into doctor_patient_treatment(Patient_ID,Patient_Name, Doctor_Name, Date) values(%s,%s,%s,%s)'
                mycursor.execute(query,(self.patient_id,name_entry.get(),select_doctor.get(),datetime.today().date()))
                con.commit()
                con.close()
                messagebox.showinfo('Patient Registration','Patient has been successfully registered')

        self.delete_frames()
        doctor_list()

        title_label=Label(self.main_frame,text='Patient Registration UI',font=('Times New Roman',15,'bold'),bg='light green').pack()
        id_label=Label(self.main_frame,text='Patient ID:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=100)
        id_label2=Label(self.main_frame,text=self.patient_id,font=('Times New Roman',15,'bold'),bg='light green').place(x=200,y=100)
        name_label=Label(self.main_frame,text='Patient Name:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=150)
        age_label=Label(self.main_frame,text='Patient Age:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=200)
        phone_label=Label(self.main_frame,text='Patient Phone:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=250)
        issues_label=Label(self.main_frame,text='Patient Issues:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=300)
        doctor_label=Label(self.main_frame,text='Doctor Appointment:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=350)
        name_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        name_entry.place(x=200,y=150)
        age_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25,textvariable=age)
        age_entry.place(x=200,y=200)
        phone_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        phone_entry.place(x=200,y=250)
        issues_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        issues_entry.place(x=200,y=300)
        select_doctor=ttk.Combobox(self.main_frame,font=('Times New Roman',15,'bold'),values=doctor_lists)
        select_doctor['state']='readonly'
        select_doctor.place(x=200,y=350)
        register_btn=Button(self.main_frame,text='Register New Patient',font=('Times New Roman',15,'bold'),command=register)
        register_btn.place(x=200,y=450)

    def edit_patient(self):
        self.delete_frames()
        def view_all():
            con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
            mycursor = con.cursor()
            query = 'create table if not exists doctor_patient_treatment(Patient_ID varchar(4),Patient_Name varchar(20),Doctor_Name varchar(20),Date Date)'
            mycursor.execute(query)
            # Query to fetch all data or apply condition based on search criteria
            query = 'SELECT * FROM doctor_patient_treatment'
            mycursor.execute(query)
            data = mycursor.fetchall()

            # Clear existing treeview entries
            for row in treeview.get_children():
                treeview.delete(row)

            # Populate the treeview with fetched data
            for row in data:
                treeview.insert('', 'end', values=row)

            con.close()
        def delete_patient_data():
            selected_patient=treeview.selection()
            for patient in selected_patient:
                current_patient=treeview.item(patient)
                print(current_patient['values'][0])
            try:
                con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
                mycursor = con.cursor()

                # Delete the record based on Patient ID
                query = "DELETE FROM doctor_patient_treatment WHERE Patient_ID = %s"
                mycursor.execute(query,current_patient['values'][0])

                query = "DELETE FROM patient_registration_table WHERE ID = %s"
                mycursor.execute(query, current_patient['values'][0])
                con.commit()
                # Notify the user and refresh the data
                messagebox.showinfo("Success", "Record deleted successfully!")


                con.close()
            except Exception as e:
                messagebox.showerror('Error', f"Error deleting record: {e}")
        def search_by_name():
            con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
            mycursor = con.cursor()
            query = 'create table if not exists doctor_patient_treatment(Patient_ID varchar(4),Patient_Name varchar(20),Doctor_Name varchar(20),Date Date)'
            mycursor.execute(query)
            # Query to fetch all data or apply condition based on search criteria
            query = 'SELECT * FROM doctor_patient_treatment where Patient_Name=%s'
            mycursor.execute(query,name_entry.get())
            data = mycursor.fetchall()

            # Clear existing treeview entries
            for row in treeview.get_children():
                treeview.delete(row)

            # Populate the treeview with fetched data
            for row in data:
                treeview.insert('', 'end', values=row)

            con.close()


        title_label=Label(self.main_frame,text='Edit Patient Details',font=("Times New Roman",15,'bold'),bg='light green').pack()
        patient_details_frame = Frame(self.main_frame, bg='light blue')
        #frame to hold treeview
        patient_details_frame.pack()
        patient_details_frame.pack_propagate(False)
        patient_details_frame.configure(width=800, height=300)
        treeview = ttk.Treeview(patient_details_frame,
                                     columns=('Patient ID', 'Patient Name', 'Doctor Name', 'Date'), show='headings')
        treeview.pack(fill=BOTH, expand=True)

        treeview.heading('Patient ID', text='Patient ID')
        treeview.heading('Patient Name', text='Patient Name')
        treeview.heading('Doctor Name', text='Doctor Name')
        treeview.heading('Date', text='Date')

        name_entry=Entry(self.main_frame,width=20)
        name_entry.place(x=5,y=410)
        search_btn1 = Button(self.main_frame, text='Search By Name',command=search_by_name)
        search_btn1.place(x=200, y=410)
        view_all_btn=Button(self.main_frame,text='View All Patient Details',command=view_all)
        view_all_btn.place(x=200,y=370)
        delete_btn=Button(self.main_frame,text='Delete Patient Details',command=delete_patient_data)
        delete_btn.place(x=200,y=490)



