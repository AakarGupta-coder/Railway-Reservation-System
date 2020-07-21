from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import time
#===================CREATING CLASS======================================
class IndianRail:
    
    def Login_Page(self):
        self.T=Tk()
        self.T.title("Welcome To Indian Rail")
        self.T.minsize(width=1366,height=768)
        self.bg_img="ir.jpg"
        self.img=ImageTk.PhotoImage(Image.open(self.bg_img))
        self.panel=Label(self.T,image=self.img)
        self.panel.place(x=0,y=0)
        self.Login_Frame=Frame(self.T,height=170,width=345,bd=5,relief=RIDGE)
        self.Login_Frame.place(x=450,y=2)
        self.user=Label(self.Login_Frame,text="User Name: ",font=("georgia",15))
        self.user.place(x=5,y=15)
        self.pas=Label(self.Login_Frame,text="Password: ",font=("georgia",15))
        self.pas.place(x=10,y=55)
        self.user_e=Entry(self.Login_Frame,font=("georgia",15),bd=3,width=15)
        self.user_e.place(x=140,y=15)
        self.pas_e=Entry(self.Login_Frame,font=("georgia",15),bd=3,width=15,show=(u"\u25CF"))
        self.pas_e.place(x=140,y=55)
        self.b1=Button(self.Login_Frame,text="Login",font=("georgia",15,"bold"),bd=5,bg="black",fg="green",command=self.Login_Check)
        self.b1.place(x=140,y=100)
        self.b2=Button(self.Login_Frame,text="Exit",font=("georgia",15,"bold"),bd=5,bg="black",fg="red",padx=18,command=quit)
        self.b2.place(x=224,y=100)
        self.T.mainloop()

    def Login_Check(self):
        self.Id=self.user_e.get()
        self.passwd=self.pas_e.get()
        if(self.Id=="admin" and self.passwd=="admin"):
            self.T.destroy()
            self.Home()
        elif(self.Id=="" and self.passwd==""):
            messagebox.showinfo("Retry","Entries can't be empty!!")
            
        else:
            messagebox.showwarning("Retry","Invalid Login!!")
            self.user_e.delete(0,END)
            self.pas_e.delete(0,END)

    def Home(self):
        self.HM=Tk()
        self.HM.title("Welcome To Indian Railway Ticket Resesvation....")
        self.HM.geometry("1600x800")
        self.bg_img="ir.jpg"
        self.img=ImageTk.PhotoImage(Image.open(self.bg_img))
        self.panel=Label(self.HM,image=self.img)
        self.panel.place(x=0,y=0)

        self.M=Menu(self.HM)
        self.HM.config(menu=self.M)
        self.SM1=Menu(self.M)
        self.M.add_cascade(label="Indian Railway",menu=self.SM1)
        self.SM1.add_cascade(label="Book Ticket",command=self.Book_Ticket)
        self.SM1.add_cascade(label="Cancel Ticket")#,command=self.New)
        self.SM1.add_cascade(label="Found Article")#,command=self.Old)
        self.SM1.add_cascade(label="Lost Article")#,command=self.Old)
        self.HM.mainloop()

        self.HM.mainloop()


    def Book_Ticket(self):
        self.N=Tk()
        self.datee=(time.strftime("%d-%m-%Y"))
        self.N.title("Pasenger Record Form....")
        
        self.NL1=Label(self.N,text="First Name",font=("georgia",15,"bold"))
        self.NL1.grid(row=0,column=0)
        self.NE1=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE1.grid(row=0,column=1)

        self.NL2=Label(self.N,text="Last Name",font=("georgia",15,"bold"))
        self.NL2.grid(row=0,column=2)
        self.NE2=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE2.grid(row=0,column=3)

        self.NL3=Label(self.N,text="Contact No.",font=("georgia",15,"bold"))
        self.NL3.grid(row=1,column=0)
        self.NE3=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE3.grid(row=1,column=1)

        self.NL4=Label(self.N,text="Email ID",font=("georgia",15,"bold"))
        self.NL4.grid(row=1,column=2)
        self.NE4=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE4.grid(row=1,column=3)

        self.NL5=Label(self.N,text="Age",font=("georgia",15,"bold"))
        self.NL5.grid(row=2,column=0)
        self.NE5=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE5.grid(row=2,column=1)

        self.NL6=Label(self.N,text="Date Of J.",font=("georgia",15,"bold"))
        self.NL6.grid(row=2,column=2)
        self.NE6=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE6.grid(row=2,column=3)

        self.NL7=Label(self.N,text="From:",font=("georgia",15,"bold"))
        self.NL7.grid(row=3,column=0)
        self.NE7=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE7.grid(row=3,column=1)

        self.NL8=Label(self.N,text="To:",font=("georgia",15,"bold"))
        self.NL8.grid(row=3,column=2)
        self.NE8=Entry(self.N,font=("georgia",15,"bold"),bd=5,width=15)
        self.NE8.grid(row=3,column=3)

        self.NL9=Label(self.N,text="Quota",font=("georgia",15,"bold"))
        self.NL9.grid(row=4,column=0)
        self.variable1=StringVar()
        self.variable1.set("-select-")
        self.NE9=ttk.Combobox(self.N,textvariable=self.variable1,font=("georgia",15),width=16)
        self.NE9.grid(row=4,column=1)
        self.NE9['value']=("GENERAL","SR.CITIZEN","LADIES","DIVYAANG","TATKAL")

        self.NL10=Label(self.N,text="Class",font=("georgia",15,"bold"))
        self.NL10.grid(row=4,column=2)
        self.variable2=StringVar()
        self.variable2.set("-select-")
        self.NE10=ttk.Combobox(self.N,textvariable=self.variable2,font=("georgia",15),width=16)
        self.NE10.grid(row=4,column=3)
        self.NE10['value']=("Sleeper (SL)","AC First Class(1A) ","AC Second Class(2A)","AC Third Class (3A)")

        
        """
        self.NL3=Label(self.N,text="Student Name",font=("Times New Roman",15,"bold"))
        self.NL3.grid(row=1,column=0)
        self.NE3=Entry(self.N,font=("Times New Roman",15,"bold"),bd=5)
        self.NE3.grid(row=1,column=1)

        self.NL4=Label(self.N,text="Course   ",font=("Times New Roman",15,"bold"))
        self.NL4.grid(row=1,column=2)
        self.variable2=StringVar()
        self.variable2.set("-select-")
        self.NE4=ttk.Combobox(self.N,textvariable=self.variable2,font=("Calibri",15),width=18)
        self.NE4.grid(row=1,column=3)
        self.NE4['value']=("Python","Python","Python","Python","Python")

        self.NL5=Label(self.N,text="Contact No ",font=("Times New Roman",15,"bold"))
        self.NL5.grid(row=2,column=0)
        self.NE5=Entry(self.N,font=("Times New Roman",15,"bold"),bd=5)
        self.NE5.grid(row=2,column=1)

        self.NL6=Label(self.N,text="Email ID  ",font=("Times New Roman",15,"bold"))
        self.NL6.grid(row=2,column=2)
        self.NE6=Entry(self.N,font=("Times New Roman",15,"bold"),bd=5)
        self.NE6.grid(row=2,column=3)

        self.NL7=Label(self.N,text="Reference",font=("Times New Roman",15,"bold"))
        self.NL7.grid(row=3,column=0)
        self.NE7=Entry(self.N,font=("Times New Roman",15,"bold"),bd=5)
        self.NE7.grid(row=3,column=1)

        self.NL8=Label(self.N,text="Remark ",font=("Times New Roman",15,"bold"))
        self.NL8.grid(row=3,column=2)
        self.NE8=Entry(self.N,font=("Times New Roman",15,"bold"),bd=5)
        self.NE8.grid(row=3,column=3)

        self.NB1=Button(self.N,text="SUBMIT",font=("Times New Roman",15,"bold"),bd=5,fg="green")#,command=self.Lead_Submit)
        self.NB1.grid(row=4,column=1)

        self.NB2=Button(self.N,text="RESET",font=("Times New Roman",15,"bold"),bd=5,padx=17)#,command=self.Lead_Reset)
        self.NB2.grid(row=4,column=2)

        self.NB2=Button(self.N,text="EXIT",font=("Times New Roman",15,"bold"),bd=5,fg="red",padx=20)#,command=self.Lead_Exit)
        self.NB2.grid(row=4,column=3)

        self.NE1.insert(0,self.datee)"""
        self.N.mainloop()

ob=IndianRail()
ob.Login_Page()
        
        
    
