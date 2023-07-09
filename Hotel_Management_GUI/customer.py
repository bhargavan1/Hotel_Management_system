from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import random

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1285x550+230+220")

        #---------------------------------------------variables---------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        #-------------------title
        lbl = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                    fg="gold")
        lbl.place(x=0, y=0, width=1295, height=50)

        #--------------------our logo
        img2 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\small-luxury-hotels-logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)
        #---------------------labelFFrame----------
        lblframeleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        lblframeleft.place(x=5,y=50,width=425,height=490)

        #-----------------------------------------------labels and entrys----------------------------------
        # ----------custRef
        lbl_cust_ref= Label(lblframeleft, text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        # entry
        self.entry_ref = ttk.Entry(lblframeleft,textvariable=self.var_ref, font=("times new roman", 13, "bold"),width=29,state="readonly")
        self.entry_ref.grid(row=0,column=1)
        # ----------custname
        cname = Label(lblframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        # entry
        self.entry_cname = ttk.Entry(lblframeleft,textvariable=self.var_cust_name, font=("times new roman", 13, "bold"), width=29)
        self.entry_cname.grid(row=1, column=1)
        # ----------mothername
        mothername = Label(lblframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=6)
        mothername.grid(row=2, column=0, sticky=W)
        # entry
        self.entry_mothername = ttk.Entry(lblframeleft,textvariable=self.var_mother, font=("times new roman", 13, "bold"), width=29)
        self.entry_mothername.grid(row=2, column=1)
        # ----------gender combobox
        lbl_gender = Label(lblframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        # combobox
        self.combo_gender=ttk.Combobox(lblframeleft,textvariable=self.var_gender,font=("arial", 12, "bold"),width=27,state="readonly")
        self.combo_gender['value']=("select","Male","female","other")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=3, column=1)

        # ----------postcode
        PostCode = Label(lblframeleft, text="PostCode", font=("arial", 12, "bold"), padx=2, pady=6)
        PostCode.grid(row=4, column=0, sticky=W)
        # entry
        self.entry_PostCode = ttk.Entry(lblframeleft,textvariable=self.var_post, font=("times new roman", 13, "bold"), width=29)
        self.entry_PostCode.grid(row=4, column=1)
        # ----------mobilenumber
        Mobile = Label(lblframeleft, text="Mobile Number", font=("arial", 12, "bold"), padx=2, pady=6)
        Mobile.grid(row=5, column=0, sticky=W)
        # entry
        self.entry_Mobile = ttk.Entry(lblframeleft,textvariable=self.var_mobile, font=("times new roman", 13, "bold"), width=29)
        self.entry_Mobile.grid(row=5, column=1)
        # ----------email
        email = Label(lblframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        email.grid(row=6, column=0, sticky=W)
        # entry
        self.entry_email = ttk.Entry(lblframeleft,textvariable=self.var_email, font=("times new roman", 13, "bold"), width=29)
        self.entry_email.grid(row=6, column=1)

        # ----------Nationality
        Nationality = Label(lblframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        Nationality.grid(row=7, column=0, sticky=W)
        # combobox
        self.combo_Nationality = ttk.Combobox(lblframeleft,textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        self.combo_Nationality['value'] = ("select", "Indian", "American", "other")
        self.combo_Nationality.current(0)
        self.combo_Nationality.grid(row=7, column=1)

        # ----------idproof
        idproof = Label(lblframeleft, text="Id proof:", font=("arial", 12, "bold"), padx=2, pady=6)
        idproof.grid(row=8, column=0, sticky=W)
        # combobox
        self.combo_idproof = ttk.Combobox(lblframeleft,textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        self.combo_idproof['value'] = ("select", "AdharCard", "Pancard", "Driving Licence","Passport")
        self.combo_idproof.current(0)
        self.combo_idproof.grid(row=8, column=1)
        # ----------idnumber
        id_num = Label(lblframeleft, text="Id number:", font=("arial", 12, "bold"), padx=2, pady=6)
        id_num.grid(row=9, column=0, sticky=W)

        self.entry_id_num = ttk.Entry(lblframeleft,textvariable=self.var_id_number, font=("times new roman", 13, "bold"),
                                  width=29)
        self.entry_id_num.grid(row=9, column=1)

        # ----------address
        address = Label(lblframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        address.grid(row=10, column=0, sticky=W)
        # entry
        self.entry_address = ttk.Entry(lblframeleft,textvariable=self.var_address, font=("times new roman", 13, "bold"), width=29)
        self.entry_address.grid(row=10, column=1)

        #---------------------------------------------btns-------------------------
        btnframe = Frame(lblframeleft,bd=2,relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        btnAdd=Button(btnframe,command=self.add_data,text="Add",font=("arial", 11, "bold"), bg="black",fg="gold",width=10)
        btnAdd.grid(row=0, column=0,padx=1)

        btnUpdate = Button(btnframe,command=self.update_record, text="Update", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btnframe,command=self.delete_record, text="Delete", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btnframe,command=self.reset_data, text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #--------------------------------------tabel frame--------------------------------
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"),
                                  padx=2)
        Table_frame.place(x=435, y=50, width=860, height=490)

        lbl_Search = Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_Search.grid(row=0, column=0, sticky=W,padx=2)
        # combobox
        self.search_var=StringVar()
        combo_Search = ttk.Combobox(Table_frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search['value'] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        # entry
        self.txt_search = StringVar()
        entry_Search = ttk.Entry(Table_frame,textvariable=self.txt_search, font=("times new roman", 13, "bold"), width=24)
        entry_Search.grid(row=0, column=2,padx=2)

        btn_Search = Button(Table_frame,command=self.search_record, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btn_Search.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_frame,command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        #----------------------------------------SHOW DATA TABLE--------------------------------------------
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        #--------------scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        #tree view
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality"
                                                                    ,"idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.fetch_data()

        def clicker(e):
            self.select_record()

        # bindings
        # my_tree.bind("<Double-1>",clicker)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", clicker)


    def select_record(self):
        self.entry_cname.delete(0, END)
        self.entry_mothername.delete(0, END)
        self.combo_gender.current(0)
        self.entry_PostCode.delete(0, END)
        self.entry_Mobile.delete(0, END)
        self.entry_email.delete(0, END)
        self.combo_Nationality.current(0)
        self.combo_idproof.current(0)
        self.entry_id_num.delete(0, END)
        self.entry_address.delete(0, END)

        # grab record number
        selected = self.Cust_Details_Table.focus()
        values = self.Cust_Details_Table.item(selected, 'values')

        self.var_ref.set(values[0])
        self.entry_cname.insert(0, values[1])
        self.entry_mothername.insert(0, values[2])
        self.var_gender.set(values[3])
        self.entry_PostCode.insert(0, values[4])
        self.entry_Mobile.insert(0, values[5])
        self.entry_email.insert(0, values[6])
        self.var_nationality.set(values[7])
        self.var_id_proof.set(values[8])
        self.entry_id_num.insert(0, values[9])
        self.entry_address.insert(0, values[10])
    def create_table(self):
        # do some database stuff
        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        # create a table
        c.execute("""CREATE TABLE if not exists customers_table (
            ref integer,
            name text,
            mother integer,
            gender text,
            post text,
            mobile text,
            email text,
            nationality text,
            idproof text,
            idnumber text,
            address text
        )
        """)

        # commit changes
        conn.commit()

        # close our connection
        conn.close()
    def add_data(self):
        self.create_table()
        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table WHERE ref=?", (self.var_ref.get(),))
        records = c.fetchall()

        print(records)

        # commit changes
        conn.commit()

        # close our connection
        conn.close()
        if records != []:
            messagebox.showerror("Error", "User already existed", parent=self.root)

        elif self.var_ref.get() == "" or self.var_cust_name.get() == "" or self.var_mother.get() == "" or self.var_gender.get() == "select" or self.var_post.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "select" or self.var_id_proof.get() == "select" or self.var_id_number.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # create a database or connect to one that exists
                conn = sqlite3.connect('customer_crm.db')

                # create a cursor
                c = conn.cursor()

                # add new record
                c.execute(
                    "INSERT INTO customers_table VALUES(:ref,:name,:mname,:gender,:post,:mobile,:email,:nationality,:idproof,:idnumber,:address)",
                    {
                        'ref': self.var_ref.get(),
                        'name': self.var_cust_name.get(),
                        'mname': self.var_mother.get(),
                        'gender': self.var_gender.get(),
                        'post': self.var_post.get(),
                        'mobile': self.var_mobile.get(),
                        'email': self.var_email.get(),
                        'nationality': self.var_nationality.get(),
                        'idproof': self.var_id_proof.get(),
                        'idnumber': self.var_id_number.get(),
                        'address': self.var_address.get()
                    }
                    )

                # commit changes
                conn.commit()

                # close our connection
                conn.close()

                messagebox.showinfo("Success", "Customer Details added successfully", parent=self.root)

                self.fetch_data()

                #self.reset_data()

            except Exception as es:
                messagebox.showwarning("Warning", f"something went wrong:{str(es)}", parent=self.root)
    def fetch_data(self):
        #remove everything from treeview
        for record in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(record)

        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table")
        records = c.fetchall()

        global curr_iid
        curr_iid = 0

        for record in records:
            if curr_iid % 2 == 0:
                self.Cust_Details_Table.insert(parent='', index='end', iid=curr_iid, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                record[9], record[10]), tags=('evenrow',))
            else:
                self.Cust_Details_Table.insert(parent='', index='end', iid=curr_iid, text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                record[9], record[10]), tags=('oddrow',))
            curr_iid += 1

        # commit changes
        conn.commit()

        # close our connection
        conn.close()

    def check_user(self):
        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM customers_table WHERE ref=?", (self.var_ref.get(),))
        records = c.fetchall()
        print(records)

        # commit changes
        conn.commit()

        # close our connection
        conn.close()

        return records == []

    def update_record(self):

        if self.check_user():
            messagebox.showerror("Error", "Please select a record", parent=self.root)


        else:
            record = self.Cust_Details_Table.selection()

            data = (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get()
            )

            # create a database or connect to one that exists
            conn = sqlite3.connect('customer_crm.db')

            # create a cursor
            c = conn.cursor()

            c.execute("""UPDATE customers_table SET 
                name=:name,
                mother=:mname,
                gender=:gender,
                post=:post,
                mobile =:mobile,
                email =:email,
                nationality =:nationality,
                idproof =:idproof,
                idnumber =:idnumber,
                address =:address
                WHERE ref=:ref""",
                      {
                          'name': self.var_cust_name.get(),
                          'mname': self.var_mother.get(),
                          'gender': self.var_gender.get(),
                          'post': self.var_post.get(),
                          'mobile': self.var_mobile.get(),
                          'email': self.var_email.get(),
                          'nationality': self.var_nationality.get(),
                          'idproof': self.var_id_proof.get(),
                          'idnumber': self.var_id_number.get(),
                          'address': self.var_address.get(),

                          'ref': self.var_ref.get(),
                      }
                      )

            # commit changes
            conn.commit()

            # close our connection
            conn.close()

            self.Cust_Details_Table.item(record, text="", values=data)

            self.fetch_data()

            # add a little message box
            messagebox.showinfo("Updated!", "Your Record updated successfully", parent=self.root)


    def delete_record(self):
        if self.check_user():
            messagebox.showerror("Error", "Please select a record", parent=self.root)
        else:
            records = self.Cust_Details_Table.selection()
            self.Cust_Details_Table.delete(records[0])

            # create a database or connect to one that exists
            conn = sqlite3.connect('customer_crm.db')

            # create a cursor
            c = conn.cursor()

            c.execute("DELETE FROM customers_table WHERE ref=?", (self.var_ref.get(),))

            # commit changes
            conn.commit()

            # close our connection
            conn.close()

            self.fetch_data()

            # add a little message box
            messagebox.showinfo("Deleted!", "Your Record deleted successfully", parent=self.root)

    def reset_data(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.entry_cname.delete(0, END)
        self.entry_mothername.delete(0, END)
        self.combo_gender.current(0)
        self.entry_PostCode.delete(0, END)
        self.entry_Mobile.delete(0, END)
        self.entry_email.delete(0, END)
        self.combo_Nationality.current(0)
        self.combo_idproof.current(0)
        self.entry_id_num.delete(0, END)
        self.entry_address.delete(0, END)

    def search_record(self):
        if self.search_var.get() == "select":
            messagebox.showerror("Error", "Please select an option to search", parent=self.root)
        elif self.txt_search.get() == "":
            messagebox.showerror("Error", "Please fill the search entry", parent=self.root)
        else:
            lookup_record = self.txt_search.get()

            # clear the treeview
            for record in self.Cust_Details_Table.get_children():
                self.Cust_Details_Table.delete(record)

            if self.search_var.get() == "Mobile":
                sql_cmd = "SELECT * FROM customers_table WHERE mobile LIKE ?"
            elif self.search_var.get() == "Name":
                sql_cmd = "SELECT * FROM customers_table WHERE name LIKE ?"
            else:
                sql_cmd = "SELECT * FROM customers_table WHERE ref LIKE ?"

            # create a database or connect to one that exists
            conn = sqlite3.connect('customer_crm.db')

            # create a cursor
            c = conn.cursor()

            c.execute(sql_cmd, (lookup_record,))
            records = c.fetchall()

            global curr_iid
            curr_iid = 0

            for record in records:
                if curr_iid % 2 == 0:
                    self.Cust_Details_Table.insert(parent='', index='end', iid=curr_iid, text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9], record[10]), tags=('evenrow',))
                else:
                    self.Cust_Details_Table.insert(parent='', index='end', iid=curr_iid, text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9], record[10]), tags=('oddrow',))
                curr_iid += 1

            # commit changes
            conn.commit()

            # close our connection
            conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()