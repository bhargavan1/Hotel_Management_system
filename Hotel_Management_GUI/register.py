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

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900")
        # --------------------variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\top beautiful hotel in the world.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\Illuminate_Your_True_Nature.png")
        lbl_bg1 = Label(self.root, image=self.bg1, bg="sky blue")
        lbl_bg1.place(x=20, y=100, width=400, height=500)

        # ------------------create frame
        frame = Frame(self.root, bg="white")
        frame.place(x=420, y=100, width=700, height=500)

        # ------------------create labels
        register = Label(frame, text="REGISTER HERE", font=("times new roman", 15, "bold"), bg="white", fg="dark green")
        register.place(x=20, y=20)

        # ------------------row 1
        f_name = Label(frame, text="First Name", font=("times new roman", 10, "bold"), bg="white", fg="black")
        f_name.place(x=50, y=70)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 10))
        self.fname_entry.place(x=50, y=100, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 10, "bold"), bg="white", fg="black")
        l_name.place(x=350, y=70)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 10))
        self.lname_entry.place(x=350, y=100, width=250)

        # ------------------row 2
        con_name = Label(frame, text="Contact No", font=("times new roman", 10, "bold"), bg="white", fg="black")
        con_name.place(x=50, y=140)

        self.con_name_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 10))
        self.con_name_entry.place(x=50, y=170, width=250)

        email_name = Label(frame, text="Email", font=("times new roman", 10, "bold"), bg="white", fg="black")
        email_name.place(x=350, y=140)

        self.emailname_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 10))
        self.emailname_entry.place(x=350, y=170, width=250)

        # ------------------row 3
        Security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 10, "bold"), bg="white",
                           fg="black")
        Security_Q.place(x=50, y=210)

        self.Security_Q_combobox = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 10, "bold"),
                                           state="readonly")
        self.Security_Q_combobox["values"] = ("Select", "Your Birth Place", "Your Favourite Book", "Your Hobby")
        self.Security_Q_combobox.place(x=50, y=240, width=250)
        self.Security_Q_combobox.current(0)

        Security_Answer_name = Label(frame, text="Security Answer", font=("times new roman", 10, "bold"), bg="white",
                                     fg="black")
        Security_Answer_name.place(x=350, y=210)

        self.Security_Answer_name_entry = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 10))
        self.Security_Answer_name_entry.place(x=350, y=240, width=250)

        # ------------------row 4
        pssd_name = Label(frame, text="Password", font=("times new roman", 10, "bold"), bg="white", fg="black")
        pssd_name.place(x=50, y=280)

        self.pssd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 10))
        self.pssd_entry.place(x=50, y=310, width=250)

        Confirm_pssd_name = Label(frame, text="Confirm Password", font=("times new roman", 10, "bold"), bg="white",
                                  fg="black")
        Confirm_pssd_name.place(x=350, y=280)

        self.Confirm_pssd_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 10))
        self.Confirm_pssd_entry.place(x=350, y=310, width=250)

        # ------------------create checkbutton
        self.var_check = IntVar()
        self.chk_btn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                              font=("times new roman", 8, "bold"), bg="white", fg="black", onvalue=1, offvalue=0)
        self.chk_btn.place(x=50, y=350)

        # ------------------buttons for register now,login now
        img1 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\register_now.jpg")
        img1 = img1.resize((200, 40), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl1 = Button(frame, image=self.photoimage1, command=self.register, bg="white", borderwidth=0, cursor="hand2",
                      font=("times new roman", 8, "bold"))
        lbl1.place(x=10, y=400, width=250)

        img2 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\login now.jpg")
        img2 = img2.resize((200, 60), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl2 = Button(frame, image=self.photoimage2, bg="white", borderwidth=0, cursor="hand2",
                      font=("times new roman", 8, "bold"))
        lbl2.place(x=320, y=390, width=250)

    def register(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ == "Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms And Conditions")
        else:
            # Do some database stuff
            # Create a database or connect to one that exists
            conn = sqlite3.connect('register_crm.db')

            # Create a cursor instance
            c = conn.cursor()

            # Create Table
            c.execute("""CREATE TABLE if not exists register (
                    first_name text,
                    last_name text,
                    contact text,
                    email text,
                    securityQ text,
                    securityA text,
                    password text)
                    """)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT  * FROM register WHERE email=?", (self.emailname_entry.get(),))
            record = c.fetchone()
            # record=None
            if record != None:
                messagebox.showerror("Error", "User already exists,plaese try another email")
            else:
                c.execute(
                    "INSERT INTO register VALUES(:first_name, :last_name, :contact, :email, :securityQ, :securityA, :password)",
                    {
                        'first_name': self.var_fname.get(),
                        'last_name': self.var_lname.get(),
                        'contact': self.var_contact.get(),
                        'email': self.var_email.get(),
                        'securityQ': self.var_securityQ.get(),
                        'securityA': self.var_SecurityA.get(),
                        'password': self.var_pass.get(),
                    })
            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()
            messagebox.showinfo("Sucess", "Registration Done")

if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()