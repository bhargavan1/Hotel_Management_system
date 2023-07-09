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

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800")
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\Hotel-Tips.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        # Frame for login box
        frame = Frame(self.root, bg="black")
        frame.place(x=480, y=100, width=340, height=450)

        # Logo of user image placement
        img1 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\image1_login_user_logo.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        Label(image=self.photoimage1, bg="black", borderwidth=0).place(x=510, y=100, width=280, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # labels
        # user name
        user_name = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        user_name.place(x=70, y=155)

        # entry
        self.username_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.username_entry.place(x=40, y=180, width=270)

        # password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        # entry
        self.password_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.password_entry.place(x=40, y=250, width=270)

        # Icon Images
        img2 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\image1_login_user_logo.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        Label(image=self.photoimage2, bg="black", borderwidth=0).place(x=520, y=255, width=25, height=25)

        img3 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\3.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        Label(image=self.photoimage3, bg="black", borderwidth=0).place(x=520, y=325, width=25, height=25)

        # login buttons
        login_button = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                              relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        login_button.place(x=110, y=300, width=120, height=35)

        # register buttons
        register_button = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0,
                                 fg="white", bg="black", activeforeground="white", activebackground="black")
        register_button.place(x=15, y=350, width=160)

        # forgot_password buttons
        forgot_password_button = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"),
                                        borderwidth=0, fg="white", bg="black", activeforeground="white",
                                        activebackground="black")
        forgot_password_button.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)

    # login function using messageboxes
    def login(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect('register_crm.db')

            # Create a cursor instance
            c = conn.cursor()
            c.execute("SELECT  * FROM register WHERE email=? ", (self.username_entry.get(),))
            row=c.fetchall()
            conn.commit()
            conn.close()
            if row==[]:
                messagebox.showerror("Error", "Invalid Username")
            else:
                if row[0][6] != self.password_entry.get():
                    messagebox.showerror("Error", "Invalid Password")
                else:
                    open_register = messagebox.askyesno("Yes or NO", "Access only admin")
                    print(open_register)
                    if open_register>0:
                        messagebox.showinfo("Success","Welcome to Project")
                        #self.new_window = Toplevel(self.root)
                        #self.app = hotel_management_system(self.new_window)
                    else:
                        if not open_register:
                            return

# --------------reset_password func
    def reset_pass(self):
        if self.Security_Q_combobox.get()=="Select":
            messagebox.showerror("Error","Select Security question",parent=self.root2)
        elif self.Security_Answer_name_entry.get()=="":
            messagebox.showerror("Error","Please enter the Answer",parent=self.root2)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect('register_crm.db')

            # Create a cursor instance
            c = conn.cursor()
            c.execute("SELECT  * FROM register WHERE email=?", (self.username_entry.get(),))
            row1=c.fetchall()
            if self.Security_Q_combobox.get()!=row1[0][4] or self.Security_Answer_name_entry.get()!=row1[0][5]:
                messagebox.showerror("Error", "Please Enter correct answer", parent=self.root2)
            else:
                c.execute("UPDATE register SET password=? WHERE email=?",(self.new_password_entry.get(),self.username_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()

#--------------forgot_password_window
    def forgot_password_window(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error","Please enter the email Address to reset password")
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect('register_crm.db')

            # Create a cursor instance
            c = conn.cursor()
            c.execute("SELECT  * FROM register WHERE email=? ", (self.username_entry.get(),))
            row = c.fetchone()
            conn.commit()
            conn.close()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the Valid username")
            else:
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+480+100")
                l=Label(self.root2,text="Forget Password",font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)
                Security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 10, "bold"),
                                   bg="white",
                                   fg="black")
                Security_Q.place(x=50, y=80)

                self.Security_Q_combobox = ttk.Combobox(self.root2,
                                                        font=("times new roman", 10, "bold"),
                                                        state="readonly")
                self.Security_Q_combobox["values"] = ("Select", "Your Birth Place", "Your Favourite Book", "Your Hobby")
                self.Security_Q_combobox.place(x=50, y=110, width=250)
                self.Security_Q_combobox.current(0)

                Security_Answer_name = Label(self.root2, text="Security Answer", font=("times new roman", 10, "bold"),
                                             bg="white",
                                             fg="black")
                Security_Answer_name.place(x=50, y=150)

                self.Security_Answer_name_entry = ttk.Entry(self.root2,
                                                            font=("times new roman", 10))
                self.Security_Answer_name_entry.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 10, "bold"),
                                             bg="white",
                                             fg="black")
                new_password.place(x=50, y=220)

                self.new_password_entry = ttk.Entry(self.root2,
                                                            font=("times new roman", 10))
                self.new_password_entry.place(x=50, y=250, width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman", 10, "bold"), fg="white", bg="green")
                btn.place(x=100,y=290)

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
        lbl2 = Button(frame, command=self.return_login,image=self.photoimage2, bg="white", borderwidth=0, cursor="hand2",
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
    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    main()