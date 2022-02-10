import tkinter as tk
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.ttk import Combobox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to the Jungle")
        self.geometry('800x600')
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)
        self.qnt0 = tk.StringVar()
        self.qnt1 = tk.StringVar()
        self.qnt2 = tk.StringVar()
        self.cost0 = tk.StringVar()
        self.cost1 = tk.StringVar()
        self.cost2 = tk.StringVar()
        self.cost3 = tk.StringVar()
        self.cost4 = tk.StringVar()
        self.cost5 = tk.StringVar()
        self.fCost0 = 0
        self.fCost1 = 0
        self.fCost2 = 0
        self.finalCost = tk.StringVar()
        self.cCnt0 = tk.StringVar()
        self.cCnt1 = tk.StringVar()
        self.cCnt2 = tk.StringVar()
        self.cnt0 = 0
        self.cnt1 = 0
        self.cnt2 = 0
        self.qnt0.set('0')
        self.qnt1.set('0')
        self.qnt2.set('0')
        self.cost0.set('$0.00')
        self.cost1.set('$0.00')
        self.cost2.set('$0.00')
        self.cost3.set('$0.00')
        self.cost4.set('$0.00')
        self.cost5.set('$0.00')
        self.finalCost.set('$0.00')
        self.create_widgets()
        self.cCnt0.set('0')
        self.cCnt1.set('0')
        self.cCnt2.set('0')

    #interaction
    def clicked0(self):
        try:
            self.cnt0 += int(self.qnt0.get())
            self.cnt1 += int(self.qnt1.get())
            self.cnt2 += int(self.qnt2.get())
            self.qnt0.set('0')
            self.qnt1.set('0')
            self.qnt2.set('0')
            self.cost0.set('$0.00')
            self.cost1.set('$0.00')
            self.cost2.set('$0.00')
        except:
            print("Error with input")
        try:
            self.cCnt0.set(str(self.cnt0))
            self.cCnt1.set(str(self.cnt1))
            self.cCnt2.set(str(self.cnt2))
        except:
            print('Could not set cCnt value')
        try:
            self.priceCalc3(self)
            self.priceCalc4(self)
            self.priceCalc5(self)
        except:
            print('Cart totals failed to calculate')
        try:
            text = "$"+ str(self.fCost0+self.fCost1+self.fCost2)
            self.finalCost.set(text)
        except:
            print('Final Cost Tally Failed')

    #checkout interaction
    def checkout(self):
        showwarning(title='Stupid Hobbitses', message='All your cookies are belong to us')
    
    def create_widgets(self):
        #Column 0
        lbl0=Label(self, text="What would you like to order?")
        lbl2=Label(self,text="Thin Mints")
        lbl3=Label(self,text="Tagalongs")
        lbl4=Label(self,text="Savannah")
        btn0=Button(self,text="Add to Cart")
        lbl9=Label(self,text="----------Cart--------")
        lbl10=Label(self,text="Thin Mints")
        lbl11=Label(self,text="Tagalongs")
        lbl12=Label(self,text="Savannah")
        btn1=Button(self,text="Checkout")
        btn0.configure(command=self.clicked0)
        btn1.configure(command=self.checkout)
        
          #column 1
        lbl5=Label(self,text="Price")
        lbl6=Label(self,text="$7.50")
        lbl7=Label(self,text="$6.00")
        lbl8=Label(self,text="$9.00")
        lbl21=Label(self,text="Price")
        lbl22=Label(self,text="$7.50")
        lbl23=Label(self,text="$6.00")
        lbl24=Label(self,text="$9.00")
        



        #column 2
        lbl1=Label(self, text="Qnt.")
        self.in0=Entry(self,width=5,textvariable=self.qnt0)
        self.in1=Entry(self,width=5,textvariable=self.qnt1)
        self.in2=Entry(self,width=5,textvariable=self.qnt2)
        lbl14=Label(self,text="Quantity")
        lbl15=Label(self,textvariable=self.cCnt0)
        lbl16=Label(self,textvariable=self.cCnt1)
        lbl17=Label(self,textvariable=self.cCnt2)
        lbl26=Label(self,text='Cart Total-->')
        
        #column 3
        lbl13=Label(self,text="Total")
        self.in3=Label(self,width=7,textvariable=self.cost0)
        self.in0.bind("<Any-KeyRelease>", self.priceCalc0)
        self.in4=Label(self,width=7,textvariable=self.cost1)
        self.in1.bind("<Any-KeyRelease>", self.priceCalc1)
        self.in5=Label(self,width=7,textvariable=self.cost2)
        self.in2.bind("<Any-KeyRelease>", self.priceCalc2)
        lbl18=Label(self,textvariable=self.cost3)
        lbl19=Label(self,textvariable=self.cost4)
        lbl20=Label(self,textvariable=self.cost5)
        lbl25=Label(self,textvariable=self.finalCost)

        #layout
        lbl0.grid(column=0,row=0)
        lbl1.grid(column=2,row=0)
        lbl2.grid(column=0,row=1)
        lbl3.grid(column=0,row=2)
        lbl4.grid(column=0,row=3)
        lbl5.grid(column=1,row=0)
        lbl6.grid(column=1,row=1)
        lbl7.grid(column=1,row=2)
        lbl8.grid(column=1,row=3)
        lbl9.grid(column=0,row=5)
        lbl10.grid(column=0,row=6)
        lbl11.grid(column=0,row=7)
        lbl12.grid(column=0,row=8)
        lbl13.grid(column=3,row=0)
        lbl14.grid(column=2,row=5)
        lbl15.grid(column=2,row=6)
        lbl16.grid(column=2,row=7)
        lbl17.grid(column=2,row=8)
        lbl18.grid(column=3,row=6)
        lbl19.grid(column=3,row=7)
        lbl20.grid(column=3,row=8)
        lbl21.grid(column=1,row=5)
        lbl22.grid(column=1,row=6)
        lbl23.grid(column=1,row=7)
        lbl24.grid(column=1,row=8)
        lbl25.grid(column=3,row=9)
        lbl26.grid(column=2,row=9)
        btn0.grid(column=0,row=4)
        btn1.grid(column=3,row=10)
        self.in0.grid(column=2,row=1)
        self.in1.grid(column=2,row=2)
        self.in2.grid(column=2,row=3)
        self.in3.grid(column=3,row=1)
        self.in4.grid(column=3,row=2)
        self.in5.grid(column=3,row=3)

    def priceCalc0(self,arg):
        #print("Cost 1 funtion running")
        try:
            text = '$' + str(int(self.qnt0.get())*7.50)
            self.cost0.set(text)
        except:
            #print('Not a valid number')
            self.cost0.set('$0.00')


    def priceCalc1(self,arg):
        #print("Cost 2 funtion running")
        try:
            text = '$' + str(int(self.qnt1.get())*6.00)
            self.cost1.set(text)
        except:
            #print('Not a valid number')
            self.cost1.set('$0.00')
        

    def priceCalc2(self,arg):
        #print("Cost 3 funtion running")
        try:
            text = '$' + str(int(self.qnt2.get())*9.00)
            self.cost2.set(text)
        except:
            #print('Not a valid number')
            self.cost2.set('$0.00')

    def priceCalc3(self,arg):
        #print("Cost 4 funtion running")
        try:
            self.fCost0=int(self.cCnt0.get())*7.50
            text = '$' + str(self.fCost0)
            self.cost3.set(text)
        except:
            #print('Not a valid number')
            self.cost3.set('$0.00')


    def priceCalc4(self,arg):
        #print("Cost 5 funtion running")
        try:
            self.fCost1=int(self.cCnt1.get())*6.00
            text = '$' + str(self.fCost1)
            self.cost4.set(text)
        except:
            #print('Not a valid number')
            self.cost4.set('$0.00')
        

    def priceCalc5(self,arg):
        #print("Cost 6 funtion running")
        try:
            self.fCost2=int(self.cCnt2.get())*9.00
            text = '$' + str(self.fCost2)
            self.cost5.set(text)
        except:
            #print('Not a valid number')
            self.cost5.set('$0.00')
        

#creates the persistance loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
