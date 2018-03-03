

"""
A program that keeps track of transactions and stores buyer's perception parameters for
additional analysis enabling the detection of recurrent unnecessary expenses.

+-----|-------|-------|-----------|-------------|-----------|------------+
+iden-+-fecha-+-monto-+-categoría-+-descripción-+-necesidad-+-importancia+
+-----|-------|-------|-----------|-------------|-----------|------------+
User can:

View all historical transactions
Search an entry
Add entry
Update entry
Delete
Close



Eventually will:

view graphics of expenses
"""

import time
import tkinter
from backend import Database

database = Database("finanzas.db")

window = tkinter.Tk()


def view_command():
    list1.delete(0, tkinter.END)
    for row in database.view():
        list1.insert(tkinter.END, row)


def search_command():
    list1.delete(0, tkinter.END)
    for row in database.search(num_id.get(), fecha_entry.get(), monto_entry.get(), categ_entry.get(),
                               descrip_entry.get(), neces_entry.get(), import_entry.get()):
        list1.insert(tkinter.END, row)


def add_command():
    database.insert(num_id.get(), fecha_entry.get(), monto_entry.get(), categ_entry.get(), descrip_entry.get(),
                    neces_entry.get(), import_entry.get())
    list1.delete(0, tkinter.END)
    list1.insert(tkinter.END, (
        num_id.get(), fecha_entry.get(), monto_entry.get(), categ_entry.get(), descrip_entry.get(), neces_entry.get(),
        import_entry.get()))
    if list1.get(index) == 0:
        time.sleep(2)
        for row in database.view():
            list1.insert(tkinter.END, row)
    view_command()        

def get_select_row(event):
    global selected
    index = list1.curselection()[0]
    selected = list1.get(index)
    e1.delete(0, tkinter.END)
    e1.insert(tkinter.END, selected[0])
    e2.delete(0, tkinter.END)
    e2.insert(tkinter.END, selected[1])
    e3.delete(0, tkinter.END)
    e3.insert(tkinter.END, selected[2])
    e4.delete(0, tkinter.END)
    e4.insert(tkinter.END, selected[3])
    e5.delete(0, tkinter.END)
    e5.insert(tkinter.END, selected[4])
    e6.delete(0, tkinter.END)
    e6.insert(tkinter.END, selected[5])
    e7.delete(0, tkinter.END)
    e7.insert(tkinter.END, selected[6])


def delete_command():
    database.delete(selected[0])
    view_command()

def update_command():
    database.update(num_id.get(), fecha_entry.get(), monto_entry.get(), categ_entry.get(), descrip_entry.get(),
                    neces_entry.get(), import_entry.get())
    view_command()

#######################################LABELS

window.wm_title("Expenses")

l1 = tkinter.Label(window, text="Transaction ID", height=4, width=15)
l1.grid(row=2, column=0)

l2 = tkinter.Label(window, text="Date", height=2)
l2.grid(row=3, column=0)

l3 = tkinter.Label(window, text="Amount", width=15)
l3.grid(row=3, column=2)

l4 = tkinter.Label(window, text="Category")
l4.grid(row=3, column=4)

l5 = tkinter.Label(window, text="Description", height=4)
l5.grid(row=4, column=0)

l6 = tkinter.Label(window, text="Necessity")
l6.grid(row=4, column=2)

l7 = tkinter.Label(window, text="Importance")
l7.grid(row=4, column=4)

spacer1 = tkinter.Label(window, text="", height=4)
spacer1.grid(row=7, column=4)

spacer2 = tkinter.Label(window, text="", height=12)
spacer2.grid(row=0, column=0)

######################################FIELD ENTRY
num_id = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=num_id)
e1.grid(row=2, column=1, rowspan=1, columnspan=1)

fecha_entry = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable=fecha_entry)
e2.grid(row=3, column=1)

monto_entry = tkinter.StringVar()
e3 = tkinter.Entry(window, textvariable=monto_entry)
e3.grid(row=3, column=3)

categ_entry = tkinter.StringVar()
e4 = tkinter.Entry(window, textvariable=categ_entry)
e4.grid(row=3, column=5)

descrip_entry = tkinter.StringVar()
e5 = tkinter.Entry(window, textvariable=descrip_entry)
e5.grid(row=4, column=1)

neces_entry = tkinter.StringVar()
e6 = tkinter.Entry(window, textvariable=neces_entry)
e6.grid(row=4, column=3)

import_entry = tkinter.StringVar()
e7 = tkinter.Entry(window, textvariable=import_entry)
e7.grid(row=4, column=5)

####################################################LIST AND SCROLL

list1 = tkinter.Listbox(window, height=10, width=118)
list1.grid(row=0, column=0, rowspan=1, columnspan=6)

scrollb = tkinter.Scrollbar(window)
scrollb.grid(row=0, column=6)

list1.configure(yscrollcommand=scrollb.set)
scrollb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_select_row)

###################################################BUTTONS

b1 = tkinter.Button(window, text="See All", width=15, command=view_command)
b1.grid(row=1, column=4)

b2 = tkinter.Button(window, text="Search", width=15, command=search_command)
b2.grid(row=1, column=5)

b3 = tkinter.Button(window, text="Add", width=15, height=2, command=add_command)
b3.grid(row=5, column=3)

b4 = tkinter.Button(window, text="Update", width=15, height=2, command=update_command)
b4.grid(row=5, column=4)

b5 = tkinter.Button(window, text="Delete", width=15, height=2, command=delete_command)
b5.grid(row=5, column=5)

b6 = tkinter.Button(window, text="Close", width=15, height=2, command=window.destroy)
b6 = tkinter.Button(window, text="Close", width=15, height=2, command=window.destroy)
b6.grid(row=7, column=5)

window.mainloop()
