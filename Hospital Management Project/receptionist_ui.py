from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime

class RECEPTIONIST_UI:
    def __init__(self,window):
        self.patient_id=self.new_id()
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

    def patient_register(self):
        self.patient_id=self.new_id()
        self.delete_frames()
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
        age_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        age_entry.place(x=200,y=200)
        phone_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        phone_entry.place(x=200,y=250)
        issues_entry=Entry(self.main_frame,font=('Times New Roman',15,'bold'),width=25)
        issues_entry.place(x=200,y=300)
        select_doctor=ttk.Combobox(self.main_frame,font=('Times New Roman',15,'bold'),values=self.doctor_list())
        select_doctor['state']='readonly'
        select_doctor.place(x=200,y=350)
        register_btn=Button(self.main_frame,text='Register New Patient',font=('Times New Roman',15,'bold'),command=lambda: self.register(name_entry,age_entry,phone_entry,issues_entry,select_doctor))
        register_btn.place(x=200,y=450)



    def new_id(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
        mycursor=con.cursor()
        query = 'SELECT MAX(ID) FROM patient_registration_table'
        mycursor.execute(query)
        row = mycursor.fetchone()
        con.close()
        if row[0] == None:
            return'1'
        else:
            return str(int(row[0]) + 1)


    def register(self,name_entry,age_entry,phone_entry,issues_entry,select_doctor):
        print(age_entry.get())
        try: 
            if int(age_entry.get())<= 0 or int(phone_entry.get())<= 0:
                messagebox.showerror('Error','Age and Number cannot be negative')          

        except :
            messagebox.showerror('Error','Age and Number must be a valid number')

        else:
            if name_entry.get()=='' or age_entry=='' or phone_entry.get()=='' or select_doctor.get()=='' or issues_entry.get()=='':
                messagebox.showerror('Error','Please fill all fields')
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
                mycursor=con.cursor()


                query='insert into patient_registration_table(ID,Name,Age,Phone,Issues) values (%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.patient_id,name_entry.get(),age_entry.get(),phone_entry.get(),issues_entry.get()))

                query='insert into doctor_patient_treatment(Patient_ID,Patient_Name, Doctor_Name, Date) values(%s,%s,%s,%s)'
                mycursor.execute(query,(self.patient_id,name_entry.get(),select_doctor.get(),datetime.today().date()))
                con.commit()
                con.close()
                messagebox.showinfo('Patient Registration','Patient has been successfully registered')
                self.patient_id=self.new_id()
                id_label2=Label(self.main_frame,text=self.patient_id,font=('Times New Roman',15,'bold'),bg='light green').place(x=200,y=100)


    def doctor_list(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
        mycursor=con.cursor()
        query='select name from doctor_registration_table'
        mycursor.execute(query)
        row=mycursor.fetchall()
        doctor_lists=[i[0] for i in row]
        return doctor_lists



    def view_all(self,treeview):
        con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
        mycursor = con.cursor()

        query = 'SELECT * FROM patient_registration_table'
        mycursor.execute(query)
        data = mycursor.fetchall()

        # Clearing entries
        for row in treeview.get_children():
            treeview.delete(row)

        # inserting new data
        for row in data:
            treeview.insert('', 'end', values=row)

        con.close()

    def edit_patient_data(self,treeview,edit_entry,edit_val_entry):
        selected_patient=treeview.selection()
        current_patient=treeview.item(selected_patient[0])
        patient_id = current_patient['values'][0]

        con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
        mycursor = con.cursor()
        field = edit_entry.get()
        if field == 'Age':
            query = 'UPDATE patient_registration_table SET Age=%s WHERE ID=%s'
            mycursor.execute(query, (edit_val_entry.get(), patient_id))
        elif field == 'Phone':
            query = 'UPDATE patient_registration_table SET Phone=%s WHERE ID=%s'
            mycursor.execute(query, (edit_val_entry.get(), patient_id))
        elif field == 'Issues':
            query = 'UPDATE patient_registration_table SET Issues=%s WHERE ID=%s'
            mycursor.execute(query, (edit_val_entry.get(), patient_id))
        con.commit()
        con.close()

    def search_by_name(self,treeview,name_entry):
        con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
        mycursor = con.cursor()

        query = 'SELECT * FROM patient_registration_table where Name=%s'
        mycursor.execute(query,name_entry.get())
        data = mycursor.fetchall()

        # Clearing entries
        for row in treeview.get_children():
            treeview.delete(row)

      # inserting new data
        for row in data:
            treeview.insert('', 'end', values=row)

            con.close()

    def edit_patient(self):
        self.delete_frames()
        title_label=Label(self.main_frame,text='Edit Patient Details',font=("Times New Roman",15,'bold'),bg='light green').pack()
        patient_details_frame = Frame(self.main_frame, bg='light blue')
        patient_details_frame.pack()
        patient_details_frame.pack_propagate(False)
        patient_details_frame.configure(width=800, height=300)

        # Add horizontal scrollbar
        h_scroll = ttk.Scrollbar(patient_details_frame, orient=HORIZONTAL)
        h_scroll.pack(side=BOTTOM, fill=X)

        # Modify treeview to use scrollbar
        treeview = ttk.Treeview(patient_details_frame,
                               columns=('Patient ID', 'Patient Name','Age','Phone' ,'Issue'),
                               show='headings',
                               xscrollcommand=h_scroll.set)
        treeview.pack(fill=BOTH, expand=True)

        # Configure scrollbar
        h_scroll.config(command=treeview.xview)

        treeview.heading('Patient ID', text='Patient ID')
        treeview.heading('Patient Name', text='Patient Name')
        treeview.heading('Phone', text='Phone')
        treeview.heading('Age', text='Age')
        treeview.heading('Issue', text='Issue')

        editable_fields=[  'Age', 'Phone', 'Issues']

        name_entry=Entry(self.main_frame,width=20)
        name_entry.place(x=5,y=410)
        search_btn1 = Button(self.main_frame, text='Search By Name',command=lambda: self.search_by_name(treeview,name_entry))
        search_btn1.place(x=200, y=410)
        view_all_btn=Button(self.main_frame,text='View All Patient Details',command=lambda: self.view_all(treeview))
        view_all_btn.place(x=200,y=370)
        edit_val_entry=Entry(self.main_frame,width=20)
        edit_val_entry.place(x=5,y=490)
        edit_entry = ttk.Combobox(self.main_frame,font=('Times New Roman', 15, 'bold'), values=editable_fields, width=15)
        edit_entry['state'] = 'readonly'
        edit_entry.place(x=200, y=490)
        edit_btn=Button(self.main_frame,text='Edit Patient Details',command=lambda: self.edit_patient_data(treeview,edit_entry,edit_val_entry))
        edit_btn.place(x=400,y=490)