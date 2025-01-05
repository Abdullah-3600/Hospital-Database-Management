from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Admin_UI:
    def __init__(self,window):
        self.admin_ui=window
        self.admin_ui.geometry('800x600')
        self.admin_ui.title('ADMIN USER INTERFACE')
        self.admin_ui.resizable(FALSE,FALSE)
        self.options_frame = Frame(self.admin_ui, bg='pink')
        self.options_frame.pack(side=LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=200, height=600)
        self.main_frame = Frame(self.admin_ui, bg='light green')
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=600, width=600)
        option_label=Label(self.options_frame,text='SELECT OPTIONS',font=('Times New Roman',13,'bold'),bg='pink').pack()
        nurse_button=Button(self.options_frame,text='Edit Nurse Database',font=('Times New Roman',13,'bold'),bg='pink',command=self.nurse_settings)
        nurse_button.place(x=5,y=150)
        nurse_doc_button=Button(self.options_frame,text='View Database',font=('Times New Roman',13,'bold'),bg='pink',command=self.view_db_settings)
        nurse_doc_button.place(x=5,y=300)
        main_frame_label=Label(self.main_frame,text='Select Options First',font=('Times New Roman',13,'bold'),bg='light green').pack()



    def nurse_settings(self):
        def update():
            if name_entry.get()=='' or id_entry.get()=='' or assign_room_entry.get()=='':
                messagebox.showerror('Information Blank', 'Please give proper information.')
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
                mycursor=con.cursor()
                query='update nurse_registration_table set doctor_id=%s,supervisor_id=%s,assigned_room=%s where ID=%s and name=%s '
                mycursor.execute(query,(assign_doc_entry.get(),assign_supervisor_entry.get(),assign_room_entry.get(),id_entry.get(),name_entry.get()))
                con.commit()
                con.close()



        self.delete_frames()
        title_label=Label(self.main_frame,text='Edit Nurse Database',font=('Times New Roman',15,'bold'),bg='light green').pack()
        name_label=Label(self.main_frame,text='Enter Nurse Name :',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=100)
        id_label=Label(self.main_frame,text='Enter Nurse ID :',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=150)
        assign_doc_label=Label(self.main_frame,text='Assigned Doctor ID :',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=200)
        assign_supervisor_label=Label(self.main_frame,text='Assigned Supervisor ID:',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=250)
        assign_room_label=Label(self.main_frame,text='Assigned Room Number  :',font=('Times New Roman',15,'bold'),bg='light green').place(x=5,y=300)
        name_entry=Entry(self.main_frame,width=25,font=('Times New Roman',15,'bold'))
        name_entry.place(x=230,y=100)
        id_entry=Entry(self.main_frame,width=25,font=('Times New Roman',15,'bold'))
        id_entry.place(x=230,y=150)
        assign_doc_entry=Entry(self.main_frame,width=25,font=('Times New Roman',15,'bold'))
        assign_doc_entry.place(x=230,y=200)
        assign_supervisor_entry=Entry(self.main_frame,width=25,font=('Times New Roman',15,'bold'))
        assign_supervisor_entry.place(x=230,y=250)
        assign_room_entry=ttk.Combobox(self.main_frame,font=('Times New Roman',15,'bold'),value=['R123','R234','R543','R900','R897','R567','R321'])
        assign_room_entry['state']='readonly'
        assign_room_entry.place(x=230,y=300)
        update_btn=Button(self.main_frame,text='Update',font=('Times New Roman',15,'bold'),command=update)
        update_btn.place(x=250,y=400)



    def view_db_settings(self):
        self.delete_frames()
        title_label = Label(self.main_frame, text='View Nurse-Doctor Database', font=('Times New Roman', 15, 'bold'),bg='light green').pack()
        # Create a Treeview widget
        treeview = ttk.Treeview(self.main_frame, columns=(
        "nurse_id", "doctor_id",  "supervisor_id",  "room_number"),
                                show="headings")

        con= pymysql.connect(host='localhost',user='root',password='',database='hospital_management')
        mycursor=con.cursor()
        query='select n.id,d.id,n.supervisor_id,n.assigned_room from nurse_registration_table n, doctor_registration_table d where n.doctor_id=d.id'
        mycursor.execute(query)
        row=mycursor.fetchall()
        con.commit()
        con.close()


        # Define the headings for each column
        treeview.heading("nurse_id", text="Nurse ID")
        treeview.heading("doctor_id", text="Doctor ID")
        treeview.heading("supervisor_id", text="Supervisor ID")
        treeview.heading("room_number", text="Room Number")

        # Set the width of each column

        treeview.column("nurse_id", width=100, anchor="center",stretch=NO)
        treeview.column("doctor_id", width=150, anchor="center",stretch=NO)
        treeview.column("supervisor_id", width=100, anchor="center",stretch=NO)
        treeview.column("room_number", width=100, anchor="center",stretch=NO)
        for val in row:
            treeview.insert("", "end", values=val)

        treeview.pack(padx=10, pady=10, fill="both", expand=True)

    def delete_frames(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()




