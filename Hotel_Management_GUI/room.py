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
from customer import Cust_Win

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x550+230+220")
        #--------------------------variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        # -------------------title
        lbl = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                    fg="gold")
        lbl.place(x=0, y=0, width=1295, height=50)

        # --------------------our logo
        img2 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\small-luxury-hotels-logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # ---------------------labelFFrame----------
        lblframeleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="Room Booking Details", font=("arial", 12, "bold"),
                                  padx=2)
        lblframeleft.place(x=5, y=50, width=425, height=490)
        # -----------------------------------------------labels and entrys----------------------------------
        # ----------custcontact
        lbl_cust_contact = Label(lblframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        # entry
        self.entry_contact = ttk.Entry(lblframeleft,textvariable=self.var_contact, font=("times new roman", 13, "bold"), width=20)
        self.entry_contact.grid(row=0, column=1,sticky=W)

        #fetch data button
        btnFetchData = Button(lblframeleft,command=self.fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347,y=4)
        # ----------check indate
        check_in_date = Label(lblframeleft, text="Check in date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        # entry
        self.txtcheck_in_date = ttk.Entry(lblframeleft,textvariable=self.var_checkin, font=("times new roman", 13, "bold"),
                                          width=29)
        self.txtcheck_in_date.grid(row=1, column=1)
        # ----------check outdate
        lbl_check_out = Label(lblframeleft, text="Check out date", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_out.grid(row=2, column=0, sticky=W)
        # entry
        self.txt_check_out = ttk.Entry(lblframeleft,textvariable=self.var_checkout, font=("times new roman", 13, "bold"),
                                          width=29)
        self.txt_check_out.grid(row=2, column=1)
        # ----------Room Type
        label_RoomType = Label(lblframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)
        # entry combo box
        self.combo_RoomType = ttk.Combobox(lblframeleft,textvariable=self.var_roomtype ,font=("arial", 12, "bold"),
                                         width=27, state="readonly")
        self.combo_RoomType['value'] = ("select", "single", "Double", "lexary")
        self.combo_RoomType.current(0)
        self.combo_RoomType.grid(row=3, column=1)

        # ----------available soon
        lblRoomAvailable = Label(lblframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        # entry
        self.txtRoomAvailable = ttk.Entry(lblframeleft,textvariable=self.var_roomavailable, font=("times new roman", 13, "bold"),
                                       width=29)
        self.txtRoomAvailable.grid(row=4, column=1)
        # ----------meal
        lblMeal = Label(lblframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        # entry
        self.txtMeal = ttk.Entry(lblframeleft,textvariable=self.var_meal, font=("times new roman", 13, "bold"),
                                          width=29)
        self.txtMeal.grid(row=5, column=1)
        # ----------no. of days
        lblNoofDays = Label(lblframeleft, text="No of days", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoofDays.grid(row=6, column=0, sticky=W)
        # entry
        self.txtNoofDays = ttk.Entry(lblframeleft,textvariable=self.var_noofdays, font=("times new roman", 13, "bold"),
                                 width=29)
        self.txtNoofDays.grid(row=6, column=1)
        # ---------paid tax
        lblpaidtax = Label(lblframeleft, text="paid tax", font=("arial", 12, "bold"), padx=2, pady=6)
        lblpaidtax.grid(row=7, column=0, sticky=W)
        # entry
        self.txtpaidtax = ttk.Entry(lblframeleft,textvariable=self.var_paidtax, font=("times new roman", 13, "bold"),
                                     width=29)
        self.txtpaidtax.grid(row=7, column=1)
        # ----------subtotal
        lblsubtotal = Label(lblframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblsubtotal.grid(row=8, column=0, sticky=W)
        # entry
        self.txtsubtotal = ttk.Entry(lblframeleft,textvariable=self.var_actualtotal, font=("times new roman", 13, "bold"),
                                     width=29)
        self.txtsubtotal.grid(row=8, column=1)
        # ----------total cost
        lblIdNumber = Label(lblframeleft, text="Total cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        # entry
        self.txtIdNumber = ttk.Entry(lblframeleft,textvariable=self.var_total, font=("times new roman", 13, "bold"),
                                     width=29)
        self.txtIdNumber.grid(row=9, column=1)

        ################-----------Bill button
        btnAdd = Button(lblframeleft, text="Bill", font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=10, column=0, padx=1,sticky=W)
        # ---------------------------------------------btns-------------------------
        btnframe = Frame(lblframeleft, bd=2, relief=RIDGE)
        btnframe.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btnframe, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btnframe, text="Update",command=self.update_record, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btnframe,  text="Delete", font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btnframe,  text="Reset", font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        #-------------------Right side image
        img3 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\top beautiful hotel in the world.jpg")
        img3 = img3.resize((520, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=750, y=55, width=520, height=300)

        # --------------------------------------tabel frame search system--------------------------------
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                 font=("arial", 12, "bold"),
                                 padx=2)
        Table_frame.place(x=435, y=280, width=860, height=260)

        lbl_Search = Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_Search.grid(row=0, column=0, sticky=W, padx=2)
        # combobox
        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                    state="readonly")
        combo_Search['value'] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        # entry
        self.txt_search = StringVar()
        entry_Search = ttk.Entry(Table_frame, textvariable=self.txt_search, font=("times new roman", 13, "bold"),
                                 width=24)
        entry_Search.grid(row=0, column=2, padx=2)

        btn_Search = Button(Table_frame, text="Search", font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btn_Search.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_frame, text="Show All", font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ----------------------------------------SHOW DATA TABLE--------------------------------------------
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        # --------------scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # tree view
        self.room_Table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkin", text="Check-in")
        self.room_Table.heading("checkout", text="Check-out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noofdays", text="NoOfDays")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkin", width=100)
        self.room_Table.column("checkout", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("roomavailable", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noofdays", width=100)

        self.room_Table.pack(fill=BOTH, expand=1)

        def clicker(e):
            self.select_record()

            # bindings
            # my_tree.bind("<Double-1>",clicker)
        self.room_Table.bind("<ButtonRelease-1>", clicker)
        self.fetch_data()

    def create_table(self):
        # do some database stuff
        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        # create a table
        c.execute("""CREATE TABLE if not exists rooms_table (
            contact text,
            checkin text,
            checkout text,
            roomtype text,
            room text PRIMARY KEY,
            meal text,
            noofDays text
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

        c.execute("SELECT * FROM customers_table WHERE ref=?", (self.var_contact.get(),))
        records = c.fetchall()

        print(records)

        # commit changes
        conn.commit()

        # close our connection
        conn.close()
        if records != []:
            messagebox.showerror("Error", "User already existed", parent=self.root)

        elif self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # create a database or connect to one that exists
                conn = sqlite3.connect('customer_crm.db')

                # create a cursor
                c = conn.cursor()

                # add new record
                c.execute(
                    "INSERT INTO rooms_table VALUES(:contact,:checkin,:checkout,:roomtype,:room,:meal,:noofDays)",
                    {
                        'contact': self.var_contact.get(),
                        'checkin': self.var_checkin.get(),
                        'checkout': self.var_checkout.get(),
                        'roomtype': self.var_roomtype.get(),
                        'room': self.var_roomavailable.get(),
                        'meal':self.var_meal.get(),
                        'noofDays': self.var_noofdays.get(),
                    }
                    )

                # commit changes
                conn.commit()

                # close our connection
                conn.close()

                messagebox.showinfo("Success", "Room Booked", parent=self.root)

                self.fetch_data()

                #self.reset_data()
            except Exception as es:
                messagebox.showwarning("Warning", f"something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        #remove everything from treeview
        for record in self.room_Table.get_children():
            self.room_Table.delete(record)

        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM rooms_table")
        records = c.fetchall()

        global curr_iid
        curr_iid = 0

        for record in records:
            if curr_iid % 2 == 0:
                self.room_Table.insert(parent='', index='end', iid=curr_iid, text="",
                                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                       tags=('evenrow',))
            else:
                self.room_Table.insert(parent='', index='end', iid=curr_iid, text="",
                                       values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                       tags=('oddrow',))
            curr_iid += 1

        # commit changes
        conn.commit()

        # close our connection
        conn.close()

    def select_record(self):
        self.entry_contact.delete(0, END)
        self.txtcheck_in_date.delete(0, END)
        self.txt_check_out.delete(0, END)
        self.combo_RoomType.current(0)
        self.txtRoomAvailable.delete(0, END)
        self.txtMeal.delete(0, END)
        self.txtNoofDays.delete(0, END)

        # grab record number
        selected = self.room_Table.focus()
        values1 = self.room_Table.item(selected, 'values')

        self.entry_contact.insert(0, values1[0])
        self.txtcheck_in_date.insert(0, values1[1])
        self.txt_check_out.insert(0, values1[2])
        self.combo_RoomType.set(values1[3])
        self.txtRoomAvailable.insert(0,values1[4])
        self.txtMeal.insert(0, values1[5])
        self.txtNoofDays.insert(0, values1[6])

    def check_user(self):
        # create a database or connect to one that exists
        conn = sqlite3.connect('customer_crm.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM rooms_table WHERE contact=?", (self.var_contact.get(),))
        records = c.fetchall()

        # commit changes
        conn.commit()

        # close our connection
        conn.close()

        return records == []

    def update_record(self):

        if self.check_user():
            messagebox.showerror("Error", "Please select a record", parent=self.root)


        else:
            record = self.room_Table.selection()

            data = (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
            )

            # create a database or connect to one that exists
            conn = sqlite3.connect('customer_crm.db')

            # create a cursor
            c = conn.cursor()

            c.execute("""UPDATE rooms_table SET 
                checkin=:checkin,
                checkout=:checkout,
                roomtype=:roomtype,
                room=:room,
                meal=:meal,
                noofDays=:noofDays
                WHERE contact=:contact""",
                      {

                          'checkin': self.var_checkin.get(),
                          'checkout': self.var_checkout.get(),
                          'roomtype': self.var_roomtype.get(),
                          'room': self.var_roomavailable.get(),
                          'meal': self.var_meal.get(),
                          'noofDays': self.var_noofdays.get(),

                          'contact': self.var_contact.get(),
                      }
                      )

            # commit changes
            conn.commit()

            # close our connection
            conn.close()

            self.room_Table.item(record, text="", values=data)

            #self.reset_data()

            # add a little message box
            messagebox.showinfo("Updated!", "Your Record updated successfully", parent=self.root)


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter contact number",parent=self.root)
        else:
            # create a database or connect to one that exists
            conn = sqlite3.connect('customer_crm.db')

            # create a cursor
            c = conn.cursor()

            c.execute("SELECT * FROM customers_table WHERE mobile LIKE ?", (self.var_contact.get(),))
            records = c.fetchall()

            # commit changes
            conn.commit()

            # close our connection
            conn.close()
            if records == []:
                messagebox.showerror("Error", "This number not found", parent=self.root)
            else:
                show_data_frame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                show_data_frame.place(x=450, y=55, width=300, height=180)

                name_label = Label(show_data_frame, text="Name", font=("arial", 12, "bold"))
                name_label.place(x=0, y=0)

                name_data = Label(show_data_frame, text=": " + records[0][1], font=("arial", 12, "bold"))
                name_data.place(x=90, y=0)

                gender_label = Label(show_data_frame, text="Gender", font=("arial", 12, "bold"))
                gender_label.place(x=0, y=30)

                gender_data = Label(show_data_frame, text=": " + records[0][3], font=("arial", 12, "bold"))
                gender_data.place(x=90, y=30)

                email_label = Label(show_data_frame, text="Email", font=("arial", 12, "bold"))
                email_label.place(x=0, y=60)

                email_data = Label(show_data_frame, text=": " + records[0][6], font=("arial", 12, "bold"))
                email_data.place(x=90, y=60)

                nationality_label = Label(show_data_frame, text="Nationality", font=("arial", 12, "bold"))
                nationality_label.place(x=0, y=90)

                nationality_data = Label(show_data_frame, text=": " + records[0][7], font=("arial", 12, "bold"))
                nationality_data.place(x=90, y=90)

                address_label = Label(show_data_frame, text="Address", font=("arial", 12, "bold"))
                address_label.place(x=0, y=120)

                address_data = Label(show_data_frame, text=": " + records[0][10], font=("arial", 12, "bold"))
                address_data.place(x=90, y=120)




if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
