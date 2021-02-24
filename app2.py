from tkinter import *
import tkinter as tk
from tkinter import Text
from tkinter import messagebox
from tkinter import ttk

wind = Tk()
wind.geometry("1250x450")
wind.title("Inventory Management")

# --variables--
nm = StringVar()
p_id = StringVar()
p_sp = StringVar()
p_qty = StringVar()


# --Function to insert data in file--
def insert():
    name = nm.get()
    id = p_id.get()
    sp = p_sp.get()
    qty = p_qty.get()
    k = 0

    if name == "" or id == "" or sp == "" or qty == "":
        messagebox.showerror("Error", "Please enter valid info")
        
    elif id.upper().isupper() or sp.upper().isupper() or qty.upper().isupper():
        messagebox.showerror("Error", "Please enter numeric value")

    else :
        data_file = open("data.txt",'a') #creates file if not present
        data_file.close()
        data_file = open("data.txt",'r')
        for val in data_file.readlines():
            if id in val.split("->"):
                k = 1
                break
        data_file.close()
        if k == 1:
            messagebox.showerror("Error", "ID already exists")
            inp_id.delete(0, 'end')
        else:
            data_file = open("data.txt","r")
            lines = data_file.read().splitlines()
            if len(lines) == 0:
                srno = 1
            else :
                last_line = lines[-1]
                last_line = last_line.split("->")
                srno = int(last_line[0]) + 1

            data_file.close()
            data_file = open("data.txt",'a')
            str1 = str(srno)+"->"+id+"->"+name+"->"+sp+ "->" +qty+ "\n"
            data_file.write(str1)
            inp_id.delete(0, 'end')
            inp_name.delete(0, 'end')
            inp_sp.delete(0, 'end')
            inp_qty.delete(0, 'end')
            messagebox.showinfo("Successfull", "Registered Successfully")
            data_file.close()

# --Function to display data--
def display():
    prd_list.delete(*prd_list.get_children())
    global count
    count = 0
    data_file = open("data.txt","r")
    lines = data_file.read().splitlines()
    if len(lines) == 0:
        messagebox.showerror("Data not found", "No data to show")
    else:
        for val in lines:
            prd_list.insert(parent='',index='end',iid=count, text='', values=val.split("->"))
            count+=1

# --Function to close the application
def close():
    wind.destroy()

    # -- Design --
# --Input Frame--
f1 = LabelFrame(wind,font=( 'aria' ,14 ), text = 'Inventory Management' , padx = 10 , pady = 10 , height = 100, width = 220)
f1.pack(fill = Y , expand = False , side = LEFT)

label_id = Label(f1, font=( 'aria' ,12 ),text="Product Id : ",fg="Black")
label_id.place(x=0 , y=0)

inp_id = Entry(f1,font=( 'aria' ,12 ),width=15,textvar=p_id)
inp_id.place(x=0 , y=35)

label_name = Label(f1, font=( 'aria' ,12 ),text="Product Name : ",fg="Black")
label_name.place(x=0 , y= 70)

inp_name = Entry(f1,font=( 'aria' ,12, ),width=15,textvar=nm)
inp_name.place(x=0 , y= 105)

label_sp = Label(f1, font=( 'aria' ,12 ),text="Selling Price : ",fg="Black")
label_sp.place(x=0 , y= 140)

inp_sp = Entry(f1,font=( 'aria' ,12, ),width=15,textvar=p_sp)
inp_sp.place(x=0 , y= 175)

label_qty = Label(f1, font=( 'aria' ,12 ),text="Quantity : ",fg="Black")
label_qty.place(x=0 , y = 215)

inp_qty = Entry(f1,font=( 'aria' ,12, ),width=15,textvar=p_qty)
inp_qty.place(x=0 , y = 250)

btn_insert = Button(f1,text="Insert",width=10, command = insert)
btn_insert.place(x=0,y = 310)

btn_show = Button(f1,text="Show",width=10, command = display)
btn_show.place(x=100,y = 310)

btn_close = Button(f1,text="Exit",width=10 , bg = "Red", command = close)
btn_close.place(x=50,y = 375)

# -- Output Frame --
f2 = LabelFrame(wind,font=( 'aria' ,14 ), text = 'Product list' , padx = 10 , pady = 10)
f2.pack(fill = BOTH , expand = True , side = LEFT)

prd_list = ttk.Treeview(f2 , selectmode ='browse' , columns = (1,2,3,4,5) , show = "headings")
prd_list.pack(side = TOP , fill = BOTH , expand = True)
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 12))
style.configure("Treeview",
                background = '#f5f8da',
                rowheight = 30
                )

style.map("Treeview", background = [('selected' , 'Green')])

prd_list.column("1", anchor = CENTER , width = 50)
prd_list.column("2", anchor = CENTER)
prd_list.column("3", anchor = CENTER)
prd_list.column("4", anchor = CENTER)
prd_list.column("5", anchor = CENTER , width = 75)

prd_list.heading("1", text ="Item no.", anchor = CENTER)
prd_list.heading("2", text ="Product ID", anchor = CENTER)
prd_list.heading("3", text ="Name", anchor = CENTER)
prd_list.heading("4", text ="Selling Price", anchor = CENTER)
prd_list.heading("5", text ="Quantity", anchor = CENTER)


wind.mainloop()
