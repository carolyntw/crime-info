"""
A program that stores Los Angelos crime incidents:
Type, Day,
Month, Year,
Street, Zipcode

User can:
View all
Search incident
Add incident
Update incident
Delete
Close
"""
from errno import E2BIG
from tkinter import *
from crime_info_backend import Database

database = Database("crimes.db")

def get_selected_row(event):
    #when the function is called, the indented block under try will be executed.
    #if there is an IndexError, the block would not be executed. Pass=do nothing.
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
    except IndexError:
        pass


def view_command():
    #ensure deleting all from the index of zero to the end
    list1.delete(0,END)
    for row in database.view():
        #the new rows will be put at the end of the list box
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(type_text.get(),street_text.get(),zipcode_text.get(),day_text.get(),month_text.get(),year_text.get()):
        list1.insert(END,row)

def insert_command():
    database.insert(type_text.get(),street_text.get(),zipcode_text.get(),day_text.get(),month_text.get(),year_text.get())
    list1.delete(0,END)
    list1.insert(END,(type_text.get(),street_text.get(),zipcode_text.get(),day_text.get(),month_text.get(),year_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],type_text.get(),street_text.get(),zipcode_text.get(),day_text.get(),month_text.get(),year_text.get())


window = Tk()
window.wm_title("CrimeInfo")

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

type_text = StringVar()
e1=Entry(window,textvariable=type_text)
e1.grid(row=0,column=1)

street_text = StringVar()
e2=Entry(window,textvariable =street_text)
e2.grid(row=0,column=3)

zipcode_text = StringVar()
e3=Entry(window,textvariable =zipcode_text)
e3.grid(row=0,column=5)

day_text = StringVar()
e4=Entry(window,textvariable = day_text)
e4.grid(row=1,column=1)

month_text = StringVar()
e5=Entry(window,textvariable = month_text)
e5.grid(row=1,column=3)

year_text = StringVar()
e6=Entry(window,textvariable = year_text)
e6.grid(row=1,column=5)

list1 = Listbox(window, height=6,width=45)
list1.grid(row=2,column=0,rowspan=6,columnspan=4)

#scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=6)

#apply a configure method to the list box, and a configure method to the scroll bar object
#these configure methods get arguments
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="View all", width = 12, command = view_command)
b1.grid(row=2,column=5)

b2 = Button(window,text="Search incident", width = 12, command = search_command)
b2.grid(row=3,column=5)

b3 = Button(window,text="Add incident", width = 12, command = insert_command)
b3.grid(row=4,column=5)

b4 = Button(window,text="Update selected", width = 12, command = update_command)
b4.grid(row=5,column=5)

b5 = Button(window,text="Delete selected", width = 12, command = delete_command)
b5.grid(row=6,column=5)

b6 = Button(window,text="Close", width = 12, command= window.destroy)
b6.grid(row=7,column=5)

window.mainloop()