import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Doctor_UI:
    def __init__(self, window):
        self.search_name = StringVar()
        self.search_id = StringVar()
        self.search_date = StringVar()
        self.doctor_ui = window
        self.doctor_ui.title('Patient Serial Details')
        self.doctor_ui.config(bg='light blue')
        self.doctor_ui.geometry('500x500')
        self.doctor_ui.resizable(FALSE, FALSE)

        # Frame to hold the treeview
        self.patient_details_frame = Frame(self.doctor_ui, bg='light green')
        self.patient_details_frame.pack()
        self.patient_details_frame.pack_propagate(False)
        self.patient_details_frame.configure(width=500, height=300)

        # Treeview to show patient details
        self.treeview = ttk.Treeview(self.patient_details_frame, columns=('Patient ID', 'Patient Name', 'Doctor Name', 'Date'), show='headings')
        self.treeview.pack(fill=BOTH, expand=True)

        self.treeview.heading('Patient ID', text='Patient ID')
        self.treeview.heading('Patient Name', text='Patient Name')
        self.treeview.heading('Doctor Name', text='Doctor Name')
        self.treeview.heading('Date', text='Date')

        # Entry fields for search
        search_name_entry = Entry(self.doctor_ui, width=20, textvariable=self.search_name)
        search_name_entry.place(x=5, y=310)
        search_id_entry = Entry(self.doctor_ui, width=20, textvariable=self.search_id)
        search_id_entry.place(x=5, y=340)
        search_date_entry = Entry(self.doctor_ui, width=20, textvariable=self.search_date)
        search_date_entry.place(x=5, y=370)

        # Search buttons
        search_btn1 = Button(self.doctor_ui, text='Search By Name', command=self.search_by_name)
        search_btn1.place(x=150, y=310)
        search_btn2 = Button(self.doctor_ui, text='Search By ID', command=self.search_by_id)
        search_btn2.place(x=150, y=340)
        search_btn3 = Button(self.doctor_ui, text='Search By Date', command=self.search_by_date)
        search_btn3.place(x=150, y=370)

        # Delete button
        delete_btn = Button(self.doctor_ui, text='Delete', command=self.delete_record)
        delete_btn.place(x=400, y=310)

        # Fetch and populate data on UI initialization
        self.fetch_data()

    def fetch_data(self, condition=None):
        # Connect to the MySQL database
        try:

            con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
            mycursor = con.cursor()
            query='create table if not exists doctor_patient_treatment(Patient_ID varchar(4),Patient_Name varchar(20),Doctor_Name varchar(20),Date Date)'
            mycursor.execute(query)
            # Query to fetch all data or apply condition based on search criteria
            query = 'SELECT * FROM doctor_patient_treatment'
            if condition:
                query += f' WHERE {condition}'

            mycursor.execute(query)
            data = mycursor.fetchall()

            # Clear existing treeview entries
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Populate the treeview with fetched data
            for row in data:
                self.treeview.insert('', 'end', values=row)

            con.close()
        except Exception as e:
            messagebox.showerror('Error', f"Error fetching data: {e}")

    def search_by_name(self):
        name = self.search_name.get()
        if name:
            condition = f"Patient_Name LIKE '%{name}%'"
            self.fetch_data(condition)

    def search_by_id(self):
        patient_id = self.search_id.get()
        if patient_id:
            condition = f"Patient_ID = '{patient_id}'"
            self.fetch_data(condition)

    def search_by_date(self):
        date = self.search_date.get()
        if date:
            condition = f"Date = '{date}'"
            self.fetch_data(condition)

    def delete_record(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showwarning("No selection", "Please select a record to delete.")
            return

        # Get the Patient ID from the selected row
        patient_id = self.treeview.item(selected_item, 'values')[0]

        # Connect to the MySQL database
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='hospital_management')
            mycursor = con.cursor()

            # Delete the record based on Patient ID
            query = f"DELETE FROM doctor_patient_treatment WHERE Patient_ID = '{patient_id}'"
            mycursor.execute(query)
            con.commit()

            # Notify the user and refresh the data
            messagebox.showinfo("Success", "Record deleted successfully!")
            self.fetch_data()

            con.close()
        except Exception as e:
            messagebox.showerror('Error', f"Error deleting record: {e}")


