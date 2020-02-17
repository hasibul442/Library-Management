from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:

    def __init__(self,root):

        #============================Background========================
        self.root= root
        self.root.title("Library Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background ='powder blue')

        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surename=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        PostCode=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        DateOverDue=StringVar()
        DayOnLoan=StringVar()
        Prescription=StringVar()

        def iExit():
            iExit=tkinter.messagebox.askyesno("Library Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        #================================Frame========================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,width=1350, padx = 20, bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=('arial',40,'bold'),text="\tLibrary Management System\t", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20,width=1300,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Library Membership Info:",)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Book Details:",)
        DataFrameRight.pack(side=RIGHT)        


        #=================================================Widget=================================================================================
        self.lblMemberType = Label(DataFrameLeft,font=('arial',12,'bold'), text="Member Type:", padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)

                #======Combo Box=======
        self.cboMemberType=ttk.Combobox(DataFrameLeft,font=('arial',12),state='randonly',width=23)
        self.cboMemberType['value']=('Choose One','Student','Lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

                #========Text Box========
        self.lblBookID = Label(DataFrameLeft,font=('arial',12,'bold'), text="Book ID:", padx=2,pady=2)
        self.lblBookID.grid(row=0,column=2,sticky=W)
        self.txtBookID = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtBookID.grid(row=0,column=3)

        self.lblRef = Label(DataFrameLeft,font=('arial',12,'bold'), text="Reference No:", padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtRef.grid(row=1,column=1)

        self.lblBookTitle = Label(DataFrameLeft,font=('arial',12,'bold'), text="Book Title:", padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.txtBookTitle = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtBookTitle.grid(row=1,column=3)

        self.lblTitle = Label(DataFrameLeft,font=('arial',12,'bold'), text="Title:", padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboMemberType=ttk.Combobox(DataFrameLeft,font=('arial',12),state='randonly',width=23)
        self.cboMemberType['value']=('Choose One','Mr.','Miss.','Mrs.','Dr.','Capt.','Ms.')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=2,column=1)

        self.lblAuthor = Label(DataFrameLeft,font=('arial',12,'bold'), text="Author:", padx=2,pady=2)
        self.lblAuthor.grid(row=2,column=2,sticky=W)
        self.txtAuthor = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtAuthor.grid(row=2,column=3)

        self.lblFirstname = Label(DataFrameLeft,font=('arial',12,'bold'), text="First Name:", padx=2,pady=2)
        self.lblFirstname.grid(row=3,column=0,sticky=W)
        self.txtFirstname = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtFirstname.grid(row=3,column=1)

        self.lblLastname = Label(DataFrameLeft,font=('arial',12,'bold'), text="Last Name:", padx=2,pady=2)
        self.lblLastname.grid(row=4,column=0,sticky=W)
        self.txtLastname = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtLastname.grid(row=4,column=1)

        self.lblAddress1 = Label(DataFrameLeft,font=('arial',12,'bold'), text="AAddress 1:", padx=2,pady=2)
        self.lblAddress1.grid(row=5,column=0,sticky=W)
        self.txtAddress1 = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtAddress1.grid(row=5,column=1)

        self.lblAddress2 = Label(DataFrameLeft,font=('arial',12,'bold'), text="Address 2:", padx=2,pady=2)
        self.lblAddress2.grid(row=6,column=0,sticky=W)
        self.txtAddress2 = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtAddress2.grid(row=6,column=1)

        self.lblPostCode = Label(DataFrameLeft,font=('arial',12,'bold'), text="Post Code:", padx=2,pady=2)
        self.lblPostCode.grid(row=7,column=0,sticky=W)
        self.txtPostCode = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtPostCode.grid(row=7,column=1)

        self.lblMobileNo = Label(DataFrameLeft,font=('arial',12,'bold'), text="Mobile No:", padx=2,pady=2)
        self.lblMobileNo.grid(row=8,column=0,sticky=W)
        self.txtMobileNo = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtMobileNo.grid(row=8,column=1)

        self.lblDateBorrowed = Label(DataFrameLeft,font=('arial',12,'bold'), text="Date Borrowed:", padx=2,pady=2)
        self.lblDateBorrowed.grid(row=3,column=2,sticky=W)
        self.txtDateBorrowed = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtDateBorrowed.grid(row=3,column=3)

        self.lblDateDue = Label(DataFrameLeft,font=('arial',12,'bold'), text="Date Due", padx=2,pady=2)
        self.lblDateDue.grid(row=4,column=2,sticky=W)
        self.txtDateDue = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtDateDue.grid(row=4,column=3)

        self.lblDaysonLoan = Label(DataFrameLeft,font=('arial',12,'bold'), text="Days on Loan:", padx=2,pady=2)
        self.lblDaysonLoan.grid(row=5,column=2,sticky=W)
        self.txtDaysonLoan  = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtDaysonLoan.grid(row=5,column=3)

        self.lblLateReturnFine = Label(DataFrameLeft,font=('arial',12,'bold'), text="Late Return Fine:", padx=2,pady=2)
        self.lblLateReturnFine.grid(row=6,column=2,sticky=W)
        self.txtLateReturnFine = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtLateReturnFine.grid(row=6,column=3)

        self.lblDateOverDue = Label(DataFrameLeft,font=('arial',12,'bold'), text="Date Over Due:", padx=2,pady=2)
        self.lblDateOverDue.grid(row=7,column=2,sticky=W)
        self.txtDateOverDue = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtDateOverDue.grid(row=7,column=3)

        self.lblSellingPrice = Label(DataFrameLeft,font=('arial',12,'bold'), text="Selling Price:", padx=2,pady=2)
        self.lblSellingPrice .grid(row=8,column=2,sticky=W)
        self.txtSellingPrice  = Entry(DataFrameLeft,font=('arial',12,'bold'),width=25 )
        self.txtSellingPrice .grid(row=8,column=3)


        #====================================Button==============================================================================
        self.btnDisplayData=Button(ButtonFrame, text = 'Display Data', font=('arial',12,'bold'),width=30,bd=4)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame, text = 'Delete', font=('arial',12,'bold'),width=30,bd=4)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame, text = 'Reset', font=('arial',12,'bold'),width=30,bd=4)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame, text = 'Exit', font=('arial',12,'bold'),width=30,bd=4, command=iExit)
        self.btnExit.grid(row=0,column=3)

        #=====================Widget======================================
        self.txtDisplayR=Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)

        #========================================List Box======================
        
        ListOfBooks = ['Cinderella','Game Design', 'Ancient Rome', 'Made in Africa', 'Sleeping Beauty', 'London', 'Nigeria', 'Snow White', 'Shreik 3', 'Shreik 2', 'London Street', 'I Love Lagos', 'Hello India', 'Love Kenya']
        booklist=Listbox(DataFrameRight, width = 20, height=12,font=('arial',12,'bold'))
        booklist.bind('<<ListboxSelect>>')
        booklist.grid(row=0,column=0,padx=8)

                #=======Scrollbar=======
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1,sticky='ns')
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END,items)


    #==============================View Data==========
        self.lblLable=Label(FrameDetail,font=('arial',10,'bold'),pady=8,text="Member Type\tReference No.\tTitle\tFirstname\tSurename\tAddress 1\tAddress 2\tPost Code\tBook Title\tData Borrowed\tDays On Loan",)
        self.lblLable.grid(row=0,column=0)

        self.txtDisplayR=Text(FrameDetail,font=('arial',12,'bold'),width=141,height=4,padx=2,pady=4)
        self.txtDisplayR.grid(row=1,column=0)

        
        

        

if __name__=='__main__':
    root=Tk()
    application = Library(root)
    root.mainloop()
