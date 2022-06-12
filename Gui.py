from tkinter import * 
import pandas as pd #lire les fichiers excels/csv (bd)
import random  #generation des nombres aleatoires 
import time 

#*******Dataset******
#stockage des prix 
prix = pd.read_excel("Prix.xlsx")

les_prix = {}
prod = list(prix['Produit'])
prices = list(prix['Prix'])

for i in range(len(prod)):
    les_prix[prod[i]]=prices[i]



#*****GUI*****
root = Tk()
root.geometry("1400x700+0+0")
root.title("Gestion de Pâtisserie")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='logo-patisserie.png'))


text_Input = StringVar()
operator = ""

def time_t():
    localtime= time.asctime(time.localtime(time.time())) 
    lblInfo.config(text=localtime)
    lblInfo.after(1000,time_t) #refresh

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnCalcul():
    global operator
    try :
        calcul = str(eval(operator))
        text_Input.set(calcul)
        operator = ""
    except :
        operator = ""
        text_Input.set("")

def Ref():

    x = random.randint(10000,50876)
    randomRef = str(x)
    rand.set(randomRef)
    
    Cm = float(Muffins.get())
    CC = float(Croissants.get())
    Cma = float(Macaron.get())
    CG = float(Gateaux.get() )
    CCa =float(Cake.get())
    CD = float(Cafe.get())
    CP = float(Pain.get())

    Tm = Cm * les_prix["Muffins"]
    TC = CC * les_prix["Croissants"]
    TCa = Cma * les_prix["Macaron "]
    TG = CG * les_prix["Gateaux"]
    TCCa = CCa * les_prix["Cake"]
    TD = CD * les_prix["Café & Boissons"]
    TP = CP * les_prix["Pain"]

    all = Tm+TC+TCa+TG+TCCa+TD+TP 

    Total_prix = "TND" , str("%.2f" % (all))
    Taxes = "TND" , str("%.2f" % ((all) * 0.09)) #Valeur TVA 9%
    sercives = "TND" , str("%.2f" % ((all)/99))
    prix_brute = "TND" , str("%.2f" %(all + (all*0.09) + (all/99)))
    
    Service.set(sercives)
    Tax.set(Taxes)
    Total.set(Total_prix)
    Total_cost.set(prix_brute)
    facture()

def Exit():
    root.destroy()

def Reset():
    global operator
    operator = ""
    text_Input.set("")
    rand.set("")
    Muffins.set("0")
    Croissants.set("0")
    Macaron.set("0")
    Gateaux.set("0") 
    Cake.set("0")
    Cafe.set("0")
    Pain.set("0")
    Service.set("")
    Tax.set("")
    Total.set("")
    Total_cost.set("")

Tops = Frame(root, width = 1600,height = 50 ,bg="", relief=SUNKEN) 
Tops.pack(side=TOP) 
f1 = Frame(root, width = 800,height = 700,bg="", relief=SUNKEN) 
f1.pack(side=LEFT) 
f2 = Frame(root, width = 300,height = 700,bg="#BFB8DA", relief=SUNKEN) 
f2.pack(side=RIGHT)  


"""img = PhotoImage(file="logo-patisserie.png") 
logo = Label(Tops,image=img, width=250,height=200)
logo.grid(row=0,column=0,rowspan=2)"""

#*********Top window*********
lblInfo = Label(Tops, font=('arial',50, 'bold'), text="Système de Gestion de Pâtisserie ",fg="#708ae9", bd=6, anchor="w")
lblInfo.grid(row=0,column=1,columnspan=3)
lblInfo = Label(Tops, font=('arial',20, 'bold'),fg="Black", bd=6, anchor="w")
lblInfo.grid(row=1,column=1,columnspan=3)
time_t() #en cours changement 1s


#*****Calculator*****
txtDisplap = Entry(f2,font=('arial', 20,'bold'), textvariable=text_Input, bd=15, insertwidth=14, bg='#DFE1F3', justify='right') 
txtDisplap.grid(columnspan=4) 
 
btn1 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="1",bg="#BFB8DA",command=lambda:btnClick(1)).grid(row=2,column=0)
btn2 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="2",bg="#BFB8DA",command=lambda:btnClick(2)).grid(row=2,column=1)
btn3 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="3",bg="#BFB8DA",command=lambda:btnClick(3)).grid(row=2,column=2)
Addition = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="+",bg="#BFB8DA",command=lambda:btnClick("+")).grid(row=2,column=3)

btn4 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="4",bg="#BFB8DA",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="5",bg="#BFB8DA",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="6",bg="#BFB8DA",command=lambda:btnClick(6)).grid(row=3,column=2)
sub = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="-",bg="#BFB8DA",command=lambda:btnClick("-")).grid(row=3,column=3)


btn7 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="7",bg="#BFB8DA",command=lambda:btnClick(7)).grid(row=4,column=0)
btn8 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="8",bg="#BFB8DA",command=lambda:btnClick(8)).grid(row=4,column=1)
btn9 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="9",bg="#BFB8DA",command=lambda:btnClick(9)).grid(row=4,column=2)
mult = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="*",bg="#BFB8DA",command=lambda:btnClick("*")).grid(row=4,column=3)

