from fileinput import filename
from itertools import product
import os
import time
from tkinter import *
from tkinter import ttk
from turtle import width
from time import strftime
import random
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import tempfile


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        #self.root.resizable(False,False)

        #=====================VARIABLES=====================#
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.Tax=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        Tax=1



        # Product Categories list
        self.Category=["Select Option","Clothing","LifeStyle","Edibles","Mobiles"]

        #SubCatClothing
        self.SubCatClothing=["Pant","T_Shirt","Shirt","Sweaters","Hoodies"]
        
        self.Pant=["Levis","Diesel","Wrangler","CalvinKlein","AllenSolly"]
        self.price_Levis=5000
        self.price_Diesel=6500
        self.price_Wrangler=8000
        self.price_CalvinKlein=10000
        self.price_AllenSolly=9000

        self.T_Shirt=["Polo","Roadster","JacknJones","Armani","Spykar"]
        self.price_Polo=600
        self.price_Roadster=550
        self.price_JacknJones=700
        self.price_Armani=1000
        self.price_Spykar=500

        
        self.Shirt=["Peter_England","Van_Heusen","Louis_Phillipe","Park_Avenue","US_Polo","Lee"]
        self.price_Peter_England=800
        self.price_Van_Heusen=1500
        self.price_Louis_Phillipe=1200
        self.price_Park_Avenue=900
        self.price_US_Polo=950
        self.price_Lee=500

        
        self.Sweaters=["Tommy_Hilfiger","GAP ","Forever_21","Blackberrys","Ether"]
        self.price_Tommy_Hilfiger=700
        self.price_GAP=500
        self.price_Forever_21=600
        self.price_Blackberrys=900
        self.price_Ether=800

        
        self.Hoodies=["Puma","Flying_Machine","Nautica","Nike","Wrogn"]
        self.price_Puma=3500
        self.price_Flying_Machine=2000
        self.price_Nautica=2800
        self.price_Nike=4000
        self.price_Wrogn=2500

        #SubCatLifeStyle
        self.SubCatLifeStyle=["Bath_Soap","Face_Cream","Hair_Oil","Shampoo","Face_Wash","Body_Wash","Moisturizer","Room_Freshner","ToothPaste"]
        
        
        self.Bath_Soap=['Dettol','Lux','Life_Boy','Santoor','Pears']
        self.price_Dettol=30
        self.price_Lux=40
        self.price_Life_Boy=20
        self.price_Santoor=35
        self.price_Pears=45


        self.Face_Cream=['Himalaya','Nivea','Loreal','Biotique','Lotus']
        self.price_Himalaya=180
        self.price_Nivea=240
        self.price_Loreal=650
        self.price_Biotique=150
        self.price_Lotus=295


        self.Hair_Oil=['Parachute','Patanjali','Emami',"Dabur",'Amway']
        self.price_Parachute=200
        self.price_Patanjali=180
        self.price_Emami=150
        self.price_Dabur=215
        self.price_Amway=230


        self.Shampoo=['HeadnShoulders','Clinic_Plus','Sunsilk','Garnier','Pantene']
        self.price_HeadnShoulders=350
        self.price_Clinic_Plus=325
        self.price_Sunsilk=360
        self.price_Garnier=400
        self.price_Pantene=500


        self.Face_Wash=['Mamaearth','Ponds','VLCC','Everyuth','FairnLovely']
        self.price_Mamaearth=180
        self.price_Ponds=150
        self.price_VLCC=130
        self.price_Everyuth=110
        self.price_FairnLovely=90

        self.Body_Wash=['Aveeno','Pears','Biotique','Dove','Nivea']
        self.price_Aveeno=250
        self.price_Pears=120
        self.price_Biotique=140
        self.price_Dove=130
        self.price_Nivea=190

        self.Moisturizer=['Clinique','Mcaffeine','Lotus','Olay','Lakme' ]
        self.price_Clinique=2300
        self.price_Mcaffeine=300
        self.price_Lotus=280
        self.price_Olay=640
        self.price_Lakme=150

        self.Room_Freshner=['Godrej','Airwick','Odonil','Ambi_Pur','Glade']
        self.price_Godrej=290
        self.price_Airwick=350
        self.price_Odonil=206
        self.price_Ambi_Pur=210
        self.price_Glade=95

        self.ToothPaste=['Colgate','Pepsodent','Sensodyne','Meswak','Close_up']
        self.price_Colgate=55
        self.price_Pepsodent=95
        self.price_Sensodyne=120
        self.price_Meswak=150
        self.price_Close_up=40


        #SubCatEdibles
        self.SubCatEdibles=['Biscuit','Mayonnaise','Sauce','ColdDrinks','Noodels','Salt','Sugar']

        self.Biscuit=['Bourbon','Good_Day','Unibic','Oreo','KrackJack']
        self.price_Bourbon=75
        self.price_Good_Day=45
        self.price_Unibic=65
        self.price_Oreo=50
        self.price_KrackJack=30

        self.Mayonnaise=['Funfoods','Veeba','Heinz','Del_Monte','Cremica']
        self.price_Funfoods=150
        self.price_Veeba=165
        self.price_Heinz=450
        self.price_Del_Monte=180
        self.price_Cremica=260

        self.Sauce=['Maggi','Kissan','Heinz','Tops','Ching_Chinese']
        self.price_Maggi=170
        self.price_Kissan=200
        self.price_Heinz=150
        self.price_Tops=130
        self.price_Ching_Chinese=450

        self.ColdDrinks=['Pepsi','Coca_Cola','Maaza','Sprite','Thumsup']
        self.price_Pepsi=40
        self.price_Coca_Cola=40
        self.price_Maaza=40
        self.price_Sprite=40
        self.price_Thumsup=40

        self.Noodels=['Maggi','Yippee','Top_Ramen','Chings','Patanjali']
        self.price_Maggi=45
        self.price_Yippee=72
        self.price_Top_Ramen=80
        self.price_Chings=60
        self.price_Patanjali=20


        self.Salt=['Tata','Aashirvaad','Saffola','Catch','Annapurna']
        self.price_Tata=58
        self.price_Aashirvaad=40
        self.price_Saffola=35
        self.price_Catch=62
        self.price_Annapurna=20


        self.Sugar=['Dhampure','Fortune','Sugarlite','Trust','Vedaka']
        self.price_Dhampure=80
        self.price_Fortune=55
        self.price_Sugarlite=64
        self.price_Trust=65
        self.price_Vedaka=70
        
        
        
         #SubCatMobiles
        self.SubCatMobiles=["Oneplus","Samsung","Nokia","Vivo"]

        self.Oneplus=['Nord','7Pro','7Tpro','9R','10R']
        self.price_Nord=30000
        self.price_7Pro=32000
        self.price_7Tpro=36000
        self.price_9R=40000
        self.price_10R=56000

        self.Samsung=['Galaxy_S22Ultra','Galaxy_ZFlip','Galaxy_ZFold','Galaxy_Note20Ultra','Galaxy_s22']
        self.price_Galaxy_S22Ultra=110000
        self.price_Galaxy_ZFlip=82000
        self.price_Galaxy_ZFold=150000
        self.price_Galaxy_Note20Ultra=90000
        self.price_Galaxy_s22=85000


        self.Nokia=['Nokia_Play_2_Max','Nokia_X100','Nokia_8','Nokia_X50']
        self.price_Nokia_Play_2_Max=45525
        self.price_Nokia_X100=15999
        self.price_Nokia_8=36999
        self.price_Nokia_X50=14999


        self.Vivo=['Vivo_XFold','Vivo_X80','Vivo_s12Pro','Vivo_V20']
        self.price_Vivo_XFold=109999
        self.price_Vivo_X80=62999
        self.price_Vivo_s12Pro=49999
        self.price_Vivo_V20=31999
        








        #Image1
        img=Image.open("image/banner.jpg")
        img=img.resize((510,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=510,height=130)


        #Image2
        img_1=Image.open("image/scanner.jpg")
        img_1=img_1.resize((510,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=510,y=0,width=510,height=130)


        #Image3
        img_2=Image.open("image/poper.jpg")
        img_2=img_2.resize((510,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1020,y=0,width=510,height=130)

        lbl_title=Label(self.root,text="Supermarket Billing System ",font=("Centuty",30,"bold"),bg="white",fg="salmon")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title,font=("Centuty",12,"bold"),bg="white",fg="salmon")
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="light green")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("Centuty",12,"bold"),bg="light green",fg="salmon")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.", font=("century",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("century",10,"bold"),width=21)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=("arial",12,"bold"),bg='white',text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=("arial",12,"bold"),bg='white',text="Email-id",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Product Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("Centuty",12,"bold"),bg="light green",fg="salmon")
        Product_Frame.place(x=370,y=5,width=660,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,font=("arial",12,"bold"),bg='white',text="Select Category",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",12,"bold"),width=19,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #Subcategory
        self.lblSubCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product
        self.lblproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=("arial",10,"bold"),width=24)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=("arial",10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10,bg="#99CC99")
        MiddleFrame.place(x=10,y=150,width=1020,height=340)

        #Image4
        img_4=Image.open("image/lolo.jpg")
        img_4=img_4.resize((490,315),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_img_4=Label(MiddleFrame,image=self.photoimg_4)
        lbl_img_4.place(x=0,y=0,width=490,height=315)

        #Image5
        img_5=Image.open("image/new.jpg")
        img_5=img_5.resize((490,315),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        lbl_img_5=Label(MiddleFrame,image=self.photoimg_5)
        lbl_img_5.place(x=501,y=0,width=500,height=315)
        

         # Search   
        Search_Frame=Frame (Main_Frame, bd=1, bg="white")
        Search_Frame.place(x=1080, y=12, width=400,height=29)

        self.lblBill=Label(Search_Frame, font=('arial', 12, 'bold'), fg="white", bg="red",text="Bill Number")
        self.lblBill.grid (row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill, font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch=Button (Search_Frame,command=self.find_bill, text="Search", font=('arial',10, 'bold'), bg="orangered",fg="white",width=15 ,cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        #Right frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text='Bill Area',font=('century', 12,'bold'),bg='light green',fg='red')
        RightLabelFrame.place(x=1035,y=45,width=480,height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=("century",12,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        

        #Bill Counter LableFrame

        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter", font= ("century",14, "bold"),bg="light green",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg="light green",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=26)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg='light green',text='Gov Tax',bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',12,'bold'),width=20)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg='light green',text='Total',bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',12,'bold'),width=20 )
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

         # Button Frame
        Btn_Frame=Frame(Bottom_Frame, bd=2,bg="white")
        Btn_Frame.place(x=320,y=10)

        self.BtnAddToCart=Button (Btn_Frame,command=self.AddItems,height=2, text="Add To Cart", font=('arial',15, 'bold'), bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerate=Button (Btn_Frame,command=self.gen_bill,height=2, text="Generate Bill", font=('arial',15, 'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerate.grid(row=0, column=1)

        self.BtnSaveBill=Button (Btn_Frame,command=self.save_bill,height=2, text="Save Bill", font=('arial', 15, 'bold'), bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSaveBill.grid(row=0, column=2)

        self.BtnClear=Button (Btn_Frame,command=self.clear,height=2, text="Clear", font=("arial", 15, 'bold'), bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0, column=3)

        self.BtnExit=Button (Btn_Frame,command=self.root.destroy,height=2, text="Exit", font=('arial',15, 'bold'), bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0, column=4)

        self.BtnPrint=Button (Btn_Frame,command=self.iprint,height=2, text="Print", font=('arial', 15, 'bold'), bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=5)
        self.welcome() 


        self.L=[]
#===================================FUNCTION DECLARATION=============================
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"WELCOME TO SUPERMARKET BILLING STATION")
        self.textarea.insert(END,"                                      ")
        self.textarea.insert(END,f"\nBill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\nCustomer Email:{self.c_email.get()}")
        self.textarea.insert(END,f"\nPhone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n=========================================")
        self.textarea.insert(END,f"\nProducts \t\tQTY\t\tPrice") 
        self.textarea.insert(END,f"\n=========================================\n")
        
    def AddItems(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.L.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Select The Product Name")
        else:
            
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.L))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.L))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.L))+((((sum(self.L))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("ERROR","Please Add Any Product To The Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.L))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n========================================")
            self.textarea.insert(END,f"\nSub_Amount:\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\nTax_Amount:\t\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\nTotal_Amount:\t\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n========================================")

    def save_bill(self):
        
        op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bill/'+str(self.bill_no.get())+".txt","w") 
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"bill no:{self.bill_no.get()} Save Successful")
            f1.close()

        
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]== self.search_bill.get():
             f1=open(f'bill/{i}','r')
             self.textarea.delete(1.0,END)
             for d in f1:
                self.textarea.insert(END,d)
             f1.close()
             found="yes"
            if found=="no":
                messagebox.showerror("Error","Invalid Bill Number")


    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_email.set("")
        self.c_phon.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.L=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()

    def Categories(self,event=''):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Edibles":
            self.ComboSubCategory.config(value=self.SubCatEdibles)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.Pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T_Shirt":
            self.ComboProduct.config(value=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Sweaters":
            self.ComboProduct.config(value=self.Sweaters)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hoodies":
            self.ComboProduct.config(value=self.Hoodies)
            self.ComboProduct.current(0)


        #LifeStyle
        if self.ComboSubCategory.get()=="Bath_Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face_Cream":
            self.ComboProduct.config(value=self.Face_Cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair_Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shampoo":
            self.ComboProduct.config(value=self.Shampoo)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face_Wash":
            self.ComboProduct.config(value=self.Face_Wash)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Body_Wash":
            self.ComboProduct.config(value=self.Body_Wash)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Moisturizer":
            self.ComboProduct.config(value=self.Moisturizer)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Room_Freshner":
            self.ComboProduct.config(value=self.Room_Freshner)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="ToothPaste":
            self.ComboProduct.config(value=self.ToothPaste)
            self.ComboProduct.current(0)

        #Edilbes
        if self.ComboSubCategory.get()=="Biscuit":
            self.ComboProduct.config(value=self.Biscuit)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Mayonnaise":
            self.ComboProduct.config(value=self.Mayonnaise)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Sauce":
            self.ComboProduct.config(value=self.Sauce)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="ColdDrinks":
            self.ComboProduct.config(value=self.ColdDrinks)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Noodels":
            self.ComboProduct.config(value=self.Noodels)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Salt":
            self.ComboProduct.config(value=self.Salt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Sugar":
            self.ComboProduct.config(value=self.Sugar)
            self.ComboProduct.current(0)

        #Mobiles
        if self.ComboSubCategory.get()=="Oneplus":
            self.ComboProduct.config(value=self.Oneplus)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Nokia":
            self.ComboProduct.config(value=self.Nokia)
            self.ComboProduct.current(0)

        
        if self.ComboSubCategory.get()=="Vivo":
            self.ComboProduct.config(value=self.Vivo)
            self.ComboProduct.current(0)

    def price(self,event=""):
        #Pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Diesel":
            self.ComboPrice.config(value=self.price_Diesel)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Wrangler":
            self.ComboPrice.config(value=self.price_Wrangler)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="CalvinKlein":
            self.ComboPrice.config(value=self.price_CalvinKlein)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="AllenSolly":
            self.ComboPrice.config(value=self.price_AllenSolly)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T-Shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="JacknJones":
            self.ComboPrice.config(value=self.price_JacknJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Armani":
            self.ComboPrice.config(value=self.price_Armani)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_Spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt
        if self.ComboProduct.get()=="Peter_England":
            self.ComboPrice.config(value=self.price_Peter_Englands)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Van_Heusen":
            self.ComboPrice.config(value=self.price_Van_Heusen)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis_Phillipe":
            self.ComboPrice.config(value=self.price_Louis_Phillipe)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park_Avenue":
            self.ComboPrice.config(value=self.price_Park_Avenue)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="US_Polo":
            self.ComboPrice.config(value=self.price_US_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lee":
            self.ComboPrice.config(value=self.price_Lee)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Sweaters
        if self.ComboProduct.get()=="Tommy_Hilfiger":
            self.ComboPrice.config(value=self.price_Tommy_Hilfiger)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="GAP":
            self.ComboPrice.config(value=self.price_GAP)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Forever_21":
            self.ComboPrice.config(value=self.price_Forever_21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Blackberrys":
            self.ComboPrice.config(value=self.price_Blackberrys)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ether":
            self.ComboPrice.config(value=self.price_Ether)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Hoodies
        if self.ComboProduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_Puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Flying_Machine":
            self.ComboPrice.config(value=self.price_Flying_Machine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nautica":
            self.ComboPrice.config(value=self.price_Nautica)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nike":
            self.ComboPrice.config(value=self.price_Nike)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Wrogn":
            self.ComboPrice.config(value=self.price_Wrogn)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        #Bath-Soap
        if self.ComboProduct.get()=="Dettol":
            self.ComboPrice.config(value=self.price_Dettol)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_Lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Life_Boy":
            self.ComboPrice.config(value=self.price_Life_Boy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pears":
            self.ComboPrice.config(value=self.price_Pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face_Cream
        if self.ComboProduct.get()=="Himalaya":
            self.ComboPrice.config(value=self.price_Himalaya)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nivea":
            self.ComboPrice.config(value=self.price_Nivea)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Loreal":
            self.ComboPrice.config(value=self.price_Loreal)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Biotique":
            self.ComboPrice.config(value=self.price_Biotique)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lotus":
            self.ComboPrice.config(value=self.price_Lotus)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Hair_Oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_Parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Patanjali":
            self.ComboPrice.config(value=self.price_Patanjali)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Emami":
            self.ComboPrice.config(value=self.price_Emami)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dabur":
            self.ComboPrice.config(value=self.price_Dabur)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Amway":
            self.ComboPrice.config(value=self.price_Amway)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Shampoo
        if self.ComboProduct.get()=="HeadnShoulders":
            self.ComboPrice.config(value=self.price_HeadnShoulders)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Clinic_Plus":
            self.ComboPrice.config(value=self.price_Clinic_Plus)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sunsilk":
            self.ComboPrice.config(value=self.price_Sunsilk)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_Garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Wrogn":
            self.ComboPrice.config(value=self.price_Wrogn)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pantene":
            self.ComboPrice.config(value=self.price_Pantene)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Face_Wash
        if self.ComboProduct.get()=="Mamaearth":
            self.ComboPrice.config(value=self.price_Mamaearth)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_Ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="VLCC":
            self.ComboPrice.config(value=self.price_VLCC)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Everyuth":
            self.ComboPrice.config(value=self.price_Everyuth)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="FairnLovely":
            self.ComboPrice.config(value=self.price_FairnLovely)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Body_Wash
        if self.ComboProduct.get()=="Aveeno":
            self.ComboPrice.config(value=self.price_Aveeno)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pears":
            self.ComboPrice.config(value=self.price_Pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Biotique":
            self.ComboPrice.config(value=self.price_Biotique)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dove":
            self.ComboPrice.config(value=self.price_Dove)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nivea":
            self.ComboPrice.config(value=self.price_Nivea)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Moisturizer    
        if self.ComboProduct.get()=="Clinique":
            self.ComboPrice.config(value=self.price_Clinique)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mcaffeine":
            self.ComboPrice.config(value=self.price_Mcaffeine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lotus":
            self.ComboPrice.config(value=self.price_Lotus)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_Olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lakme":
            self.ComboPrice.config(value=self.price_Lakme)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Room_Freshner
        if self.ComboProduct.get()=="Godrej":
            self.ComboPrice.config(value=self.price_Godrej)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Airwick":
            self.ComboPrice.config(value=self.price_Airwick)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Odonil":
            self.ComboPrice.config(value=self.price_Odonil)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ambi_Pur":
            self.ComboPrice.config(value=self.price_Ambi_Pur)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Glade":
            self.ComboPrice.config(value=self.price_Glade)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #ToothPaste
        if self.ComboProduct.get()=="Colgate":
            self.ComboPrice.config(value=self.price_Colgate)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pepsodent":
            self.ComboPrice.config(value=self.price_Pepsodent)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sensodyne":
            self.ComboPrice.config(value=self.price_Sensodyne)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Meswak":
            self.ComboPrice.config(value=self.price_Meswak)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Close_up":
            self.ComboPrice.config(value=self.price_Close_up)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Biscuit
        if self.ComboProduct.get()=="Bourbon":
            self.ComboPrice.config(value=self.price_Bourbon)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Good_Day":
            self.ComboPrice.config(value=self.price_Good_Day)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Unibic":
            self.ComboPrice.config(value=self.price_Unibic)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oreo":
            self.ComboPrice.config(value=self.price_Oreo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="KrackJack":
            self.ComboPrice.config(value=self.price_KrackJack)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Mayonnaise
        if self.ComboProduct.get()=="Funfoods":
            self.ComboPrice.config(value=self.price_Funfoods)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Veeba":
            self.ComboPrice.config(value=self.price_Veeba)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Heinz":
            self.ComboPrice.config(value=self.price_Heinz)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Del_Monte":
            self.ComboPrice.config(value=self.price_Del_Monte)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Cremica":
            self.ComboPrice.config(value=self.price_Cremica)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Sauce
        if self.ComboProduct.get()=="Maggi":
            self.ComboPrice.config(value=self.price_Maggi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Kissan":
            self.ComboPrice.config(value=self.price_Kissan)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Heinz":
            self.ComboPrice.config(value=self.price_Heinz)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Tops":
            self.ComboPrice.config(value=self.price_Tops)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ching_Chinese":
            self.ComboPrice.config(value=self.price_Ching_Chinese)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #ColdDrinks
        if self.ComboProduct.get()=="Pepsi":
            self.ComboPrice.config(value=self.price_Pepsi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Coca_Cola":
            self.ComboPrice.config(value=self.price_Coca_Cola)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Maaza":
            self.ComboPrice.config(value=self.price_Maaza)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sprite":
            self.ComboPrice.config(value=self.price_Sprite)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Thumsup":
            self.ComboPrice.config(value=self.price_Thumsup)
            self.ComboPrice.current(0)
            self.qty.set(1)
        

        #Noodels
        if self.ComboProduct.get()=="Maggi":
            self.ComboPrice.config(value=self.price_Maggi)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Yippee":
            self.ComboPrice.config(value=self.price_Yippee)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Top_Ramen":
            self.ComboPrice.config(value=self.price_Top_Ramen)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Chings":
            self.ComboPrice.config(value=self.price_Chings)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Patanjali":
            self.ComboPrice.config(value=self.price_Patanjali)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Salt
        if self.ComboProduct.get()=="Tata":
            self.ComboPrice.config(value=self.price_Tata)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Aashirvaad":
            self.ComboPrice.config(value=self.price_Aashirvaad)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Saffola":
            self.ComboPrice.config(value=self.price_Saffola)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Catch":
            self.ComboPrice.config(value=self.price_Catch)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Annapurna":
            self.ComboPrice.config(value=self.price_Annapurna)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Sugar
        if self.ComboProduct.get()=="Dhampure":
            self.ComboPrice.config(value=self.price_Dhampure)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Fortune":
            self.ComboPrice.config(value=self.price_Fortune)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sugarlite":
            self.ComboPrice.config(value=self.price_Sugarlite)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Trust":
            self.ComboPrice.config(value=self.price_Trust)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vedaka":
            self.ComboPrice.config(value=self.price_Vedaka)
            self.ComboPrice.current(0)
            self.qty.set(1)
        #Oneplus
        if self.ComboProduct.get()=="Nord":
            self.ComboPrice.config(value=self.price_Nord)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="7Pro":
            self.ComboPrice.config(value=self.price_7Pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="7Tpro":
            self.ComboPrice.config(value=self.price_7Tpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="9R":
            self.ComboPrice.config(value=self.price_9R)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get()=="10R":
            self.ComboPrice.config(value=self.price_10R)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Samsung
        if self.ComboProduct.get()=="Galaxy_S22Ultra":
            self.ComboPrice.config(value=self.price_Galaxy_S22Ultra)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy_ZFlip":
            self.ComboPrice.config(value=self.price_Galaxy_ZFlip)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy_ZFold":
            self.ComboPrice.config(value=self.price_Galaxy_ZFold)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy_Note20Ultra":
            self.ComboPrice.config(value=self.price_Galaxy_Note20Ultra)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy_s22":
            self.ComboPrice.config(value=self.price_Galaxy_s22)
            self.ComboPrice.current(0)
            self.qty.set(1)
        

        #Nokia
        if self.ComboProduct.get()=="Nokia_Play_2_Max":
            self.ComboPrice.config(value=self.price_Nokia_Play_2_Max)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nokia_X100":
            self.ComboPrice.config(value=self.price_Nokia_X100)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nokia_8":
            self.ComboPrice.config(value=self.price_Nokia_8)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Nokia_X50":
            self.ComboPrice.config(value=self.price_Nokia_X50)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Vivo
        if self.ComboProduct.get()=="Vivo_XFold":
            self.ComboPrice.config(value=self.price_Vivo_XFold)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vivo_X80":
            self.ComboPrice.config(value=self.price_Vivo_X80)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vivo_s12Pro":
            self.ComboPrice.config(value=self.price_Vivo_s12Pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Vivo_V20":
            self.ComboPrice.config(value=self.price_Vivo_V20)
            self.ComboPrice.current(0)
            self.qty.set(1)
        





        



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
      










