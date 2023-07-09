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
from room import Roombooking

class HotelMangementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800")

        #--------------background top image
        img1=Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\Hotel-Tips.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #--------------our logo
        img2 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\small-luxury-hotels-logo.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        #------------border heading
        lbl=Label(self.root,text="Hotel Management System" ,font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbl.place(x=0,y=140,width=1550,height=50)

        #--------------------main frame
        frame=Frame(self.root,bg="white",bd=4,relief=RIDGE)
        frame.place(x=0,y=190,width=1550,height=620)

        #------------menu label
        lbl_menu = Label(frame, text="Menu", font=("times new roman", 20, "bold"), bg="black",
                    fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #-------------btn frame
        btn_frame = Frame(frame, bg="white", bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)
        #-----------------------------------buttons----------------------------------
        cust_btn=Button(btn_frame,command=self.cust_details,text="CUSTOMER",width=22,font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand2",relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,command=self.roombooking, text="ROOM", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2", relief=RIDGE)
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2", relief=RIDGE)
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand2", relief=RIDGE)
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",
                         fg="gold", bd=0, cursor="hand2", relief=RIDGE)
        logout_btn.grid(row=4, column=0, pady=1)

        #--------------------------------right image-----------------------------------
        img3 = Image.open(r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\top beautiful hotel in the world.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        #-----------------------------------down left images -2-------------------------
        img4 = Image.open(
            r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\top beautiful hotel in the world.jpg")
        img4 = img4.resize((230,210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230,height=210)

        img5 = Image.open(
            r"C:\Users\Hemanth\PycharmProjects\Hotel_Management_GUI\images\top beautiful hotel in the world.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=100)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app= Cust_Win(self.new_window)
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app= Roombooking(self.new_window)


if __name__=="__main__":
    root=Tk()
    app=HotelMangementSystem(root)
    root.mainloop()