btn0 = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="0",bg="#BFB8DA",command=lambda:btnClick(0)).grid(row=5,column=0)
C = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="C",bg="#BFB8DA",command=lambda:btnClear()).grid(row=5,column=1)
equal = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="=",bg="#BFB8DA",command=lambda:btnCalcul()).grid(row=5,column=2)
divs = Button(f2,padx=12,pady=12,bd=6,fg="black",font=('arial', 18,'bold'),text="/",bg="#BFB8DA",command=lambda:btnClick("/")).grid(row=5,column=3)

#**********MENU**********

rand = StringVar() #reference
Muffins = StringVar() 
Croissants = StringVar() 
Macaron = StringVar() 
Gateaux = StringVar() 
Cake = StringVar() 

lblReference = Label(f1,font=("arial", 16,"bold"), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0,column=0) 
txtReference= Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=rand, bd=6, insertwidth=4, justify = 'right') 
txtReference.grid(row=0,column=1) 

lblMuffins = Label(f1,font=("arial", 16,"bold"), text="Muffins", bd=16, anchor="w")
lblMuffins.grid(row=1,column=0) 
txtMuffins=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Muffins, bd=6, insertwidth=4, justify = 'right') 
txtMuffins.grid(row=1,column=1) 

lblCroissants = Label(f1,font=("arial", 16,"bold"), text="Croissants", bd=16, anchor="w")
lblCroissants.grid(row=2,column=0) 
txtCroissants=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Croissants, bd=6, insertwidth=4, justify = 'right') 
txtCroissants.grid(row=2,column=1) 

lblMacaron = Label(f1,font=("arial", 16,"bold"), text="Macaron", bd=16, anchor="w")
lblMacaron.grid(row=3,column=0) 
txtMacaron=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Macaron, bd=6, insertwidth=4, justify = 'right') 
txtMacaron.grid(row=3,column=1) 

lblGateaux = Label(f1,font=("arial", 16,"bold"), text="Gateaux", bd=16, anchor="w")
lblGateaux.grid(row=4,column=0) 
txtGateaux=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Gateaux, bd=6, insertwidth=4, justify = 'right') 
txtGateaux.grid(row=4,column=1) 

lblCake = Label(f1,font=("arial", 16,"bold"), text="Cake", bd=16, anchor="w")
lblCake.grid(row=5,column=0) 
txtCake=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Cake, bd=6, insertwidth=4, justify = 'right') 
txtCake.grid(row=5,column=1) 



#******Side_Menu*****

Cafe = StringVar() 
Pain = StringVar() 
Service = StringVar() 
Tax = StringVar() 
Total = StringVar() 
Total_cost = StringVar() 

#Set all the meal to 0
Muffins.set("0")
Croissants.set("0")
Macaron.set("0")
Gateaux.set("0") 
Cake.set("0")
Cafe.set("0")
Pain.set("0")

lblCafe = Label(f1,font=("arial", 16,"bold"), text="Café & Boissons", bd=16, anchor="w")
lblCafe.grid(row=0,column=2) 
txtCafe=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Cafe, bd=6, insertwidth=4, justify = 'right') 
txtCafe.grid(row=0,column=3) 

lblPain = Label(f1,font=("arial", 16,"bold"), text="Pain", bd=16, anchor="w")
lblPain.grid(row=1,column=2) 
txtPain=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Pain, bd=6, insertwidth=4, justify = 'right') 
txtPain.grid(row=1,column=3) 

lblService = Label(f1,font=("arial", 16,"bold"), text="Services", bd=16, anchor="w")
lblService.grid(row=2,column=2) 
txtService=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Service, bd=6, insertwidth=4, justify = 'right') 
txtService.grid(row=2,column=3) 

lblTax = Label(f1,font=("arial", 16,"bold"), text="Taxes", bd=16, anchor="w")
lblTax.grid(row=3,column=2) 
txtTax=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Tax, bd=6, insertwidth=4, justify = 'right') 
txtTax.grid(row=3,column=3) 

lblTotal = Label(f1,font=("arial", 16,"bold"), text="Coût Net", bd=16, anchor="w")
lblTotal.grid(row=4,column=2) 
txtTotal=Entry(f1,font=("arial", 16,"bold"), bg="#F2D5E6",textvariable=Total, bd=6, insertwidth=4, justify = 'right') 
txtTotal.grid(row=4,column=3) 

lblTotal_cost = Label(f1,font=("arial", 16,"bold"), text="Coût total", bd=16, anchor="w")
lblTotal_cost.grid(row=5,column=2) 
txtTotal_cost =Entry(f1,font=("arial", 16,"bold"), bg="#9BCED0",textvariable=Total_cost, bd=6, insertwidth=4, justify = 'right') 
txtTotal_cost.grid(row=5,column=3) 

