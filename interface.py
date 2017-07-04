"""
A program that keeps track of transactions and stores buyer's perception parameters for
additional analysis enabling the detection of recurrent unnecessary expenses.

+-----|-------|-------|-----------|-------------|-----------|------------+
+iden-+-fecha-+-monto-+-categoria-+-descripción-+-necesidad-+-importancia+
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
from tkinter import  *
import backend

window=Tk()

def view_command():
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in backend.search(num_id.get(),fecha_entry.get(),monto_entry.get(),categ_entry.get(),descrip_entry.get(),neces_entry.get(),import_entry.get()):
		list1.insert(END,row)

def add_command():
	backend.insert(num_id.get(),fecha_entry.get(),monto_entry.get(),categ_entry.get(),descrip_entry.get(),neces_entry.get(),import_entry.get())
	list1.delete(0,END)
	list1.insert(END,(num_id.get(),fecha_entry.get(),monto_entry.get(),categ_entry.get(),descrip_entry.get(),neces_entry.get(),import_entry.get()))

def get_select_row(event):
	global selected
	index=list1.curselection()[0]
	selected=list1.get(index)
	e1.delete(0,END)
	e1.insert(END,selected[0])
	e2.delete(0,END)
	e2.insert(END,selected[1])
	e3.delete(0,END)
	e3.insert(END,selected[2])
	e4.delete(0,END)
	e4.insert(END,selected[3])
	e5.delete(0,END)
	e5.insert(END,selected[4])
	e6.delete(0,END)
	e6.insert(END,selected[5])
	e7.delete(0,END)
	e7.insert(END,selected[6])


def delete_command():
	backend.delete(selected[0])

def update_command():
	backend.update(num_id.get(),fecha_entry.get(),monto_entry.get(),categ_entry.get(),descrip_entry.get(),neces_entry.get(),import_entry.get())


#######################################LABELS

window.wm_title("Los Gastos")

l1=Label(window,text="ID compra",height=4,width=15)
l1.grid(row=2,column=0)

l2=Label(window,text="Fecha",height=2)
l2.grid(row=3,column=0)

l3=Label(window,text="Monto",width=15)
l3.grid(row=3,column=2)

l4=Label(window,text="Categoría")
l4.grid(row=3,column=4)

l5=Label(window,text="Descripción",height=4)
l5.grid(row=4,column=0)

l6=Label(window,text="Necesidad")
l6.grid(row=4,column=2)

l7=Label(window,text="Importancia")
l7.grid(row=4,column=4)

spacer1=Label(window,text="",height=4)
spacer1.grid(row=7,column=4)

spacer2=Label(window,text="",height=12)
spacer2.grid(row=0,column=0)


######################################FIELD ENTRY
num_id=StringVar()
e1=Entry(window,textvariable=num_id)
e1.grid(row=2,column=1,rowspan=1,columnspan=1)

fecha_entry=StringVar()
e2=Entry(window,textvariable=fecha_entry)
e2.grid(row=3,column=1)

monto_entry=StringVar()
e3=Entry(window,textvariable=monto_entry)
e3.grid(row=3,column=3)

categ_entry=StringVar()
e4=Entry(window,textvariable=categ_entry)
e4.grid(row=3,column=5)

descrip_entry=StringVar()
e5=Entry(window,textvariable=descrip_entry)
e5.grid(row=4,column=1)

neces_entry=StringVar()
e6=Entry(window,textvariable=neces_entry)
e6.grid(row=4,column=3)

import_entry=StringVar()
e7=Entry(window,textvariable=import_entry)
e7.grid(row=4,column=5)

####################################################LIST AND SCROLL

list1=Listbox(window,height=10,width=118)
list1.grid(row=0,column=0,rowspan=1,columnspan=6)

scrollb=Scrollbar(window)
scrollb.grid(row=0,column=6)

list1.configure(yscrollcommand=scrollb.set)
scrollb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_select_row)

###################################################BUTTONS

b1=Button(window,text="Ver todas",width=15,command=view_command)
b1.grid(row=1,column=4)

b2=Button(window,text="Buscar",width=15,command=search_command)
b2.grid(row=1,column=5)

b3=Button(window,text="Añadir",width=15,height=2,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Actualizar selección",width=15,height=2,command=update_command)
b4.grid(row=5,column=4)

b5=Button(window,text="Borrar Selección",width=15,height=2,command=delete_command)
b5.grid(row=5,column=5)

b6=Button(window,text="Cerrar",width=15,height=2,command=window.destroy)
b6.grid(row=7,column=5)

window.mainloop()
