"""
A program that stores Los Angelos crime incidents:
Type, Day, Month, Year, Street, Zipcode

User can:
View all, Search incident, Add incident, Update incident, Delete ,Close
""" 
from errno import E2BIG
from tkinter import *
from crime_info_backend import Database

database = Database("crimes.db")

class Window(object):

    def __init__(self,window):
        
        self.window = window

        self.window.wm_title("CrimeInfo")

        l1 = Label(window,text="Type")
        l1.grid(row=0,column=0)

        l2 = Label(window,text="Street")
        l2.grid(row=0,column=2)

        l3 = Label(window,text="Zipcode")
        l3.grid(row=0,column=4)

        l4 = Label(window,text="Day")
        l4.grid(row=1,column=0)

        l5 = Label(window,text="Month")
        l5.grid(row=1,column=2)

        l6 = Label(window,text="Year")
        l6.grid(row=1,column=4)

        self.type_text = StringVar()
        self.e1=Entry(window,textvariable = self.type_text)
        self.e1.grid(row=0,column=1)

        self.street_text = StringVar()
        self.e2=Entry(window,textvariable = self.street_text)
        self.e2.grid(row=0,column=3)

        self.zipcode_text = StringVar()
        self.e3=Entry(window,textvariable =self.zipcode_text)
        self.e3.grid(row=0,column=5)

        self.day_text = StringVar()
        self.e4=Entry(window,textvariable = self.day_text)
        self.e4.grid(row=1,column=1)

        self.month_text = StringVar()
        self.e5=Entry(window,textvariable = self.month_text)
        self.e5.grid(row=1,column=3)

        self.year_text = StringVar()
        self.e6=Entry(window,textvariable = self.year_text)
        self.e6.grid(row=1,column=5)

        self.list1 = Listbox(window, height=6,width=45)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=4)

        #scroll bar
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=4,rowspan=6)

        #apply a configure method to the list box, and a configure method to the scroll bar object
        #these configure methods get arguments
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1 = Button(window,text="View all", width = 12, command = self.view_command)
        b1.grid(row=2,column=5)

        b2 = Button(window,text="Search incident", width = 12, command = self.search_command)
        b2.grid(row=3,column=5)

        b3 = Button(window,text="Add incident", width = 12, command = self.insert_command)
        b3.grid(row=4,column=5)

        b4 = Button(window,text="Update selected", width = 12, command = self.update_command)
        b4.grid(row=5,column=5)

        b5 = Button(window,text="Delete selected", width = 12, command = self.delete_command)
        b5.grid(row=6,column=5)

        b6 = Button(window,text="Close", width = 12, command= window.destroy)
        b6.grid(row=7,column=5)
        
    def get_selected_row(self,event):
        #when the function is called, the indented block under try will be executed.
        #if there is an IndexError, the block would not be executed. Pass=do nothing.
        try:
            global selected_tuple
            self.index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(self.index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
            self.e5.delete(0,END)
            self.e5.insert(END,self.selected_tuple[5])
            self.e6.delete(0,END)
            self.e6.insert(END,self.selected_tuple[6])
        except IndexError:
            pass


    def view_command(self):
        #ensure deleting all from the index of zero to the end
        self.list1.delete(0,END)
        for row in database.view():
            #the new rows will be put at the end of the list box
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.type_text.get(),self.street_text.get(),self.zipcode_text.get(),self.day_text.get(),self.month_text.get(),self.year_text.get()):
            self.list1.insert(END,row)

    def insert_command(self):
        database.insert(self.type_text.get(),self.street_text.get(),self.zipcode_text.get(),self.day_text.get(),self.month_text.get(),self.year_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.type_text.get(),self.street_text.get(),self.zipcode_text.get(),self.day_text.get(),self.month_text.get(),self.year_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0],self.type_text.get(),self.street_text.get(),self.zipcode_text.get(),self.day_text.get(),self.month_text.get(),self.year_text.get())


window=Tk()
Window(window)
window.mainloop()