#*****Function Buttons ******
btnTotal = Button(f1,padx=12,pady=8,bd=5,fg="black",font=('arial', 18,'bold'),width=10,text="Total",bg="#9BCED0",command=Ref).grid(row=7,column=1)
btnTotal = Button(f1,padx=12,pady=8,bd=5,fg="black",font=('arial', 18,'bold'),width=10,text="Réinitialiser",bg="#9BCED0",command=Reset).grid(row=7,column=2)
btnTotal = Button(f1,padx=12,pady=8,bd=5,fg="black",font=('arial', 18,'bold'),width=10,text="Quitter",bg="#9BCED0",command=Exit).grid(row=7,column=3)



#*****Facture interface*****
def save(ref,net,total):
    Historique = pd.read_excel("Historique.xlsx")
    date = time.asctime(time.localtime(time.time())) 
    new_row = {'Référence':ref, 'Date':date, 'Prix_net':net, 'Prix_total':total}
    Historique = Historique.append(new_row, ignore_index=True)
    
    Historique.to_excel("Historique.xlsx")

def facture():
    
        window = Toplevel(root)
        window.geometry("300x450+0+0")
        window.title("Facture")
        window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo-patisserie.png'))
        bg = PhotoImage(file='mini.png')
        background = Label(window, image=bg)
        background.place(x=0, y=0)
        
        label = Label(window,text="Merci pour votre visite!!",font=('arial', 18,'bold'), justify = 'center')
        label.grid(row=0,column=0,columnspan=2)

        ref = float(rand.get())
        Cm = float(Muffins.get())
        CC = float(Croissants.get())
        Cma = float(Macaron.get())
        CG = float(Gateaux.get())
        CCa =float(Cake.get())
        CD = float(Cafe.get())
        CP = float(Pain.get())

        Tm = Cm * les_prix["Muffins"] ; Vtm = "TND" , str("%.2f" % (Tm))
        TC = CC * les_prix["Croissants"] ; Vtc = "TND" , str("%.2f" % (TC))
        TCa = Cma * les_prix["Macaron "] ; Vtca = "TND" , str("%.2f" % (TCa))
        TG = CG * les_prix["Gateaux"] ; Vtg = "TND" , str("%.2f" % (TG))
        TCCa = CCa * les_prix["Cake"] ; Vtcca = "TND" , str("%.2f" % (TCCa))
        TD = CD * les_prix["Café & Boissons"] ; Vtd = "TND" , str("%.2f" % (TD))
        TP = CP * les_prix["Pain"] ; Vtp = "TND" , str("%.2f" % (TP))

        label1 = Label(window,text="Muffins :",font=('arial', 15)).grid(row=1,column=0)
        label11 = Label(window,text=Vtm,font=('arial', 14)).grid(row=1,column=1)

        label2 = Label(window,text="Croissants :",font=('arial', 15)).grid(row=2,column=0)
        label21 = Label(window,text=Vtc,font=('arial', 14)).grid(row=2,column=1)

        label3 = Label(window,text="Macaron :",font=('arial', 15)).grid(row=3,column=0)
        label31 = Label(window,text=Vtca,font=('arial', 14)).grid(row=3,column=1)

        label4 = Label(window,text="Gateaux :",font=('arial', 15)).grid(row=4,column=0)
        label41 = Label(window,text=Vtg,font=('arial', 14)).grid(row=4,column=1)

        label5 = Label(window,text="Cake :",font=('arial', 15)).grid(row=5,column=0)
        label51 = Label(window,text=Vtcca,font=('arial', 14)).grid(row=5,column=1)

        label6 = Label(window,text="Café & Boissons :",font=('arial', 15)).grid(row=6,column=0)
        label61 = Label(window,text=Vtd,font=('arial', 14)).grid(row=6,column=1)

        label7 = Label(window,text="Pain :",font=('arial', 15)).grid(row=7,column=0)
        label71 = Label(window,text=Vtp,font=('arial', 14)).grid(row=7,column=1)


        all = Tm+TC+TCa+TG+TCCa+TD+TP
        tot = all + (all*0.09) + (all/99)

        Total_prix = "TND" , str("%.2f" % (all))
        tax_sercives = "TND" , str("%.2f" % (all/99+all* 0.09))
        prix_brute = "TND" , str("%.2f" %(tot))

        label8 = Label(window,text="Total Net :",font=('arial', 15,"bold")).grid(row=8,column=0)
        label81 = Label(window,text=Total_prix,font=('arial', 14)).grid(row=8,column=1)
        label9 = Label(window,text="Taxes & sercives :",font=('arial', 15,"bold")).grid(row=9,column=0)
        label91 = Label(window,text=tax_sercives,font=('arial', 14)).grid(row=9,column=1)
        label10 = Label(window,text="Total Brute :",font=('arial', 15,"bold")).grid(row=10,column=0)
        label101 = Label(window,text=prix_brute,font=('arial', 14)).grid(row=10,column=1)
        empty = Label(window,text="",font=('arial', 14)).grid(row=11,column=0)

        btnTotal = Button(window,padx=12,pady=8,bd=4,fg="black",font=('arial', 15,'bold'),text="Sauvegarder",bg="#FFE0C1",command=lambda:save(ref,all,tot), justify = 'center').grid(row=12,column=0,columnspan=3)

        window.mainloop()
    

root.mainloop()
